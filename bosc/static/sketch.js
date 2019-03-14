
var ws = null;

function setup() {
    createCanvas(window.innerWidth, window.innerHeight);

    ws = new WebSocket("ws://localhost:8080/websocket");
    ws.onopen = function() {
      ws.send("Hello, world");
      console.log('sent')
    };
    ws.onmessage = function (evt) {
      alert(evt.data);
    };
    console.log('ws');
}

function draw() {
    ellipse(50, 50, 80, 80);
}

function mouseMoved() {
  ellipse(mouseX, mouseY, 5, 5);
  ws.send(JSON.stringify(['mouseevent', mouseX, mouseY]));
  // prevent default
  return false;
}
