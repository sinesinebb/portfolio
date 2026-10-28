<script setup lang="ts">
const colorMode = useColorMode()
const isDark = computed(() => colorMode.value === 'dark')
function toggle() {
  colorMode.preference = isDark.value ? 'light' : 'dark'
}
</script>

<template>
  <button
    class="rounded-lg p-2 text-slate-500 transition hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white"
    :aria-label="isDark ? 'Passer en mode clair' : 'Passer en mode sombre'"
    @click="toggle"
  >
    <ClientOnly>
      <AppIcon :name="isDark ? 'sun' : 'moon'" :size="18" />
      <template #fallback><span class="block h-[18px] w-[18px]" /></template>
    </ClientOnly>
  </button>
</template>
