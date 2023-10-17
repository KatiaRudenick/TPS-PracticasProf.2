function init() {
  // Inicialización de variables para rastrear las interacciones del mouse.
  console.log("DOMContentLoaded event fired");
  let mouse = {
    click: false,
    move: false,
    pos: { x: 0, y: 0},
    pos_prev: false
  };

   // Variables para controlar el color del lapiz y el tamaño del trazo.
  var color = "#000000";
  var size = 5;
  // Modo predeterminado: lapiz
  let drawingMode = 'pencil-button'; 
  
  // Canvas
  let canvas = document.getElementById('drawing');
  let context = canvas.getContext('2d');
  let width = window.innerWidth;
  let height = window.innerHeight;
  
  // Socket IO
  let socket = io();

  canvas.width = width;
  canvas.height = height;

  canvas.addEventListener('mousedown', (e) => {
    mouse.click = true;
  });

  canvas.addEventListener('mouseup', (e) => {
    mouse.click = false;
  });

  canvas.addEventListener('mousemove', e => {
    mouse.pos.x = e.clientX / width;
    mouse.pos.y = e.clientY / height;
    mouse.move = true;
  });

  function drawBlue() {
    color = "#0A26F2";
  }
  
  function drawPlum() {
    color = "#C84EE4";
  }
  
  function drawPink() {
    color = "#F662CD";
  }
  
  function drawRed() {
    color = "#F2140C";
  }
  
  function drawYellow() {
    color = "#F6F320";
  }
  
  function drawOrange() {
    color = "#FC9012";
  }

  function drawGreen() {
    color = "#7ADB13";
  }

  function drawWhite() {
    color = "#FFFFFF";
  }
  
  function drawBlack() {
    color = "#000000";
  }

  var pinkColor = document.getElementById("pink-color");
  var blueColor = document.getElementById("blue-color");
  var redColor = document.getElementById("red-color");
  var plumColor = document.getElementById("plum-color");
  var yellowColor = document.getElementById("yellow-color");
  var orangeColor = document.getElementById("orange-color");
  var greenColor = document.getElementById("green-color");
  var whiteColor = document.getElementById("white-color");
  var blackColor = document.getElementById("black-color");
  var penSizeRange = document.getElementById("pen-size");
  penSizeRange.addEventListener("input", function () {
    size = parseInt(this.value);
  }); 

  pinkColor.addEventListener("click", drawPink);
  blueColor.addEventListener("click", drawBlue);
  plumColor.addEventListener("click", drawPlum);
  redColor.addEventListener("click", drawRed);
  yellowColor.addEventListener("click", drawYellow);
  orangeColor.addEventListener("click", drawOrange);
  greenColor.addEventListener("click", drawGreen);
  whiteColor.addEventListener("click", drawWhite);
  blackColor.addEventListener("click", drawBlack);

  // Función para ajustar el tamaño del lienzo (canvas)
  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
resizeCanvas();

  socket.on('draw_line', data => {
    let line = data.line;
    context.beginPath();
    context.lineWidth = size;
    context.strokeStyle = color;
    context.lineCap = "round";
    context.globalCompositeOperation = drawingMode === 'eraser' ? 'destination-out' : 'source-over';
    context.moveTo(line[0].x * width, line[0].y * height);
    context.lineTo(line[1].x * width, line[1].y * height);
    context.stroke();
  });

  // Agregar oyentes de clic a los botones
document.getElementById('pencil-button').addEventListener('click', () => {
  drawingMode = 'pencil';
});

document.getElementById('eraser-button').addEventListener('click', () => {
    drawingMode = 'eraser';
  });

  function mainLoop() {
    if(mouse.click && mouse.move && mouse.pos_prev) {
      socket.emit('draw_line', { line: [mouse.pos, mouse.pos_prev], 
        erase:drawingMode=== 'eraser' });
      mouse.move = false;
    }
    mouse.pos_prev = { x: mouse.pos.x, y: mouse.pos.y };
    setTimeout(mainLoop, 25);
  }
  mainLoop();
}
document.addEventListener('DOMContentLoaded', init);