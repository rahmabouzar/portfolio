import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api',
})

export const getProjects  = () => api.get('/projects/').then(r => r.data)
export const getBlogPosts = () => api.get('/blog/').then(r => r.data)
export const getSkills    = () => api.get('/skills/').then(r => r.data)
// Define ContactForm type used by sendMessage
export type ContactForm = {
  name: string
  email: string
  message: string
  [key: string]: any
}

export const sendMessage  = (data: ContactForm) => api.post('/contact/', data)