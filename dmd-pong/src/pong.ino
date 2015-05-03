namespace pong {
  int vbotVal=8;
  int vbotOld=7;
  int vbotWid=(7-1)/2;
  int ballPos[2] = {6,5};
  int ballOld[2] = {5,5};
  int ballVel[2] = {1,-1};
  int ballWid=2;
  int ballTmp[2];
  int playWid=(7-1)/2;  //Change the first number (must be odd)

  void pongReset( )
  {  
    lose();
    ballPos[1]=5;
    ballOld[0]=5;
    ballOld[1]=5;
    ballVel[0]=1;
    ballVel[1]=-1;
    dmd.drawFilledBox(32-(playOld+playWid), 0,32-(playOld-playWid), 1, GRAPHICS_NOR );
    dmd.drawFilledBox(32-(playVal+playWid), 0,32-(playVal-playWid), 1, GRAPHICS_NORMAL );
  }

  void pongLoop(){ 
      readButtons(0);
      playVal=getPosition(playOld); // Convert ping time to distance in cm and print result (0 = outside set distance range)
      ballTmp[0] = ballPos[0]+ballVel[0];
      ballTmp[1] = ballPos[1]+ballVel[1];
      if (ballTmp[0]<1 || ballTmp[0]>31){
        ballVel[0] = -1*ballVel[0];
        ballTmp[0]=ballPos[0];
      }
      if (ballTmp[1]<3){
        if (ballPos[0]>playVal+(playWid+ballWid) || ballPos[0] < playVal-(playWid+ballWid)){
          pongReset();
        }
        ballVel[1] = -1*ballVel[1];
        ballTmp[1]=ballPos[1];
      }
      if (ballTmp[1]>(DISPLAYS_DOWN*16-4)){
        if (ballPos[0]>vbotVal+(vbotWid+ballWid) || ballPos[0] < vbotVal-(vbotWid+ballWid)){
          pongReset();
        }
        ballVel[1] = -1*ballVel[1];
        ballTmp[1]=ballPos[1];
      }
      ballOld[0]=ballPos[0];
      ballOld[1]=ballPos[1];
      ballPos[0]=ballTmp[0];
      ballPos[1]=ballTmp[1];
      if (ballPos[1]>6){
        vbotOld=vbotVal;
        if (vbotVal-ballPos[0]>2){
          vbotVal-=2;
        } 
        else if (vbotVal-ballPos[0]<2){
          vbotVal+=2;
        }
      }
      if (ballPos[1]<(DISPLAYS_DOWN*16-2) && autoMode==true && ballVel[1]==-1){
        playOld=playVal;
        if (playVal-ballPos[0]>2){
          playVal-=2;
        } 
        else if (playVal-ballPos[0]<2){
          playVal+=2;
        }
      }
      dmd.drawFilledBox(31-(ballOld[0]+1), (ballOld[1]+1),31-(ballOld[0]-1), (ballOld[1]-1), GRAPHICS_NOR );
      dmd.drawFilledBox(31-(ballPos[0]+1), (ballPos[1]+1),31-(ballPos[0]-1), (ballPos[1]-1), GRAPHICS_NORMAL );
      if (playVal<30 && playVal>2 && playOld!=playVal){
        dmd.drawFilledBox(32-(playOld+playWid), 0,32-(playOld-playWid), 1, GRAPHICS_NOR );
        dmd.drawFilledBox(32-(playVal+playWid), 0,32-(playVal-playWid), 1, GRAPHICS_NORMAL );
        playOld = playVal;
      }
      if (vbotVal<30 && vbotVal>2 && vbotOld!=vbotVal){
        dmd.drawFilledBox(32-(vbotOld+vbotWid), DISPLAYS_DOWN*16-2,32-(vbotOld-vbotWid), DISPLAYS_DOWN*16-1, GRAPHICS_NOR );
        dmd.drawFilledBox(32-(vbotVal+vbotWid), DISPLAYS_DOWN*16-2,32-(vbotVal-vbotWid), DISPLAYS_DOWN*16-1, GRAPHICS_NORMAL );
      }
  }
}
void pongMain()
{ 
  using namespace pong;
  pongReset();
  while (1){ 
    pongLoop();
  }
}

