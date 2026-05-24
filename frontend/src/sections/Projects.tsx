import { useQuery } from '@tanstack/react-query'
import { getProjects } from '../services/api'
import type { Project } from '../types'

export default function Projects() {
  const { data, isLoading, isError } = useQuery<Project[]>({
    queryKey: ['projects'],
    queryFn: getProjects,
  })

  if (isLoading) return <p className="text-center">Loading...</p>
  if (isError)   return <p className="text-center text-red-500">Error loading projects</p>

  return (
    <section id="projects" className="py-20 px-6">
      <h2 className="text-3xl font-bold text-center mb-10">Projects</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {data?.map(project => (
          <div key={project.id} className="border rounded-xl p-5 shadow hover:shadow-lg transition">
            <h3 className="text-xl font-semibold mb-2">{project.title}</h3>
            <p className="text-gray-500 mb-4">{project.description}</p>
            <div className="flex flex-wrap gap-2 mb-4">
              {project.tech_stack.map(tech => (
                <span key={tech} className="bg-purple-100 text-purple-700 text-sm px-2 py-1 rounded">
                  {tech}
                </span>
              ))}
            </div>
            <div className="flex gap-4">
              {project.github_url && <a href={project.github_url} target="_blank" className="text-sm underline">GitHub</a>}
              {project.live_url   && <a href={project.live_url}   target="_blank" className="text-sm underline">Live</a>}
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}