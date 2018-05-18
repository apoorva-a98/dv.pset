var x=0, y=150, z=300, n=0;

function setup(){
	createCanvas(300, 300);
	background(255,0,0);
	strokeWeight(5);
}

function draw(){
  background(255,0,0);
  stroke(255);
  if (x<300 && n==0) {
    x++;
    ellipse(x, y, 5, 5);
  } else{
    n=1;
  }

  if (x>0 && n==1) {
    x--;
    ellipse(x, y, 5, 5);
  }
  else{
    n=0;
  }
}
