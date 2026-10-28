<script setup lang="ts">
const { data } = useResume()
const profile = computed(() => data.value?.profile)
</script>

<template>
  <footer class="border-t border-slate-200 py-10 dark:border-slate-800">
    <div class="container-page flex flex-col items-center justify-between gap-4 text-sm sm:flex-row">
      <p>© {{ new Date().getFullYear() }} {{ profile?.full_name ?? 'Yassine Bakouetila' }}. Fait avec Nuxt & Django.</p>
      <div class="flex items-center gap-4">
        <a v-if="profile?.email" :href="`mailto:${profile.email}`" aria-label="Email" class="hover:text-brand-500"><AppIcon name="mail" /></a>
        <a v-if="profile?.github_url" :href="profile.github_url" target="_blank" rel="noopener" aria-label="GitHub" class="hover:text-brand-500"><AppIcon name="github" /></a>
        <a v-if="profile?.linkedin_url" :href="profile.linkedin_url" target="_blank" rel="noopener" aria-label="LinkedIn" class="hover:text-brand-500"><AppIcon name="linkedin" /></a>
      </div>
    </div>
  </footer>
</template>
