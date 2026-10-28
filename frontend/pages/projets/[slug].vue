<script setup lang="ts">
import type { Project } from '~/composables/useResume'

const route = useRoute()
const { data: project, error } = await useFetch<Project>(`${useApiBase()}/projects/${route.params.slug}/`)

if (error.value) {
  throw createError({ statusCode: 404, statusMessage: 'Projet introuvable', fatal: true })
}
useHead({ title: () => `${project.value?.title ?? 'Projet'} — Yassine Bakouetila` })
</script>

<template>
  <article v-if="project" class="container-page max-w-4xl py-16 sm:py-24">
    <NuxtLink to="/projets" class="inline-flex items-center gap-2 text-sm text-slate-500 hover:text-brand-500">
      <AppIcon name="back" :size="16" /> Tous les projets
    </NuxtLink>

    <h1 class="mt-6 text-4xl font-extrabold tracking-tight sm:text-5xl">{{ project.title }}</h1>
    <p v-if="project.subtitle" class="mt-3 text-lg text-slate-500 dark:text-slate-400">{{ project.subtitle }}</p>
    <p v-if="project.period" class="mt-2 font-mono text-sm text-slate-500">{{ project.period }}</p>

    <div v-if="project.repo_url || project.demo_url" class="mt-6 flex gap-3">
      <a v-if="project.repo_url" :href="project.repo_url" target="_blank" rel="noopener" class="btn-ghost"><AppIcon name="github" :size="16" /> Code</a>
      <a v-if="project.demo_url" :href="project.demo_url" target="_blank" rel="noopener" class="btn-primary"><AppIcon name="external" :size="16" /> Démo</a>
    </div>

    <img v-if="project.image" :src="project.image" :alt="project.title" class="mt-10 w-full rounded-2xl border border-slate-200 dark:border-slate-800">

    <dl v-if="project.metrics.length" class="mt-10 grid grid-cols-2 gap-4 sm:grid-cols-4">
      <div v-for="m in project.metrics" :key="m.label" class="card text-center">
        <dd class="font-mono text-3xl font-bold text-brand-600 dark:text-brand-400">{{ m.value }}</dd>
        <dt class="mt-1 text-xs uppercase tracking-wide text-slate-500">{{ m.label }}</dt>
      </div>
    </dl>

    <div class="mt-10 space-y-4 text-lg leading-relaxed">
      <p v-for="(para, i) in project.description.split('\n\n')" :key="i">{{ para }}</p>
    </div>

    <div v-if="project.highlights.length" class="mt-10">
      <h2 class="text-2xl font-bold">Points clés</h2>
      <ul class="mt-4 space-y-3">
        <li v-for="h in project.highlights" :key="h" class="flex gap-3">
          <AppIcon name="check" :size="18" class="mt-1 shrink-0 text-brand-500" />{{ h }}
        </li>
      </ul>
    </div>

    <div class="mt-10">
      <h2 class="text-2xl font-bold">Technologies</h2>
      <div class="mt-4 flex flex-wrap gap-2">
        <span v-for="t in project.tech" :key="t" class="chip text-sm">{{ t }}</span>
      </div>
    </div>
  </article>
</template>
