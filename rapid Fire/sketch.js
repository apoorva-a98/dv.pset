var x=0,y=0;
var up=1,right=0;
var a,b,c,d;
function setup(){
	createCanvas(600, 600);
	frameRate(36);
	strokeWeight(5);
	background(0,0,0);
}

function draw(){
	translate(width/2,height/2);
	point(x,y);
	stroke(255,255,255);
	if (y<10-height/2){
		x=x+5;
		if (x<10-width/2){
			y=y-5;
			x=290;
		}
	}

	else{
		y=y-5;

	}

/*
	if up==1{
		y=y+1;
	}
	if up==0{
		y=y-1;
	}
	if right==1{
		x=x+1;
	}
	if right==0{
		x=x-1
	}
*/
}
