
var ws = null;

function setup () {
  createCanvas(window.innerWidth, window.innerHeight);
  ws = new WebSocket("ws://localhost:8080/websocket");
  ws.onopen = function() {
      ws.send("Hello, world");
      console.log('sent')
      };
  ws.onmessage = function (evt) {
      alert(evt.data);
  };
  console.log('ws')
}

function draw () {
  circle(100, 100, 100);
}

function mouseMoved () {
  circle(mouseX, mouseY, 5);
}
