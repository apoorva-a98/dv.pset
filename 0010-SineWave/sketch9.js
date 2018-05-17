var PI=22/7;
var x=0,y;
var a=PI/16,f=5;

function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(1);
}

function draw(){
x++;
y=150+sin(a*PI/6)*50;
a++;
ellipse(x*10,y, 5, 5);
}
