// @ts-check

const config = {
  title: 'Israel Government Threat Actors CTI',
  tagline: 'Defensive CTI for Israeli government and public-sector exposure',
  favicon: 'img/favicon.svg',

  url: 'https://anpa1200.github.io',
  baseUrl: '/israel-government-threat-actors-cti/',

  organizationName: 'anpa1200',
  projectName: 'israel-government-threat-actors-cti',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

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
          alt: 'Israel CTI shield',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'ctiSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/anpa1200/israel-government-threat-actors-cti',
            label: 'GitHub',
            position: 'right',
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
            title: 'Repository',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/anpa1200/israel-government-threat-actors-cti',
              },
              {
                label: 'Issues',
                href: 'https://github.com/anpa1200/israel-government-threat-actors-cti/issues',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Andrey Pautov. Built with Docusaurus.`,
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
