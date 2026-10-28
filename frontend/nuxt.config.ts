export default defineNuxtConfig({
  compatibilityDate: '2025-01-01',
  devtools: { enabled: false },
  modules: ['@nuxtjs/tailwindcss', '@nuxtjs/color-mode'],
  css: ['~/assets/css/main.css'],
  colorMode: { classSuffix: '', preference: 'dark', fallback: 'dark' },
  runtimeConfig: {
    // NUXT_API_BASE_SERVER : URL utilisée côté serveur (SSR), optionnelle
    apiBaseServer: '',
    public: {
      // Surchargé par la variable d'environnement NUXT_PUBLIC_API_BASE
      apiBase: 'http://localhost:8000/api',
    },
  },
  app: {
    head: {
      htmlAttrs: { lang: 'fr' },
      title: 'Yassine Bakouetila — Développeur Full Stack & ML Engineer',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        {
          name: 'description',
          content: 'Portfolio de Yassine Mouhamed Bakouetila, développeur full stack, ML engineer et data scientist à Brazzaville.',
        },
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap',
        },
      ],
    },
    pageTransition: { name: 'page', mode: 'out-in' },
  },
})
