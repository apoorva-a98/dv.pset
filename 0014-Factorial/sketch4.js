var n=0, input, x=1,i=0,flag=0;

function setup(){
  createCanvas(300, 300);
  background(255,255,255);
  stroke(0);
  strokeWeight(5);

  input=createInput();
  input.position(20,65);

  greeting = createElement('h5', 'enter a no. for creating factorial');
  greeting.position(20, 5);
  button = createButton('submit');
  button.position(20, 85);
  button.mousePressed(update);
  //if(flag>0){
     
  //}
}

function update(){
  n=input.value();
  flag=1;
  factorial(); 
}

function factorial(){
  for(i=n; i>0; i--){
    x=x*i;
}
print(x);
}

function draw(){}
