import Fastify from 'fastify'

const fastify = Fastify({
  logger: true
})

fastify.get('/', async (request, reply) => {
  const data = {
    message: 'Hello from TypeScript Fastify!',
    timestamp: new Date().toISOString()
  }

  try {
    const response = await fetch('http://localhost:5000/receive', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const result = await response.json()
    return { sent: data, received: result }
  } catch (error) {
    console.error('Error:', error)
    reply.status(500).send({ error: 'Failed to send data to Python server' })
  }
})

const start = async () => {
  try {
    await fastify.listen({ port: 3000 })
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}

start()
