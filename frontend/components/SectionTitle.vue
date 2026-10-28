<script setup lang="ts">
defineProps<{ eyebrow: string; title: string }>()
</script>

<template>
  <div class="mb-10">
    <p class="font-mono text-sm text-brand-600 dark:text-brand-400">// {{ eyebrow }}</p>
    <h2 class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">{{ title }}</h2>
  </div>
</template>
