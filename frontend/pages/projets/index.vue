<script setup lang="ts">
useHead({ title: 'Projets — Yassine Bakouetila' })
const { data, error } = useResume()

const filter = ref('Tous')
const allTech = computed(() => {
  const counts = new Map<string, number>()
  data.value?.projects.forEach(p => p.tech.forEach(t => counts.set(t, (counts.get(t) ?? 0) + 1)))
  return ['Tous', ...[...counts.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10).map(([t]) => t)]
})
const projects = computed(() =>
  (data.value?.projects ?? []).filter(p => filter.value === 'Tous' || p.tech.includes(filter.value)),
)
</script>

<template>
  <LoadError v-if="error" />
  <section v-else class="container-page py-16 sm:py-24">
    <SectionTitle eyebrow="projets" title="Mes réalisations" />
    <div class="mb-8 flex flex-wrap gap-2">
      <button
        v-for="t in allTech" :key="t"
        class="rounded-full border px-4 py-1.5 text-sm transition"
        :class="filter === t
          ? 'border-brand-500 bg-brand-500 text-white dark:text-slate-950'
          : 'border-slate-300 hover:border-brand-500 dark:border-slate-700'"
        @click="filter = t"
      >
        {{ t }}
      </button>
    </div>
    <div class="grid gap-6 lg:grid-cols-2">
      <ProjectCard v-for="p in projects" :key="p.id" :project="p" />
    </div>
  </section>
</template>
