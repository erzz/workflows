const restify = require('restify');

const PORT = 8888;
const app = restify.createServer();
app.get('/', (req, res) => res.send({ hello: 'World' }));
app.listen(PORT);
