// @ts-check

const sidebars = {
  ctiSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: 'Overview',
    },
    {
      type: 'category',
      label: 'Foundations',
      collapsed: false,
      items: [
        'israel-government-threat-model',
        'source-rating',
        'known-limitations',
        'customer-environment-use',
      ],
    },
    {
      type: 'category',
      label: 'Methodology',
      collapsed: false,
      items: [
        'methodology/operating-standard',
        'methodology/scoring-models',
        'methodology/source-freshness',
        'methodology/artifact-contracts',
      ],
    },
    {
      type: 'category',
      label: 'Threat Hunting',
      collapsed: false,
      items: ['threat-hunting/hunt-workflow'],
    },
    {
      type: 'category',
      label: 'Detection Engineering',
      collapsed: false,
      items: [
        'detection-engineering/detection-lifecycle',
        'detection-engineering/detection-status-dashboard',
        'detection-engineering/quality-gates',
        'detection-engineering/platform-field-mapping',
        'detection-engineering/platform-query-variants',
        'detection-engineering/sigma-validation-results',
        'detection-engineering/backend-conversion-results',
        'detection-engineering/soc-triage-playbooks',
        'detection-engineering/soc-handoff-packet',
        'detection-engineering/drl-evidence-packs',
      ],
    },
    {
      type: 'category',
      label: 'Actors',
      collapsed: false,
      link: {
        type: 'doc',
        id: 'actors/README',
      },
      items: [
        'actors/handala',
        'actors/scarred-manticore',
        'actors/muddywater',
        'actors/apt42',
        'actors/apt35',
        'actors/agrius',
        'actors/cyberav3ngers',
        'actors/imperial-kitten',
        'actors/pioneer-kitten',
        'actors/darkbit',
        'actors/lyceum',
        'actors/cotton-sandstorm',
        'actors/oilrig',
        'actors/apt39',
        'actors/arid-viper',
        'actors/wirte',
        'actors/ta402',
        'actors/unc1860',
        'actors/unc3890',
        'actors/cyber-toufan',
        'actors/lebanese-cedar',
      ],
    },
    {
      type: 'category',
      label: 'Reports',
      collapsed: false,
      link: {
        type: 'doc',
        id: 'reports/README',
      },
      items: [
        'reports/defensive-cti-threats-to-israeli-public-sector',
        'reports/israel-critical-infrastructure-escalation',
        'reports/resourses_research',
        'reports/worked-cases',
        'reports/ci-validation-evidence',
        'reports/release-notes',
        'reports/andrey-medium-articles',
      ],
    },
  ],
};

module.exports = sidebars;
