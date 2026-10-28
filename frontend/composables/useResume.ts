export interface Skill { name: string; level: 'advanced' | 'good' | 'basic'; level_label: string }
export interface SkillCategory { name: string; icon: string; skills: Skill[] }
export interface Metric { label: string; value: string }
export interface Project {
  id: number; title: string; slug: string; subtitle: string; period: string
  summary: string; description: string; highlights: string[]; metrics: Metric[]
  tech: string[]; repo_url: string; demo_url: string; image: string | null; featured: boolean
}
export interface Experience {
  id: number; role: string; company: string; start: string; end: string
  highlights: string[]; tech: string[]
}
export interface Profile {
  full_name: string; title: string; tagline: string; bio: string; location: string
  email: string; phone: string; github_url: string; linkedin_url: string
  avatar: string | null; cv_file: string | null; available: boolean
}
export interface Resume {
  profile: Profile | null
  skills: SkillCategory[]
  experiences: Experience[]
  projects: Project[]
  education: { id: number; degree: string; school: string; period: string; details: string }[]
  certifications: { id: number; name: string; issuer: string; url: string }[]
  languages: { id: number; name: string; level: string }[]
}

/** Récupère tout le CV en une requête, partagé entre les pages via la clé 'resume'. */
export function useResume() {
  return useFetch<Resume>(`${useApiBase()}/resume/`, { key: 'resume' })
}
