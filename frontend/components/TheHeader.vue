<script setup lang="ts">
const open = ref(false)
const route = useRoute()
watch(() => route.fullPath, () => (open.value = false))

const links = [
  { to: '/#a-propos', label: 'À propos' },
  { to: '/#competences', label: 'Compétences' },
  { to: '/projets', label: 'Projets' },
  { to: '/#experience', label: 'Expérience' },
  { to: '/contact', label: 'Contact' },
]
</script>

<template>
  <header class="sticky top-0 z-40 border-b border-slate-200/70 bg-white/80 backdrop-blur dark:border-slate-800/70 dark:bg-slate-950/80">
    <nav class="container-page flex h-16 items-center justify-between">
      <NuxtLink to="/" class="font-mono text-lg font-bold text-slate-900 dark:text-white">
        <span class="text-brand-500">~/</span>yassine
      </NuxtLink>

      <div class="hidden items-center gap-1 md:flex">
        <NuxtLink
          v-for="l in links" :key="l.to" :to="l.to"
          class="rounded-lg px-3 py-2 text-sm font-medium text-slate-600 transition hover:text-slate-900 dark:text-slate-400 dark:hover:text-white"
        >
          {{ l.label }}
        </NuxtLink>
        <ThemeToggle />
      </div>

      <div class="flex items-center gap-1 md:hidden">
        <ThemeToggle />
        <button class="rounded-lg p-2" :aria-label="open ? 'Fermer le menu' : 'Ouvrir le menu'" @click="open = !open">
          <AppIcon :name="open ? 'close' : 'menu'" />
        </button>
      </div>
    </nav>

    <div v-if="open" class="border-t border-slate-200 md:hidden dark:border-slate-800">
      <div class="container-page flex flex-col py-2">
        <NuxtLink v-for="l in links" :key="l.to" :to="l.to" class="py-3 font-medium">{{ l.label }}</NuxtLink>
      </div>
    </div>
  </header>
</template>
