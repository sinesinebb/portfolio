<script setup lang="ts">
import type { Project } from '~/composables/useResume'
defineProps<{ project: Project }>()
</script>

<template>
  <NuxtLink :to="`/projets/${project.slug}`" class="card card-hover group flex flex-col">
    <div class="flex items-start justify-between gap-4">
      <div>
        <h3 class="text-xl font-bold">{{ project.title }}</h3>
        <p v-if="project.subtitle" class="mt-1 text-sm text-slate-500 dark:text-slate-400">{{ project.subtitle }}</p>
      </div>
      <span class="mt-1 text-slate-400 transition group-hover:translate-x-1 group-hover:text-brand-500">
        <AppIcon name="arrow" />
      </span>
    </div>

    <p class="mt-4 flex-1 leading-relaxed">{{ project.summary }}</p>

    <dl v-if="project.metrics.length" class="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-4">
      <div v-for="m in project.metrics" :key="m.label" class="rounded-xl bg-slate-100 px-3 py-2 dark:bg-slate-800/70">
        <dt class="text-[11px] uppercase tracking-wide text-slate-500">{{ m.label }}</dt>
        <dd class="font-mono text-lg font-semibold text-brand-600 dark:text-brand-400">{{ m.value }}</dd>
      </div>
    </dl>

    <div class="mt-5 flex flex-wrap gap-2">
      <span v-for="t in project.tech.slice(0, 7)" :key="t" class="chip">{{ t }}</span>
      <span v-if="project.tech.length > 7" class="chip">+{{ project.tech.length - 7 }}</span>
    </div>
  </NuxtLink>
</template>
