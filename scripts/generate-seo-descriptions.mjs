import fs from 'node:fs';
import path from 'node:path';

const docsDir = path.resolve('docs');
const outputPath = path.resolve('src/generated/seo-descriptions.json');
const overridesPath = path.resolve('scripts/seo-description-overrides.json');
const overrides = JSON.parse(fs.readFileSync(overridesPath, 'utf8'));

function walk(directory) {
  return fs.readdirSync(directory, {withFileTypes: true}).flatMap((entry) => {
    const resolved = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(resolved) : [resolved];
  });
}

function stripYamlQuotes(value) {
  return value?.trim().replace(/^['"]|['"]$/g, '');
}

function escapeRegExp(value) {
  return value.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
}

function cleanInline(value = '') {
  return value
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/[`*_]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function normalizeTerms(value) {
  return value
    .replace(/\bmitre\b/gi, 'MITRE')
    .replace(/\bpowershell\b/gi, 'PowerShell')
    .replace(/\.net\b/gi, '.NET')
    .replace(/\bgui\b/gi, 'GUI')
    .replace(/\bdns\b/gi, 'DNS')
    .replace(/\bc2\b/gi, 'C2')
    .replace(/PowerShell\s*\/\s*C2/g, 'PowerShell and C2')
    .replace(/PowerShell\s*\/\s*VBS/g, 'PowerShell and VBS')
    .replace(/DNS\s*\/\s*C2/g, 'DNS-based C2')
    .replace(/destructive\s*\/\s*extortion/gi, 'destructive extortion')
    .replace(/browser\s*\/\s*webshell/gi, 'browser and web shell')
    .replace(/Lyceum\s*\/\s*HEXANE-associated/g, 'Lyceum and HEXANE-associated')
    .replace(/Void Manticore\s*\/\s*Handala/g, 'Void Manticore or Handala')
    .replace(/Lebanese Cedar\s*\/\s*Volatile Cedar/g, 'Lebanese Cedar or Volatile Cedar')
    .replace(/Pioneer Kitten\s*\/\s*Fox Kitten/g, 'Pioneer Kitten or Fox Kitten')
    .replace(/NetBIOS\s*\/\s*host/g, 'NetBIOS and host')
    .replace(/OTP\s*\/\s*SMS/g, 'OTP and SMS')
    .replace(/PPAM\s*\/\s*XLL\s*\/\s*RAR/g, 'PPAM, XLL, or RAR')
    .replace(/MQTT\s*\/\s*8883/g, 'MQTT on port 8883')
    .replace(/PLC\s*\/\s*HMI\s*\/\s*fuel-controller/g, 'PLC, HMI, or fuel-controller')
    .replace(/first-30-minutes/g, 'first-30-minute')
    .replace(/used as defensive\b/gi, 'used as a defensive')
    .replace(/\bot\s*\/\s*iot\b/gi, 'OT/IoT')
    .replace(/\brat\b/gi, 'RAT')
    .replace(/\s+/g, ' ')
    .trim();
}

function isCompliant(description, title) {
  const openParentheses = (description.match(/\(/g) ?? []).length;
  const closeParentheses = (description.match(/\)/g) ?? []).length;
  return description.length >= 140
    && description.length <= 160
    && description.split(/\s+/).length >= 16
    && !description.toLowerCase().includes(title.toLowerCase())
    && !/\.\.|…/.test(description)
    && /[.!?]$/.test(description)
    && openParentheses === closeParentheses
    && !/\b(?:a|an|and|as|at|by|for|from|in|of|on|or|the|to|with)\.$/i.test(description)
    && !/\b(?:Guide (?:analyst )?review|Inform (?:analyst review|practical defensive analysis)|Apply (?:these findings in defensive analyst work|the evidence and limits in defensible analyst decisions)|Use it to guide analyst review|Use these findings in practical defensive analysis|Support defensible analyst decisions|Use the evidence(?:, limitations, and workflow guidance| and limitations)? to support defensible analysis)\b/i.test(description);
}

function descriptionNgrams(description, size = 6) {
  const words = description.toLowerCase().match(/[a-z0-9&.-]+/g) ?? [];
  return new Set(
    Array.from({length: Math.max(0, words.length - size + 1)}, (_, index) => words.slice(index, index + size).join(' ')),
  );
}

function preservesEditorialDiversity(description, ngramCounts) {
  return [...descriptionNgrams(description)].every((ngram) => (ngramCounts.get(ngram) ?? 0) < 2);
}

function recordDescriptionNgrams(description, ngramCounts) {
  for (const ngram of descriptionNgrams(description)) {
    ngramCounts.set(ngram, (ngramCounts.get(ngram) ?? 0) + 1);
  }
}

function tableCell(body, sectionName, column) {
  const section = body.match(new RegExp('## ' + escapeRegExp(sectionName) + '\\s+([\\s\\S]*?)(?=\\n##\\s|$)'))?.[1];
  const row = section
    ?.split(/\r?\n/)
    .find((line) => /^\|.*\|$/.test(line.trim()) && !/---|Summary|Notes/.test(line));
  return cleanInline(row?.split('|')[column]);
}

function parseDocument(file) {
  const raw = fs.readFileSync(file, 'utf8');
  const frontMatterMatch = raw.match(/^---\s*\n([\s\S]*?)\n---\s*\n?/);
  const frontMatter = frontMatterMatch?.[1] ?? '';
  const body = frontMatterMatch ? raw.slice(frontMatterMatch[0].length) : raw;
  const title = (
    stripYamlQuotes(frontMatter.match(/^title:\s*(.+?)\s*$/m)?.[1])
    || body.match(/^#\s+(.+?)\s*$/m)?.[1]
    || path.basename(file, path.extname(file))
  ).replace(/\s*\|\s*1200km\s*$/i, '').trim();

  return {body, title};
}

function normalizeToolText(value, title, actors) {
  const titlePattern = new RegExp('(?<![A-Za-z0-9])' + escapeRegExp(title) + '(?![A-Za-z0-9])', 'gi');
  return normalizeTerms(cleanInline(value)
    .replace(titlePattern, 'the software')
    .replace(/\bwin\.the software\b/gi, 'the software')
    .replace(/\bsoftware as software used by this actor\b/gi, 'software as used by ' + actors)
    .replace(/\bsoftware used by this actor\b/gi, 'software used by ' + actors)
    .replace(/\bby the actor\b/gi, 'by ' + actors)
    .replace(/\bthis actor\b/gi, actors)
    .replace(/\bthe actor\b/gi, actors)
    .replace(/\bthis registry utilityistry\b/gi, 'this registry utility'));
}

function toolFocusOptions(type) {
  if (/wiper|destructive|ransomware/.test(type)) {
    return [
      'destructive behavior, recovery impact, IOC handling, and response-focused hunts',
      'execution and impact signals, recovery safeguards, source limits, and validation needs',
      'wiping or encryption behavior, defensive telemetry, indicator caveats, and response scope',
      'impact behavior, recovery risks, indicators, and response hunts',
      'destructive execution, backup risk, telemetry evidence, and incident scope',
      'impact preparation, file changes, recovery controls, and validation gaps',
      'wiping or encryption signals, source context, and response priorities',
      'mass file activity, recovery inhibition, IOC caveats, and hunt design',
      'destructive staging, endpoint evidence, backup safeguards, and triage needs',
      'impact techniques, local telemetry, source provenance, and response guidance',
      'file-system damage, recovery artifacts, mappings, and escalation criteria',
      'pre-impact behavior, destructive actions, evidence limits, and defensive checks',
      'wiper or ransomware signals, indicator status, and incident validation',
      'destructive capability, host evidence, recovery posture, and hunt boundaries',
    ];
  }
  if (/web shell|backdoor|loader|implant|malware|RAT|trojan|dropper/.test(type)) {
    return [
      'execution, persistence, C2 behavior, IOC handling, and defensive hunt context',
      'delivery and execution behavior, persistence signals, source provenance, and hunt limits',
      'behavior evidence, command-and-control context, indicators, mappings, and validation gaps',
      'execution, persistence, C2, indicators, and hunt scope',
      'command execution, persistence paths, network activity, and source caveats',
      'implant delivery, host changes, C2 signals, and defensive validation',
      'payload execution, file activity, communications, and evidence limits',
      'initial delivery, follow-on commands, persistence evidence, and hunt boundaries',
      'host behavior, operator tasking, network indicators, and local baselines',
      'execution ancestry, recurring access, outbound traffic, and triage scope',
      'malware staging, command handling, file transfer, and detection evidence',
      'implant behavior, actor association, IOC context, and telemetry needs',
      'delivery chain, endpoint behavior, C2 patterns, and response guidance',
      'persistence mechanisms, process evidence, connections, and source quality',
      'execution signals, access maintenance, IOC provenance, and hunt planning',
      'loader or implant behavior, command channels, mappings, and validation',
      'endpoint artifacts, persistence, network telemetry, and operational limits',
      'source-backed capabilities, host behavior, C2, and defensive priorities',
      'staging evidence, command activity, indicator handling, and hunt design',
    ];
  }
  if (/mobile|Android|app/.test(type)) {
    return [
      'app delivery, mobile permissions, collection behavior, IOCs, and hunt guidance',
      'installation context, device collection signals, network behavior, and source caveats',
      'mobile execution, data access, C2 evidence, indicator handling, and defensive review',
      'app delivery, data access, network signals, and mobile hunts',
    ];
  }
  if (/living-off|system|network|registry|process|administration|utility|binary/.test(type)) {
    return [
      'authorized-use baselines, process context, mapped behavior, and hunt limitations',
      'expected administration, suspicious execution context, telemetry, and IOC caveats',
      'dual-use behavior, local allowlisting, ATT&CK context, and defensive validation',
      'process context, local baselines, mappings, and hunt limits',
      'expected operator use, parent-process context, telemetry, and escalation limits',
      'administrative baselines, command context, source evidence, and alert scope',
      'legitimate-use controls, execution ancestry, ATT&CK context, and hunt evidence',
      'process lineage, account context, enterprise allowlists, and defensive review',
      'command execution, approved workflows, indicator limits, and telemetry needs',
      'local usage patterns, suspicious invocation, mapping quality, and hunt boundaries',
      'authorized administration, process evidence, network context, and validation gaps',
      'baseline exceptions, execution signals, source provenance, and response guidance',
      'user and host context, command arguments, telemetry quality, and review scope',
      'process ancestry, expected tooling, behavior mappings, and escalation evidence',
      'approved operations, anomalous execution, IOC caveats, and hunt planning',
      'administrative context, invocation patterns, source quality, and alert limits',
    ];
  }
  if (/credential|post-exploitation|framework|offensive/.test(type)) {
    return [
      'credential or execution behavior, dual-use caveats, ATT&CK context, and hunt scope',
      'operator behavior, local baselines, source evidence, mappings, and validation limits',
      'execution context, credential-access signals, IOC handling, and defensive hunting',
      'access behavior, IOCs, mappings, and defensive hunts',
      'credential or execution behavior, local baselines, evidence, and hunt limits',
      'dual-use execution, account context, mapped behavior, and validation needs',
      'operator activity, credential signals, source provenance, and defensive scope',
      'access methods, process evidence, IOC caveats, and investigation guidance',
      'credential use, lateral execution, telemetry context, and hunt boundaries',
      'post-exploitation behavior, local allowlists, mappings, and response priorities',
      'account access, operator tooling, indicator status, and validation evidence',
      'execution and credential context, source quality, and detection limitations',
      'tooling behavior, identity signals, ATT&CK context, and triage guidance',
      'access evidence, process ancestry, credential telemetry, and review scope',
      'dual-use capabilities, approved baselines, source links, and hunt design',
      'credential collection, execution context, IOC handling, and escalation criteria',
    ];
  }
  if (/remote|RMM|tunnel|proxy|cloud sync/.test(type)) {
    return [
      'approved-tool baselines, remote-control behavior, network evidence, and hunt scope',
      'authorized-use checks, connection context, IOC handling, mappings, and validation gaps',
      'remote-access behavior, enterprise inventory, telemetry, and defensive hunt limits',
      'connection behavior, approved-use baselines, and hunt limits',
    ];
  }
  if (/MITRE-listed|associated family/.test(type)) {
    return [
      'source provenance, actor mappings, IOC caveats, and hunt context',
      'association evidence, ATT&CK context, indicators, and validation gaps',
      'source-backed linkage, mapped techniques, IOC status, and review scope',
      'actor linkage, source scope, IOCs, mappings, and hunts',
      'confidence rationale, source references, technique links, and IOC limits',
      'public-source association, mapping quality, indicator status, and hunt scope',
      'evidence lineage, actor context, technique coverage, and validation needs',
      'source quality, reported actor use, ATT&CK mappings, and IOC cautions',
      'association confidence, source records, mapped behaviors, and hunt boundaries',
      'public reporting, actor linkage, IOC handling, and defensive review',
      'evidence provenance, behavior mappings, indicator caveats, and hunt planning',
      'source support, actor context, ATT&CK links, and operational limitations',
      'reported software use, evidence quality, IOC status, and detection gaps',
      'source validation, actor association, mapped techniques, and hunt evidence',
      'source traceability, technique context, IOC limits, and confidence rationale',
    ];
  }
  return [
    'documented behavior, source provenance, IOC handling, mappings, and defensive hunts',
    'evidence context, confidence, indicator caveats, ATT&CK links, and validation limits',
    'behavioral evidence, source scope, IOC status, mapped techniques, and hunt guidance',
    'behavior, source scope, IOCs, mappings, and defensive hunts',
  ];
}

function toolDescription(body, title, used, ngramCounts) {
  const actors = normalizeTerms(cleanInline(body.match(/^- Associated actor\(s\):\s*(.+)$/m)?.[1]))
    .split(';')
    .map((value) => value.trim())
    .filter(Boolean)
    .slice(0, 2)
    .join(' and ');
  const sourceType = normalizeTerms(cleanInline(body.match(/^- Tool type\(s\):\s*(.+)$/m)?.[1]))
    .replace(/\s*\/\s*/g, ' or ')
    .toLowerCase()
    .replace(/\bmitre\b/g, 'MITRE')
    .replace(/\bpowershell\b/g, 'PowerShell')
    .replace(/\.net\b/g, '.NET')
    .replace(/\bgui\b/g, 'GUI')
    .replace(/\bdns\b/g, 'DNS')
    .replace(/\bc2\b/g, 'C2')
    .replace(/\bot or iot\b/g, 'OT/IoT')
    .replace(/\brat\b/g, 'RAT');
  const typeAliases = {
    reg: 'Windows configuration utility',
    net: 'Windows administration utility',
  };
  const type = typeAliases[title.toLowerCase()]
    ?? (sourceType === 'associated family'
      ? 'malware family'
      : sourceType === 'MITRE-listed software or tool'
        ? 'MITRE-listed software'
        : sourceType === 'web shells'
          ? 'web shell'
          : sourceType);
  const confidence = cleanInline(body.match(/^- Confidence level\(s\):\s*(.+)$/m)?.[1]).toLowerCase();
  const sourceIds = cleanInline(body.match(/^- Source ID\(s\):\s*(.+)$/m)?.[1]);

  if (!actors || !type || !confidence || !sourceIds) {
    throw new Error('Tool page lacks required structured facts: ' + title);
  }

  const behavior = normalizeToolText(tableCell(body, 'Behavior', 2), title, actors);
  const hunting = normalizeToolText(tableCell(body, 'Defensive Hunting Notes', 2), title, actors);
  const handling = normalizeToolText(tableCell(body, 'Handling Notes', 2), title, actors);
  const candidates = [];
  const add = (value) => {
    const normalized = value?.replace(/\s+/g, ' ').trim();
    if (normalized && !candidates.includes(normalized)) candidates.push(normalized);
  };

  const genericBehavior = /source-backed software use by/i.test(behavior);
  if (!genericBehavior) add(behavior);
  add(hunting);
  add(handling);
  add(behavior + ' ' + handling);
  add(behavior + ' ' + hunting);

  const behaviorWithoutPeriod = behavior.replace(/[.!?]+$/, '');
  const huntingWithoutPeriod = hunting.replace(/[.!?]+$/, '');
  if (!genericBehavior) add(`${behaviorWithoutPeriod} (${sourceIds}; ${confidence} confidence).`);
  add(`${huntingWithoutPeriod} (${sourceIds}; ${confidence} confidence).`);
  if (!genericBehavior) add(`${behaviorWithoutPeriod}, recorded at ${confidence} confidence under ${sourceIds}.`);
  if (!genericBehavior) add(`Under ${sourceIds} at ${confidence} confidence, ${behavior}`);

  const focusOptions = toolFocusOptions(type);
  const focusOffset = [...title].reduce((sum, character) => sum + character.codePointAt(0), 0) % focusOptions.length;
  const orderedFocusOptions = [...focusOptions.slice(focusOffset), ...focusOptions.slice(0, focusOffset)];
  for (const focus of orderedFocusOptions) {
    add(`Review this ${confidence}-confidence ${type} record for ${actors}, focusing on ${focus} under ${sourceIds}.`);
    add(`Assess ${actors}'s ${confidence}-confidence association with this ${type} through ${focus}, with provenance in ${sourceIds}.`);
    add(`Use ${sourceIds} to review this ${confidence}-confidence ${type} association with ${actors}, including ${focus}.`);
    add(`Examine this ${type} record for ${actors}, rated ${confidence} confidence under ${sourceIds}, with emphasis on ${focus}.`);
    add(`Review ${confidence}-confidence reporting that links ${actors} to this ${type}; the entry covers ${focus}.`);
    add(`Assess a ${confidence}-confidence ${type} entry associated with ${actors}; review ${focus}.`);
    add(`Use this ${confidence}-confidence record to examine ${actors}'s association with a ${type}, including ${focus}.`);
    add(`Examine evidence linking ${actors} to this ${type} at ${confidence} confidence, with attention to ${focus}.`);
    add(`Review the ${confidence}-confidence ${type} association with ${actors}; use the page for ${focus}.`);
    add(`Assess source-backed use of this ${type} by ${actors}, rated ${confidence} confidence, through ${focus}.`);
    add(`Trace this ${confidence}-confidence ${type} record for ${actors} across ${focus}.`);
    add(`Use the ${confidence}-confidence evidence linking this ${type} to ${actors} to evaluate ${focus}.`);
    add(`Review this ${type} in ${actors} reporting at ${confidence} confidence, with the page covering ${focus}.`);
    add(`Assess the ${confidence}-confidence link between ${actors} and this ${type}; the record documents ${focus}.`);
    add(`Examine this ${type} association with ${actors}, recorded at ${confidence} confidence, for ${focus}.`);
    add(`Use this ${type} record to review ${actors}'s ${confidence}-confidence linkage and ${focus}.`);
    add(`Review ${focus} in this ${confidence}-confidence ${type} entry for ${actors}.`);
    add(`Assess ${focus} through this ${confidence}-confidence ${type} record associated with ${actors}.`);
    add(`For ${actors}, use this ${confidence}-confidence ${type} entry to examine ${focus}.`);
    add(`This page records a ${confidence}-confidence ${type} association with ${actors} and covers ${focus}.`);
    add(`The ${confidence}-confidence ${type} record for ${actors} supports review of ${focus}.`);
    add(`A ${confidence}-confidence ${type} association with ${actors} is documented here alongside ${focus}.`);
    add(`Explore ${focus} for this ${type}, associated with ${actors} at ${confidence} confidence.`);
    add(`Use this ${confidence}-confidence ${type} entry for ${actors} to evaluate ${focus}.`);
    add(`Review the ${type} link to ${actors}, rated ${confidence} confidence, through ${focus}.`);
    add(`Assess this ${confidence}-confidence ${type} relationship with ${actors} using ${focus}.`);
    add(`${actors} is linked at ${confidence} confidence to this ${type}; review ${focus}.`);
    add(`For ${actors}, this ${type} association is rated ${confidence} confidence and documents ${focus}.`);
    add(`Public reporting associates this ${type} with ${actors} at ${confidence} confidence and supports review of ${focus}.`);
    add(`The entry links ${actors} to this ${type} at ${confidence} confidence while documenting ${focus}.`);
    add(`This ${type} is associated with ${actors} at ${confidence} confidence; the page organizes ${focus}.`);
    add(`A source-backed ${type} relationship with ${actors} is rated ${confidence} confidence and covers ${focus}.`);
    add(`Analysts can assess ${focus} through this ${confidence}-confidence ${type} association with ${actors}.`);
    add(`The page supports review of ${focus} for a ${confidence}-confidence ${type} linked to ${actors}.`);
    add(`This entry documents ${focus} for a ${type} linked to ${actors} at ${confidence} confidence.`);
    add(`Review ${actors}'s reported use of this ${type} at ${confidence} confidence through ${focus}.`);
    add(`Assess ${focus} in a source-backed ${type} entry associated with ${actors} at ${confidence} confidence.`);
    add(`Use this page's ${focus} to review a ${confidence}-confidence ${type} relationship with ${actors}.`);
    add(`For a ${type} linked to ${actors} at ${confidence} confidence, review ${focus}.`);
    add(`The ${confidence}-confidence relationship between ${actors} and this ${type} is documented with ${focus}.`);
    add(`This page pairs a ${confidence}-confidence ${type} link to ${actors} with ${focus}.`);
  }

  const selected = candidates.find((candidate) => (
    isCompliant(candidate, title)
    && !used.has(candidate)
    && preservesEditorialDiversity(candidate, ngramCounts)
  ));
  if (!selected) {
    throw new Error('No complete, unique tool description could be composed for "' + title + '".');
  }
  return selected;
}

const files = walk(docsDir).filter((file) => /\.mdx?$/.test(file));
const descriptions = {};
const used = new Map();
const toolNgramCounts = new Map();

for (const file of files) {
  const relative = path.relative(docsDir, file).split(path.sep).join('/');
  const sourceKey = '@site/docs/' + relative;
  const {body, title} = parseDocument(file);
  const override = overrides[sourceKey];
  if (override !== undefined && (typeof override !== 'string' || !isCompliant(override, title))) {
    throw new Error('Invalid curated SEO description for "' + title + '" (' + sourceKey + ').');
  }
  const description = override ?? (
    relative.startsWith('tools/')
      ? toolDescription(body, title, used, toolNgramCounts)
      : undefined
  );
  if (!description) {
    throw new Error('Documentation route lacks a curated SEO description: ' + sourceKey);
  }
  if (used.has(description)) {
    throw new Error('Duplicate SEO description for ' + sourceKey + ' and ' + used.get(description) + '.');
  }
  used.set(description, relative);
  descriptions[sourceKey] = description;
  if (relative.startsWith('tools/') && relative !== 'tools/README.md') {
    if (!preservesEditorialDiversity(description, toolNgramCounts)) {
      throw new Error('Curated tool description repeats a six-word phrase too often: ' + sourceKey);
    }
    recordDescriptionNgrams(description, toolNgramCounts);
  }
}

for (const sourceKey of Object.keys(overrides)) {
  if (!(sourceKey in descriptions)) {
    throw new Error('Curated SEO description does not match a documentation source: ' + sourceKey);
  }
}

fs.mkdirSync(path.dirname(outputPath), {recursive: true});
fs.writeFileSync(outputPath, JSON.stringify(descriptions, null, 2) + '\n');
console.log('Generated ' + Object.keys(descriptions).length + ' unique SEO descriptions at ' + path.relative(process.cwd(), outputPath) + '.');
