var x,y;

function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(1);
}

function draw(){
x=150;
x++;
y=sin(x);
ellipse(x,y, 5, 5);

}
