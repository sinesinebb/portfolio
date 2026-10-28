<script setup lang="ts">
import type { NuxtError } from '#app'
defineProps<{ error: NuxtError }>()
</script>

<template>
  <NuxtLayout>
    <div class="container-page py-32 text-center">
      <p class="font-mono text-6xl font-bold text-brand-500">{{ error.statusCode }}</p>
      <h1 class="mt-4 text-2xl font-bold">{{ error.statusCode === 404 ? 'Page introuvable' : 'Une erreur est survenue' }}</h1>
      <button class="btn-primary mt-8" @click="clearError({ redirect: '/' })">Retour à l'accueil</button>
    </div>
  </NuxtLayout>
</template>
