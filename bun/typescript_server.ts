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
    console.log('Sending request to Python server...')
    const response = await fetch('http://localhost:5000/receive', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })

    console.log(`Response status: ${response.status}`)
    console.log(`Response headers: ${JSON.stringify(response.headers)}`)

    if (!response.ok) {
      const errorText = await response.text()
      throw new Error(`HTTP error! status: ${response.status}, body: ${errorText}`)
    }

    const result = await response.json()
    console.log('Received response:', result)
    return { sent: data, received: result }
  } catch (error) {
    console.error('Error:', error)
    reply.status(500).send({ error: 'Failed to send data to Python server', details: error.message })
  }
})

const start = async () => {
  try {
    await fastify.listen({ port: 3000 })
    console.log('Server listening on port 3000')
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}

start()
