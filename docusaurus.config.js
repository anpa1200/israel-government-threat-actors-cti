// @ts-check

const config = {
  title: 'Israel Government Threat Actors CTI',
  tagline: 'Defensive CTI for Israeli government and public-sector exposure',
  favicon: 'img/favicon.svg',

  url: 'https://1200km.com',
  baseUrl: '/israel-government-threat-actors-cti/',

  organizationName: 'anpa1200',
  projectName: 'israel-government-threat-actors-cti',

  deploymentBranch: 'gh-pages',
  trailingSlash: true,

  onBrokenLinks: 'warn',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/anpa1200/israel-government-threat-actors-cti/edit/main/',
        },
        blog: false,
        gtag: {trackingID: 'G-TMTG21RVHM', anonymizeIP: true},
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/social-card.svg',
      metadata: [
        {
          name: 'keywords',
          content:
            'cyber threat intelligence, CTI, Israel, Iran, threat actors, Sigma, detection engineering, Docusaurus',
        },
      ],
      navbar: {
        title: 'Israel CTI',
        logo: {
          alt: '1200km',
          src: 'img/logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'ctiSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            to: '/ecosystem',
            label: 'Ecosystem',
            position: 'left',
          },
          {
            label: 'Projects',
            position: 'right',
            items: [
              {label: 'CTI Analyst Field Manual', href: 'https://1200km.com/cti-analyst-field-manual/'},
              {label: 'CTI as a Code', href: 'https://1200km.com/CTI_as_a_Code/'},
              {label: 'Operation Desert Hydra', href: 'https://1200km.com/operation-desert-hydra/'},
              {label: 'Customer-Driven AI CTI', href: 'https://1200km.com/customer-driven-ai-cti-project/'},
              {label: 'Israel Threat Actors CTI', href: 'https://1200km.com/israel-government-threat-actors-cti/'},
              {label: 'AI vs Defense', href: 'https://1200km.com/ai-vs-defense/'},
              {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
              {label: 'ThreatMapper Docs', href: 'https://1200km.com/threatmapper-docs/'},
            ],
          },
          {
            href: 'https://medium.com/@1200km',
            label: 'Medium',
            position: 'right',
          },
          {
            href: 'https://github.com/anpa1200/israel-government-threat-actors-cti',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: 'https://1200km.com/',
            label: 'Main Page',
            position: 'right',
            className: 'navbar-portfolio-btn',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Project',
            items: [
              {
                label: 'Threat Model',
                to: '/israel-government-threat-model',
              },
              {
                label: 'Actor Index',
                to: '/actors/',
              },
              {
                label: 'Report Index',
                to: '/reports/',
              },
            ],
          },
          {
            title: 'Ecosystem',
            items: [
              {label: 'CTI Analyst Field Manual', href: 'https://1200km.com/cti-analyst-field-manual/'},
              {label: 'CTI as a Code', href: 'https://1200km.com/CTI_as_a_Code/'},
              {label: 'Operation Desert Hydra', href: 'https://1200km.com/operation-desert-hydra/'},
              {label: 'Customer-Driven AI CTI', href: 'https://1200km.com/customer-driven-ai-cti-project/'},
              {label: 'Israel Threat Actors CTI', href: 'https://1200km.com/israel-government-threat-actors-cti/'},
              {label: 'AI vs Defense', href: 'https://1200km.com/ai-vs-defense/'},
              {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
              {label: 'ThreatMapper Docs', href: 'https://1200km.com/threatmapper-docs/'},
            ],
          },
          {
            title: 'Author',
            items: [
              {label: 'Medium', href: 'https://medium.com/@1200km'},
              {label: 'GitHub', href: 'https://github.com/anpa1200'},
              {label: 'LinkedIn', href: 'https://www.linkedin.com/in/andrey-pautov/'},
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Andrey Pautov. Israel Government Threat Actors CTI — defensive public-source knowledge base.`,
      },
      prism: {
        additionalLanguages: ['bash', 'json', 'yaml', 'powershell'],
      },
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: true,
      },
    }),
};

module.exports = config;
