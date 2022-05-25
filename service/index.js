// Require the framework and instantiate it
const fastify = require('fastify')({ logger: true })
const {spawn} = require('child_process');


fastify.register(require('fastify-cors'), {
  origin: '*',
  methods: ['GET'],
});


 fastify.get('/weather', (request, reply) => {

   const python = spawn('python', ['../script/script.py', '41.28,36.34']);
    
    python.stdout.on ('data', data => {
      const latin1String = data.toString("latin1");   
      dataToSend=  JSON.parse(latin1String)
      console.log(dataToSend)
      reply.type('application/json').code(200)
      reply.send(dataToSend)
     
      
    })
    python.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });
   
   });



  fastify.post('/data', (request, reply) => {
   //reply.send(request.body)
   const python = spawn('python', ['../script/script.py', String(request.body.cityName)]);
    
   python.stdout.on ('data', data => {
     const latin1String = data.toString("latin1");   
     dataToSend=  JSON.parse(latin1String)
     console.log(dataToSend)
     reply.type('application/json').code(200)
     reply.send(dataToSend)
    
     
   })
   python.stderr.on('data', (data) => {
     console.error(`stderr: ${data}`);
   });
  
     

     
    });


  
   
   
   
    

  
// Run the server!
fastify.listen(3000, (err, address) => {
    if (err) throw err
    // Server is now listening on ${address}
  })