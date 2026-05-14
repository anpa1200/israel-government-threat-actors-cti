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
      items: ['israel-government-threat-model', 'source-rating'],
    },
    {
      type: 'category',
      label: 'Methodology',
      collapsed: false,
      items: [
        'methodology/operating-standard',
        'methodology/scoring-models',
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
        'detection-engineering/quality-gates',
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
        'actors/muddywater',
        'actors/apt42',
        'actors/apt35',
        'actors/agrius',
        'actors/cyberav3ngers',
        'actors/cotton-sandstorm',
        'actors/oilrig',
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
        'reports/andrey-medium-articles',
      ],
    },
  ],
};

module.exports = sidebars;
