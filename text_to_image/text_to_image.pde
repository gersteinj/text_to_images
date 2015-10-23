String lines[];
int count = 0;
boolean active = false;

PGraphics graphic;

//this is the height (in pixels) of the text
int sizeOfText = 60;

//this is the size of the image output
int graphicW = 300;
int graphicH = 200;

void setup() {
  //To set the size of the image you get, replace 300 with the width you want and replace 200 with the height you want
  size(displayWidth, displayHeight); 

  //select a file
  selectInput("Select a word list. It should be a .txt file.", "fileSelected");

  graphic = createGraphics(graphicW, graphicH);
}

void draw() {
  if (active) {
    graphic.beginDraw();
    graphic.background(255);
    graphic.fill(0);
    graphic.textSize(sizeOfText);
    graphic.textAlign(CENTER);
    graphic.text(lines[count], graphicW/2, graphicH/2 + sizeOfText/2);
    //saveFrame("text-####.png");
    graphic.endDraw();
    graphic.save("text"+count+".png");
    count++;
    if (count >= lines.length) {
      exit();
    }
  }
}

void fileSelected(File selection) {
  if (selection == null) {
    println("No file chosen");
  } else {
    lines = loadStrings("wordlist.txt");
    active = true;
  }
}