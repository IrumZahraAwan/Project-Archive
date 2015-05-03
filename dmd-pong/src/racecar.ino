namespace race {
  int listWid=(19-1)/2;
  int playWid=(5-1)/2;  //Change the first number (must be odd)
  int list[32];
  int everyTwo=0;
  int autoPos=16;
  int autoOld=16;
  int genDirection = -1;
  int old=16;

  int nextCenter(int previousCenter){
    float r = random(0,101)/100.0;
    Serial.println(' ');
    if (  r < ( 15 - min ( abs(previousCenter - listWid), abs(31-listWid - previousCenter)) ) / 15 )
      genDirection*=-1;
    Serial.println(r);
    int newRet = genDirection;
    if(r<0.3){
      newRet =  previousCenter-genDirection;
    } 
    else {
      newRet = previousCenter+genDirection;
    }

    return min( max( newRet, listWid ) , 31-listWid );
  }

  void raceReset()
  {
    lose();
    autoPos=16;
    dmd.drawFilledBox(32-(autoPos+playWid), 0,32-(autoPos-playWid), 1, GRAPHICS_NORMAL );
    list[0]=16;
    for (i=1;i<32;i++){
      list[i]=nextCenter(list[i-1]);
    }
  }
  void raceLoop(){
    readButtons(2);
    everyTwo=(everyTwo+1)%2;
    playVal = getPosition(playOld);
    if (playVal<30 && playVal>2 && playVal!=playOld){
      autoOld=autoPos;
      autoPos=playVal;
    }
    if (autoMode && autoPos!=list[0]){
      autoOld=autoPos;
      //autoPos=(autoPos-list[0])/abs(autoPos-list[0]);
      if (list[0]>autoPos){
        autoPos=autoPos+1;
      }
      else {
        autoPos=autoPos-1;
      };
    }
    if (everyTwo==1){
      i=-1;
      dmd.drawFilledBox(32-(old-(listWid)), i+1,32, i+2, GRAPHICS_NOR );
        dmd.drawFilledBox(0, i+1,32-(old+(listWid)), i+2, GRAPHICS_NOR );
      for (i=0;i<32;i++){
        dmd.drawFilledBox(32-(list[i]-(listWid)), i+1,32, i+2, GRAPHICS_NOR );
        dmd.drawFilledBox(0, i+1,32-(list[i]+(listWid)), i+2, GRAPHICS_NOR );
        dmd.drawFilledBox(32-(list[i]-(listWid)), i,32, i+1, GRAPHICS_NORMAL );
        dmd.drawFilledBox(0, i,32-(list[i]+(listWid)), i+1, GRAPHICS_NORMAL );
      }
      old=list[0];
      for (i=0;i<32-1;i++){
        list[i] = list[i+1];
      }
      list[31]=nextCenter(list[30]);

    }
    if (autoOld!=autoPos){
      dmd.drawFilledBox(32-(autoOld+playWid), 0,32-(autoOld-playWid), 1, GRAPHICS_NOR );
      dmd.drawFilledBox(32-(autoPos+playWid), 0,32-(autoPos-playWid), 1, GRAPHICS_NORMAL );
      playOld = playVal;
    }

    if ( (list[0]+listWid-4) < (autoPos-playWid) || (list[0]-listWid+4) > (autoPos+playWid) )
    {
      raceReset();
    }
  }



}

void raceMain()
{
  using namespace race;
  raceReset();
  while (1){
    raceLoop();
  }
}

