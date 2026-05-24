export interface Project {
  id: number
  title: string
  description: string
  tech_stack: string[]
  github_url: string
  live_url: string
  image: string
  created_at: string
}

export interface BlogPost {
  id: number
  title: string
  slug: string
  content: string
  published: boolean
  created_at: string
}

export interface Skill {
  id: number
  name: string
  category: 'frontend' | 'backend' | 'tools'
  level: number
}

export interface ContactForm {
  name: string
  email: string
  body: string
}
