/** URL de l'API : en SSR on peut passer par le réseau interne (ex. Docker), côté navigateur par l'URL publique. */
export function useApiBase() {
  const config = useRuntimeConfig()
  return (import.meta.server && config.apiBaseServer) || config.public.apiBase
}
