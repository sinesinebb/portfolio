<script setup lang="ts">
const { data, error } = useResume()
const profile = computed(() => data.value?.profile)
const featured = computed(() => data.value?.projects.filter(p => p.featured) ?? [])
const levelClass: Record<string, string> = {
  advanced: 'border-brand-400/60 bg-brand-50 text-brand-700 dark:bg-brand-500/10 dark:text-brand-300',
  good: '',
  basic: 'opacity-70',
}
const titles = computed(() => profile.value?.title.split('·').map(t => t.trim()) ?? [])
</script>

<template>
  <LoadError v-if="error || !profile" />
  <div v-else>
    <!-- Hero -->
    <section class="relative overflow-hidden">
      <div class="bg-grid pointer-events-none absolute inset-0 [mask-image:radial-gradient(ellipse_at_top,black,transparent_70%)]" />
      <div class="pointer-events-none absolute -top-40 left-1/2 h-96 w-[48rem] -translate-x-1/2 rounded-full bg-brand-500/20 blur-3xl" />

      <div class="container-page relative grid items-center gap-12 py-20 sm:py-28 lg:grid-cols-[1.2fr_1fr]">
        <div>
          <p v-if="profile.available" class="inline-flex items-center gap-2 rounded-full border border-brand-400/40 bg-brand-500/10 px-3 py-1 text-xs font-medium text-brand-700 dark:text-brand-300">
            <span class="h-2 w-2 animate-pulse rounded-full bg-brand-500" /> Disponible pour un nouveau poste
          </p>
          <h1 class="mt-6 text-4xl font-extrabold tracking-tight sm:text-6xl">
            Bonjour, je suis<br><span class="text-gradient">{{ profile.full_name }}</span>
          </h1>
          <div class="mt-5 flex flex-wrap gap-2">
            <span v-for="t in titles" :key="t" class="chip text-sm">{{ t }}</span>
          </div>
          <p class="mt-6 max-w-xl text-lg leading-relaxed">{{ profile.tagline }}</p>
          <div class="mt-8 flex flex-wrap gap-3">
            <NuxtLink to="/projets" class="btn-primary">Voir mes projets <AppIcon name="arrow" :size="16" /></NuxtLink>
            <NuxtLink to="/contact" class="btn-ghost">Me contacter</NuxtLink>
            <a v-if="profile.cv_file" :href="profile.cv_file" target="_blank" class="btn-ghost"><AppIcon name="download" :size="16" /> CV</a>
          </div>
          <p class="mt-6 flex items-center gap-2 text-sm text-slate-500"><AppIcon name="pin" :size="16" /> {{ profile.location }}</p>
        </div>

        <!-- Carte façon éditeur de code -->
        <div class="card hidden !p-0 font-mono text-sm shadow-2xl shadow-brand-500/10 lg:block">
          <div class="flex items-center gap-2 border-b border-slate-200 px-4 py-3 dark:border-slate-800">
            <span class="h-3 w-3 rounded-full bg-red-400" /><span class="h-3 w-3 rounded-full bg-amber-400" /><span class="h-3 w-3 rounded-full bg-emerald-400" />
            <span class="ml-2 text-xs text-slate-500">search_dev/ranking.py</span>
          </div>
          <pre class="overflow-x-auto p-5 leading-7"><code><span class="text-fuchsia-500">def</span> <span class="text-sky-500">hybrid_score</span>(doc, query):
    <span class="text-slate-400"># lexical + sémantique + autorité</span>
    bm25 = <span class="text-sky-500">bm25</span>(doc, query)
    sem  = <span class="text-sky-500">cosine</span>(camembert(doc), camembert(query))
    pr   = pagerank[doc.url]
    <span class="text-fuchsia-500">return</span> α*bm25 + β*sem + γ*pr

<span class="text-slate-400"># Évaluation TREC</span>
<span class="text-slate-400"># P@10=</span><span class="text-brand-500">0.75</span>  <span class="text-slate-400">R@20=</span><span class="text-brand-500">0.68</span>  <span class="text-slate-400">F1=</span><span class="text-brand-500">0.71</span></code></pre>
        </div>
      </div>
    </section>

    <!-- À propos -->
    <section id="a-propos" class="container-page scroll-mt-20 py-20">
      <SectionTitle eyebrow="à propos" title="Qui suis-je ?" />
      <div class="grid gap-10 lg:grid-cols-[2fr_1fr]">
        <div class="space-y-4 text-lg leading-relaxed">
          <p v-for="(p, i) in profile.bio.split('\n\n')" :key="i">{{ p }}</p>
        </div>
        <div class="card space-y-5">
          <div>
            <h3 class="flex items-center gap-2 font-semibold"><AppIcon name="globe" :size="18" /> Langues</h3>
            <ul class="mt-2 space-y-1 text-sm">
              <li v-for="l in data!.languages" :key="l.id"><strong class="text-slate-900 dark:text-white">{{ l.name }}</strong> — {{ l.level }}</li>
            </ul>
          </div>
          <div>
            <h3 class="flex items-center gap-2 font-semibold"><AppIcon name="award" :size="18" /> Certifications</h3>
            <ul class="mt-2 space-y-1.5 text-sm">
              <li v-for="c in data!.certifications" :key="c.id" class="flex gap-2">
                <AppIcon name="check" :size="16" class="mt-0.5 shrink-0 text-brand-500" />
                <a v-if="c.url" :href="c.url" target="_blank" rel="noopener" class="hover:underline">{{ c.name }}</a>
                <span v-else>{{ c.name }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Compétences -->
    <section id="competences" class="scroll-mt-20 bg-slate-50 py-20 dark:bg-slate-900/40">
      <div class="container-page">
        <SectionTitle eyebrow="compétences" title="Ma boîte à outils" />
        <div class="grid gap-6 md:grid-cols-2">
          <div v-for="cat in data!.skills" :key="cat.name" class="card">
            <h3 class="flex items-center gap-3 text-lg font-semibold">
              <span class="rounded-lg bg-brand-500/10 p-2 text-brand-600 dark:text-brand-400"><AppIcon :name="cat.icon" /></span>
              {{ cat.name }}
            </h3>
            <div class="mt-5 flex flex-wrap gap-2">
              <span v-for="s in cat.skills" :key="s.name" class="chip" :class="levelClass[s.level]" :title="s.level_label">{{ s.name }}</span>
            </div>
          </div>
        </div>
        <p class="mt-6 flex flex-wrap gap-4 text-xs text-slate-500">
          <span class="flex items-center gap-1.5"><span class="h-2.5 w-2.5 rounded-full bg-brand-500" /> Avancé</span>
          <span class="flex items-center gap-1.5"><span class="h-2.5 w-2.5 rounded-full bg-slate-400" /> Bon niveau</span>
          <span class="flex items-center gap-1.5"><span class="h-2.5 w-2.5 rounded-full bg-slate-400/50" /> Notions</span>
        </p>
      </div>
    </section>

    <!-- Projets phares -->
    <section class="container-page py-20">
      <div class="flex items-end justify-between gap-4">
        <SectionTitle eyebrow="projets" title="Projets phares" />
        <NuxtLink to="/projets" class="mb-10 hidden text-sm font-semibold text-brand-600 hover:underline sm:block dark:text-brand-400">Tous les projets →</NuxtLink>
      </div>
      <div class="grid gap-6 lg:grid-cols-2">
        <ProjectCard v-for="p in featured" :key="p.id" :project="p" />
      </div>
    </section>

    <!-- Expérience -->
    <section id="experience" class="scroll-mt-20 bg-slate-50 py-20 dark:bg-slate-900/40">
      <div class="container-page">
        <SectionTitle eyebrow="parcours" title="Expérience professionnelle" />
        <ol class="relative space-y-8 border-l border-slate-200 pl-8 dark:border-slate-800">
          <li v-for="exp in data!.experiences" :key="exp.id" class="relative">
            <span class="absolute -left-[41px] top-1.5 flex h-5 w-5 items-center justify-center rounded-full border-4 border-slate-50 bg-brand-500 dark:border-slate-950" />
            <div class="card">
              <div class="flex flex-col justify-between gap-1 sm:flex-row sm:items-baseline">
                <h3 class="text-lg font-bold">{{ exp.role }}</h3>
                <span class="font-mono text-xs text-slate-500">{{ exp.start }}<template v-if="exp.end"> — {{ exp.end }}</template></span>
              </div>
              <p class="mt-1 text-sm font-medium text-brand-600 dark:text-brand-400">{{ exp.company }}</p>
              <ul class="mt-4 space-y-2">
                <li v-for="h in exp.highlights" :key="h" class="flex gap-2">
                  <span class="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-slate-400" />{{ h }}
                </li>
              </ul>
              <div v-if="exp.tech.length" class="mt-4 flex flex-wrap gap-2">
                <span v-for="t in exp.tech" :key="t" class="chip">{{ t }}</span>
              </div>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <!-- Formation -->
    <section id="formation" class="container-page scroll-mt-20 py-20">
      <SectionTitle eyebrow="formation" title="Diplômes & formations" />
      <div class="grid gap-6 md:grid-cols-2">
        <div v-for="ed in data!.education" :key="ed.id" class="card flex gap-4">
          <span class="h-fit rounded-lg bg-brand-500/10 p-2 text-brand-600 dark:text-brand-400"><AppIcon name="school" /></span>
          <div>
            <h3 class="font-bold">{{ ed.degree }}</h3>
            <p class="text-sm text-slate-500">{{ ed.school }}</p>
            <p class="mt-1 font-mono text-xs text-slate-500">{{ ed.period }}</p>
            <p v-if="ed.details" class="mt-3 text-sm leading-relaxed">{{ ed.details }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="container-page pb-24">
      <div class="relative overflow-hidden rounded-3xl bg-slate-900 px-6 py-14 text-center sm:px-12 dark:bg-slate-900">
        <div class="pointer-events-none absolute inset-0 bg-gradient-to-br from-brand-500/30 via-transparent to-cyan-500/20" />
        <h2 class="relative text-3xl font-bold !text-white">Travaillons ensemble</h2>
        <p class="relative mx-auto mt-3 max-w-xl text-slate-300">
          Vous cherchez un développeur full stack, un ML engineer ou un data scientist ? Parlons de votre projet.
        </p>
        <NuxtLink to="/contact" class="btn-primary relative mt-8">Me contacter <AppIcon name="arrow" :size="16" /></NuxtLink>
      </div>
    </section>
  </div>
</template>
