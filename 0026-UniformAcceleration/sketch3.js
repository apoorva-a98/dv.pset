var x=0, y=0, n=0, m=0, v=60.0, u=1.0;

function setup(){
  createCanvas(300, 300);
  background(255,0,0);
  stroke(255);
  strokeWeight(5);
}

function draw(){
background(255,0,0);
if(v>u){
  if(y<300 && m==0){
    y=y+v*sin(PI/3);
      if (x<300 && n==0) {
        x=x+v*cos(PI/3);
        ellipse(x, y, 5, 5);
      } else{
        n=1;
      }

      if (x>0 && n==1) {
        x=x-v*cos(PI/3);
        ellipse(x, y, 5, 5);
      } else{
        n=0;
      }
    } else {
      m=1;
    }


    if(y>0 && m==1){
      y=y-v*sin(PI/3);
        if (x<300 && n==0) {
          x=x+v*cos(PI/3);
          ellipse(x, y, 5, 5);
        } else{
          n=1;
        }

        if (x>0 && n==1) {
          x=x-v*cos(PI/3);
          ellipse(x, y, 5, 5);
        } else{
          n=0;
        }
      } else {
        m=0;
      }
        v=v-0.25;
    }
  else{
    if(y<300 && m==0){
      y=y+sin(PI/3);
        if (x<300 && n==0) {
          x=x+cos(PI/3);
          ellipse(x, y, 5, 5);
        } else{
          n=1;
        }

        if (x>0 && n==1) {
          x=x-cos(PI/3);
          ellipse(x, y, 5, 5);
        } else{
          n=0;
        }
      } else {
        m=1;
      }

      if(y>0 && m==1){
        y=y-sin(PI/3);
          if (x<300 && n==0) {
            x=x+cos(PI/3);
            ellipse(x, y, 5, 5);
          } else{
            n=1;
          }

          if (x>0 && n==1) {
            x=x-cos(PI/3);
            ellipse(x, y, 5, 5);
          } else{
            n=0;
          }
        } else {
          m=0;
        }
  }
}
