///////////////////////////////////////////////////
//                                               //
// Text to Images created by Jacqueline Gerstein //
//   GersteinJ@gmail.com            @gersteinj   //
//                                               //
///////////////////////////////////////////////////


//Change values to change settings

//Replace "text" with whatever you want the name of the files to be
//Make sure your filename is in quotes
//Files will be named in the following format: name + number + .png
String fileName = "text";

//Height of text in pixels
int sizeOfText = 60;

//Size of image output
int graphicW = 300;
int graphicH = 200;

//Colors of text and background, given as (red, green, blue). Default is black text on white background
color textColor = color(0, 0, 0);
color bgColor = color(255, 255, 255);


//Create array to store word list
String lines[];
//Index variable
int count = 0;
//Determines whether program is running
boolean active = false;

//Declare PGraphic object 
PGraphics graphic;




void setup() {
  size(800, 600);

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
    graphic.background(bgColor);
    graphic.fill(textColor);
    graphic.textSize(sizeOfText);
    graphic.textAlign(CENTER);

    //draw one of the words
    graphic.text(lines[count], graphicW/2, graphicH/2 + sizeOfText/2);

    //end PGraphic
    graphic.endDraw();

    //save the image
    graphic.save(fileName+nf(count, 4)+".png");

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
    String file = selection.getAbsolutePath();
    lines = loadStrings(file);
    //set active to true so the main program can run
    active = true;
  }
}