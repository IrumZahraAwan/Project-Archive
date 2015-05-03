#include "SPI.h"      
#include "DMD.h" 
#include "TimerOne.h"
#include "Arial_black_16.h"
#include "SystemFont5x7.h"
#include <NewPing.h>
#define DISPLAYS_ACROSS 1
#define DISPLAYS_DOWN 2
#define DISPLAYS_ORIENTATION 1
#define TRIGGER_PIN  2  // Arduino pin tied to trigger pin on the ultrasonic sensor.
#define ECHO_PIN     3  // Arduino pin tied to echo pin on the ultrasonic sensor.
#define MAX_DISTANCE 200 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.
#define BUTTON1 0
#define BUTTON2 23

DMD dmd(DISPLAYS_ACROSS,DISPLAYS_DOWN);
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
int noPlayer=true;
int autoMode=false;
int playVal=8;
int playOld=7;
int gameID =2;
int i,j;

void lose()
{
  if (noPlayer==true)
    autoMode=true;
  dmd.clearScreen( true );
  dmd.drawLine(11, 8*(DISPLAYS_DOWN-1)+3, 20, 8*(DISPLAYS_DOWN-1)+12, GRAPHICS_NORMAL );
  dmd.drawLine(11, 8*(DISPLAYS_DOWN-1)+12, 20, 8*(DISPLAYS_DOWN-1)+3, GRAPHICS_NORMAL );
  for (int x=0;x<1;x++)
    delay(1000);
  dmd.clearScreen( true );
  noPlayer=true;
}   

int getPosition(int playOld){
  delay(50);                      // Wait 50ms between pings (about 20 pings/sec). 29ms should be the shortest delay betwee    n pings.
  int playVal = (sonar.ping() / US_ROUNDTRIP_CM)-10; // Convert ping time to distance in cm and print result (0 = outside set distance range)
  if (playVal>29 or playVal<3){playVal=playOld;} else {noPlayer=false;autoMode=false;}
  return playVal;
}

int readButtons(int gameID){
  gameID = (gameID+1)%3;
  if(!digitalRead(BUTTON1)){
    if (gameID==0){
      pongMain();
    } else
    if (gameID==1){
      mazeMain();
    } else
    if (gameID==2){
      raceMain();
    }
  }
  /*if(!digitalRead(BUTTON2)){
    Serial.println("porque nos los dos");
    mazeMain();
  }*/
  return 1;
}

void ScanDMD(){dmd.scanDisplayBySPI();}

void setup()
{
  Timer1.initialize( 5000 );           
  Timer1.attachInterrupt( ScanDMD );  
  dmd.clearScreen( true );
  pinMode(BUTTON1, INPUT);
  pinMode(BUTTON2, INPUT);

  Serial.begin(9600);
}

void loop(){
  if (gameID==0){
    pongMain();
  } else
  if (gameID==1){
    mazeMain();
  }
  else
  if (gameID==2){
    raceMain();
  }
}
