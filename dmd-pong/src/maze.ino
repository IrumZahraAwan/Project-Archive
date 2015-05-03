namespace maze {
  int listWid=(13-1)/2;
  int playWid=(5-1)/2;  //Change the first number (must be odd)
  int list[3]={10, 6, 20};
  int listGap=12;
  int listHeight=listGap;
  int everyTwo=0;
  int autoPos=16;
  int autoOld=16;

  void mazeReset()
  {
    listHeight=listGap;
    lose();
    autoPos=16;
    dmd.drawFilledBox(32-(autoPos+playWid), 0,32-(autoPos-playWid), 1, GRAPHICS_NORMAL );
  }
  void mazeLoop(){
    readButtons(1);
    everyTwo=(everyTwo+1)%2;
    playVal = getPosition(playOld);
    if (playVal<30 && playVal>2 && playVal!=playOld){
      autoOld=autoPos;
      autoPos=playVal;
    }
    if (autoMode && autoPos!=list[0]){
      autoOld=autoPos;
      //autoPos=(autoPos-list[0])/abs(autoPos-list[0]);
      if (list[0]>autoPos){autoPos=autoPos+1;}
      else {autoPos=autoPos-1;};
    }
    if (everyTwo==1){
      for (i=0;i<3;i++){
        dmd.drawFilledBox(32-(list[i]-(listWid)), listHeight+i*listGap+1,32, listHeight+i*listGap+2, GRAPHICS_NOR );
        dmd.drawFilledBox(0, listHeight+i*listGap+1,32-(list[i]+(listWid)), listHeight+i*listGap+2, GRAPHICS_NOR );
        dmd.drawFilledBox(32-(list[i]-(listWid)), listHeight+i*listGap,32, listHeight+i*listGap+1, GRAPHICS_NORMAL );
        dmd.drawFilledBox(0, listHeight+i*listGap,32-(list[i]+(listWid)), listHeight+i*listGap+1, GRAPHICS_NORMAL );
      }
      if (listHeight<-2){
          for (i=0;i<3-1;i++){
            list[i] = list[i+1];
          }
          list[2]=random(4,28);
          listHeight=listGap-2;
        }
        listHeight-=1;
        
    }
    if (autoOld!=autoPos){
      dmd.drawFilledBox(32-(autoOld+playWid), 0,32-(autoOld-playWid), 1, GRAPHICS_NOR );
      dmd.drawFilledBox(32-(autoPos+playWid), 0,32-(autoPos-playWid), 1, GRAPHICS_NORMAL );
      playOld = playVal;
    }
    if (listHeight<2 && listHeight>-1){
      if ( (list[0]+listWid-4) < (autoPos-playWid) || (list[0]-listWid+4) > (autoPos+playWid) )
      {
        mazeReset();
      }
    }
  }
  
  
  
}

void mazeMain()
{
  using namespace maze;
  mazeReset();
  while (1){
    mazeLoop();
  }
}
