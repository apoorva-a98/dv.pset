var m=180, n=0, x,y;

function setup(){
	createCanvas(500,500);
	background(255,0,0);
	strokeWeight(1);
	ellipse(250,250, 5, 5);
	frameRate(1);
}

function draw(){
clear();
//Sun
stroke(255,255,0);
ellipse(250,250,5,5);
//Mercury
stroke(0,255,0);
x= 250+20*sin(m);
y= 250+20*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);
//Venus
x= 250+(40)*sin(m);
y= 250+(40)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);
//Earth
a= 250+(60)*sin(m);
b= 250+(60)*cos(m);
m=m+0.2;
ellipse(a, b, 5, 5);
//Earth-Moon
stroke(255,0,0);
k= a+(10)*sin(n);
l= b+(10)*cos(n);
n=n+1;
ellipse(k, l, 5, 5);
//Mars
stroke(0,255,0);
x= 250+(80)*sin(m);
y= 250+(80)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);
//Jupiter
x= 250+(100)*sin(m);
y= 250+(100)*cos(m);
m=m+0.1;
ellipse(x, y, 5, 5);
//Saturn
x= 250+(120)*sin(m);
y= 250+(120)*cos(m);
m=m+0.1;
ellipse(x, y, 3, 3);
ellipse(x, y, 7, 7);


}
