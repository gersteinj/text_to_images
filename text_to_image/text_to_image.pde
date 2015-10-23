String lines[];
int count = 0;
boolean active = false;

//this is the height (in pixels) of the text
int sizeOfText = 60;

void setup() {
  //To set the size of the image you get, replace 300 with the width you want and replace 200 with the height you want
  size(300, 200); 

  //select a file
  selectInput("Select a word list. It should be a .txt file.", "fileSelected");

  textSize(sizeOfText);
  //Everything from here on can be left alone

  textAlign(CENTER);
  fill(0);
}

void draw() {
  if (active) {
    background(255);
    text(lines[count], width/2, height/2 + sizeOfText/2);
    saveFrame("text-####.png");
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