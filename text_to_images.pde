String lines[];
int count = 0;

//this is the height (in pixels) of the text
int sizeOfText = 60;

void setup() {
  //To set the size of the image you get, replace 300 with the width you want and replace 200 with the height you want
  size(300, 200); 

  textSize(sizeOfText);
  //Everything from here on can be left alone
  lines = loadStrings("wordlist.txt");
  textAlign(CENTER);
  fill(0);
}

void draw() {
  background(255);
  text(lines[count], width/2, height/2 + sizeOfText/2);
  saveFrame("text-###");
  count++;
  if (count >= lines.length) {
    exit();
  }
}