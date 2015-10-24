//Create array to store word list
String lines[];
//Index variable
int count = 0;
//Determines whether program is running
boolean active = false;

//Declare PGraphic object 
PGraphics graphic;

//Height of text in pixels
int sizeOfText = 60;

//Size of image output
int graphicW = 300;
int graphicH = 200;

void setup() {
  //size of canvas is not currently relevant
  //size(displayWidth, displayHeight); 

  //Select a file from dialog box
  selectInput("Select a word list. It should be a .txt file.", "fileSelected");

  //initialize the PGraphic object
  graphic = createGraphics(graphicW, graphicH);
}

void draw() {
  //Don't run until a file is selected
  if (active) {
    //start PGraphic
    graphic.beginDraw();

    //drawing settings
    graphic.background(255);
    graphic.fill(0);
    graphic.textSize(sizeOfText);
    graphic.textAlign(CENTER);

    //draw one of the words
    graphic.text(lines[count], graphicW/2, graphicH/2 + sizeOfText/2);

    //end PGraphic
    graphic.endDraw();

    //save the image
    graphic.save("text"+count+".png");

    //increase index
    count++;

    //exit when done
    if (count >= lines.length) {
      exit();
    }
  }
}

//works with file selection
void fileSelected(File selection) {
  //Gives an error if no file is chosen
  if (selection == null) {
    println("No file chosen");
  } else {
    //if a file is chosen, load the word list into the array
    lines = loadStrings("wordlist.txt");
    //set active to true so the main program can run
    active = true;
  }
}