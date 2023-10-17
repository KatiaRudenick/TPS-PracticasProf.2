const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const path = require('path');

// Inicializaciones
const app = express();
const server = http.createServer(app);
const io = socketIO(server);

//Configuraciones
app.set('port', process.env.PORT || 3000);

//Sockets
require('./sockets')(io);

//Sirve archivos estaticos (html,css,js, img, etc) añ cliente a traves de http
//Crea una ruta completa al directorio 'public' en el directorio actual 
app.use(express.static(path.join(__dirname, 'public')));

//Inicia servidor
server.listen(app.get('port'), () => {
  console.log('Server on port', app.get('port'));
});