// @ts-check

const config = {
  title: 'Israel Government Threat Actors CTI',
  tagline: 'Defensive CTI for Israeli government and public-sector exposure',
  favicon: 'img/favicon.svg',

  url: 'https://anpa1200.github.io',
  baseUrl: '/israel-government-threat-actors-cti/',

  organizationName: 'anpa1200',
  projectName: 'israel-government-threat-actors-cti',

  headTags: [
    {
      tagName: 'script',
      attributes: {
        async: 'true',
        src: 'https://www.googletagmanager.com/gtag/js?id=G-TMTG21RVHM',
      },
    },
    {
      tagName: 'script',
      attributes: {},
      innerHTML: `
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-TMTG21RVHM');
      `,
    },
  ],
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
              {label: 'CTI Analyst Field Manual', href: 'https://anpa1200.github.io/cti-analyst-field-manual/'},
              {label: 'CTI as a Code', href: 'https://anpa1200.github.io/CTI_as_a_Code/'},
              {label: 'Operation Desert Hydra', href: 'https://anpa1200.github.io/operation-desert-hydra/'},
              {label: 'Customer-Driven AI CTI', href: 'https://anpa1200.github.io/customer-driven-ai-cti-project/'},
              {label: 'Israel Threat Actors CTI', href: 'https://anpa1200.github.io/israel-government-threat-actors-cti/'},
              {label: 'AI vs Defense', href: 'https://anpa1200.github.io/ai-vs-defense/'},
              {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
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
            href: 'https://anpa1200.github.io/',
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
              {label: 'CTI Analyst Field Manual', href: 'https://anpa1200.github.io/cti-analyst-field-manual/'},
              {label: 'CTI as a Code', href: 'https://anpa1200.github.io/CTI_as_a_Code/'},
              {label: 'Operation Desert Hydra', href: 'https://anpa1200.github.io/operation-desert-hydra/'},
              {label: 'Customer-Driven AI CTI', href: 'https://anpa1200.github.io/customer-driven-ai-cti-project/'},
              {label: 'Israel Threat Actors CTI', href: 'https://anpa1200.github.io/israel-government-threat-actors-cti/'},
              {label: 'AI vs Defense', href: 'https://anpa1200.github.io/ai-vs-defense/'},
              {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
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
