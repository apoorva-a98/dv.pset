var m=250, n=0,r=20, s=40, x,y;

function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(1);
}

function draw(){
x= 150+s*sin(m);
y= 150+r*cos(m)*sin(m);
m=m+0.1;
ellipse(x, y, 5, 5);

}
