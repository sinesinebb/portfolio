<script setup lang="ts">
useHead({ title: 'Contact — Yassine Bakouetila' })
const { data } = useResume()
const { public: { apiBase } } = useRuntimeConfig()

const form = reactive({ name: '', email: '', subject: '', message: '' })
const status = ref<'idle' | 'sending' | 'sent' | 'error'>('idle')
const errorMsg = ref('')

async function submit() {
  status.value = 'sending'
  try {
    await $fetch(`${apiBase}/contact/`, { method: 'POST', body: form })
    status.value = 'sent'
    Object.assign(form, { name: '', email: '', subject: '', message: '' })
  }
  catch (e: any) {
    status.value = 'error'
    errorMsg.value = e?.status === 429
      ? 'Trop de messages envoyés. Réessayez plus tard.'
      : "L'envoi a échoué. Vérifiez les champs ou écrivez-moi directement par email."
  }
}
</script>

<template>
  <section class="container-page py-16 sm:py-24">
    <SectionTitle eyebrow="contact" title="Discutons de votre projet" />
    <div class="grid gap-10 lg:grid-cols-[1fr_1.5fr]">
      <div class="space-y-6">
        <p class="text-lg leading-relaxed">
          Une offre de poste, une mission ou simplement une question ? Écrivez-moi, je réponds rapidement.
        </p>
        <ul class="space-y-4">
          <li v-if="data?.profile?.email" class="flex items-center gap-3">
            <span class="rounded-lg bg-brand-500/10 p-2 text-brand-600 dark:text-brand-400"><AppIcon name="mail" /></span>
            <a :href="`mailto:${data.profile.email}`" class="hover:text-brand-500">{{ data.profile.email }}</a>
          </li>
          <li v-if="data?.profile?.phone" class="flex items-center gap-3">
            <span class="rounded-lg bg-brand-500/10 p-2 text-brand-600 dark:text-brand-400"><AppIcon name="briefcase" /></span>
            {{ data.profile.phone }}
          </li>
          <li v-if="data?.profile?.location" class="flex items-center gap-3">
            <span class="rounded-lg bg-brand-500/10 p-2 text-brand-600 dark:text-brand-400"><AppIcon name="pin" /></span>
            {{ data.profile.location }}
          </li>
        </ul>
      </div>

      <form class="card space-y-5" @submit.prevent="submit">
        <div class="grid gap-5 sm:grid-cols-2">
          <label class="block">
            <span class="mb-1.5 block text-sm font-medium">Nom *</span>
            <input v-model="form.name" required maxlength="120" class="input" autocomplete="name">
          </label>
          <label class="block">
            <span class="mb-1.5 block text-sm font-medium">Email *</span>
            <input v-model="form.email" type="email" required class="input" autocomplete="email">
          </label>
        </div>
        <label class="block">
          <span class="mb-1.5 block text-sm font-medium">Objet</span>
          <input v-model="form.subject" maxlength="200" class="input">
        </label>
        <label class="block">
          <span class="mb-1.5 block text-sm font-medium">Message *</span>
          <textarea v-model="form.message" required rows="6" class="input resize-y" />
        </label>

        <p v-if="status === 'sent'" class="rounded-xl bg-brand-500/10 px-4 py-3 text-sm text-brand-700 dark:text-brand-300">
          Merci ! Votre message a bien été envoyé.
        </p>
        <p v-if="status === 'error'" class="rounded-xl bg-red-500/10 px-4 py-3 text-sm text-red-600 dark:text-red-400">{{ errorMsg }}</p>

        <button type="submit" class="btn-primary" :disabled="status === 'sending'">
          {{ status === 'sending' ? 'Envoi…' : 'Envoyer le message' }}
          <AppIcon name="arrow" :size="16" />
        </button>
      </form>
    </div>
  </section>
</template>
