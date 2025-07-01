import math

class Main:
    def __init__(self, entry_column=None, magic_number=0.5):
        self.current_line_char_count = 0
        self.entry_column = entry_column  # 1-indexed, or None
        self.magic_number = magic_number  # Used for deterministic "random"
        self._maze_lines = []  # Buffer for maze output

    def print_expr(self, expression):
        if isinstance(expression, (int, float)):
            text = f"{expression:.2f}".rstrip('0').rstrip('.')
        else:
            text = expression
        # Instead of printing, append to buffer
        if not self._maze_lines:
            self._maze_lines.append("")
        self._maze_lines[-1] += text
        self.current_line_char_count += len(text)

    def println(self):
        # Instead of printing, append a new line to buffer
        self._maze_lines.append("")
        self.current_line_char_count = 0

    def tab(self, num_spaces):
        return ' ' * round(num_spaces - self.current_line_char_count)

    def as_int(self, variable):
        return round(variable)

    def round_down_to_int(self, variable):
        return math.floor(variable)

    def random(self, positive_int):
        # Use the magic_number instead of a fixed 0.5
        return self.magic_number

    def mid(self, text, starting_index, num_chars):
        return text[self.as_int(starting_index - 1):self.as_int(starting_index + num_chars - 1)]

    def generate_maze(self):
        """
        Runs the maze generation logic and returns the maze as a string.
        """
        self._maze_lines = []
        self.current_line_char_count = 0
        self._run_maze_logic()
        # Remove any leading empty lines
        while self._maze_lines and self._maze_lines[0] == "":
            self._maze_lines.pop(0)
        # Remove any trailing empty lines
        while self._maze_lines and self._maze_lines[-1] == "":
            self._maze_lines.pop()
        return "\n".join(self._maze_lines)

    def _run_maze_logic(self):
        """
        The original run() logic, but all output is captured in self._maze_lines.
        """
        label = 10

        scalarC = 0
        scalarH = 0
        scalarI = 0
        scalarJ = 0
        scalarQ = 0
        scalarR = 0
        scalarS = 0
        scalarV = 0
        scalarX = 0
        scalarZ = 0
        matrixV = []
        matrixW = []
        loopActive165 = False
        loopActive1017 = False
        loopActive1043 = False
        loopActive1015 = False

        iterations = 0

        while True:
            iterations += 1
            if iterations > 99999:
                self.print_expr("INFINITE LOOP DETECTED. STOPPING EXECUTION.")
                self.println()
                break

            if loopActive165 and label > 180:
                loopActive165 = False;
            if loopActive1017 and label > 1040:
                loopActive1017 = False;
            if loopActive1043 and label > 1070:
                loopActive1043 = False;
            if loopActive1015 and label > 1072:
                loopActive1015 = False;

            match label:
                #10PRINTTAB(28);"AMAZINGPROGRAM"
                case 10:
                    label = 20
                    self.print_expr(self.tab(28))
                    self.print_expr("AMAZING PROGRAM")
                    self.println()
                
                #20PRINTTAB(15);"CREATIVECOMPUTINGMORRISTOWN,NEWJERSEY"
                case 20:
                    label = 30
                    self.print_expr(self.tab(15))
                    self.print_expr("CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
                    self.println()
                
                #30PRINT:PRINT:PRINT:PRINT
                case 30:
                    label = 100
                    self.println()
                    self.println()
                    self.println()
                    self.println()
                
                #100INPUT"WHATAREYOURWIDTHANDLENGTH";H,V
                case 100:
                    label = 102
                    self.print_expr("WHAT ARE YOUR WIDTH AND LENGTH")
                    self.println()
                    scalarH = float(input())
                    scalarV = float(input())
                    # Read entry column if provided (optional third input)
                    try:
                        entry_col = input()
                        if entry_col.strip() != "":
                            self.entry_column = int(entry_col)
                        # Try to read magic_number (optional fourth input)
                        magic_number_input = input()
                        if magic_number_input.strip() != "":
                            self.magic_number = float(magic_number_input)
                    except EOFError:
                        pass

                #102IFH<>1ANDV<>1THEN110
                case 102:
                    label = 104
                    if (scalarH != 1) and (scalarV != 1):
                        label = 110
                
                #104PRINT"MEANINGLESSDIMENSIONS.TRYAGAIN.":GOTO100
                case 104:
                    label = 110
                    self.print_expr("MEANINGLESS DIMENSIONS.  TRY AGAIN.")
                    self.println()
                    label = 100
                
                #110DIMW(H,V),V(H,V)
                case 110:
                    label = 120
                    matrixW = [[0] * (self.as_int(scalarV) + 1) for _ in range(self.as_int(scalarH) + 1)]
                    matrixV = [[0] * (self.as_int(scalarV) + 1) for _ in range(self.as_int(scalarH) + 1)]
                
                #120PRINT
                case 120:
                    label = 130
                    self.println()
                
                #130PRINT
                case 130:
                    label = 140
                    self.println()
                
                #140PRINT
                case 140:
                    label = 150
                    self.println()
                
                #150PRINT
                case 150:
                    label = 160
                    self.println()
                
                #160Q=0:Z=0:X=INT(RND(1)*H+1)
                case 160:
                    label = 165
                    scalarQ = 0
                    scalarZ = 0
                    # If entry_column is specified, use it (1-indexed), else legacy random
                    if self.entry_column is not None:
                        scalarX = int(self.entry_column)
                    else:
                        scalarX = self.round_down_to_int(self.random(1)*scalarH+1) #Exit location.
                
                #165FORI=1TOH
                case 165:
                    label = 170
                    if loopActive165 == False:
                        scalarI = 1
                        loopActive165 = True
                    if (scalarI - scalarH) * 1 > 0: # reached the last column 
                        label = 190
                
                #170IFI=XTHEN173
                case 170:
                    label = 171
                    if (scalarI == scalarX): # if I=X draw the exit
                        label = 173
                
                #171PRINT".--";:GOTO180
                case 171:
                    label = 173
                    self.print_expr(".--")
                    label = 180
                
                #173PRINT".";
                case 173:
                    label = 180
                    self.print_expr(".  ") # draw the exit
                
                #180NEXTI
                case 180:
                    label = 190
                    scalarI = scalarI + 1
                    label = 165
                
                #190PRINT"."
                case 190:
                    label = 195
                    self.print_expr(".") # draw the right wall
                    self.println() # move to the next line
                
                #195C=1:W(X,1)=C:C=C+1
                case 195:
                    label = 200
                    scalarC = 1
                    matrixW[self.as_int(scalarX)][self.as_int(1)] = scalarC
                    scalarC = scalarC+1
                
                #200R=X:S=1:GOTO260
                case 200:
                    label = 210
                    scalarR = scalarX
                    scalarS = 1
                    label = 260
                
                #210IFR<>HTHEN240
                case 210:
                    label = 215
                    if (scalarR != scalarH):
                        label = 240
                
                #215IFS<>VTHEN230
                case 215:
                    label = 220
                    if (scalarS != scalarV):
                        label = 230
                
                #220R=1:S=1:GOTO250
                case 220:
                    label = 230
                    scalarR = 1
                    scalarS = 1
                    label = 250
                
                #230R=1:S=S+1:GOTO250
                case 230:
                    label = 240
                    scalarR = 1
                    scalarS = scalarS+1
                    label = 250
                
                #240R=R+1
                case 240:
                    label = 250
                    scalarR = scalarR+1
                
                #250IFW(R,S)=0THEN210
                case 250:
                    label = 260
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS)] == 0):
                        label = 210
                
                #260IFR-1=0THEN530
                case 260:
                    label = 265
                    if (scalarR-1 == 0):
                        label = 530
                
                #265IFW(R-1,S)<>0THEN530
                case 265:
                    label = 270
                    if (matrixW[self.as_int(scalarR-1)][self.as_int(scalarS)] != 0):
                        label = 530
                
                #270IFS-1=0THEN390
                case 270:
                    label = 280
                    if (scalarS-1 == 0):
                        label = 390
                
                #280IFW(R,S-1)<>0THEN390
                case 280:
                    label = 290
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS-1)] != 0):
                        label = 390
                
                #290IFR=HTHEN330
                case 290:
                    label = 300
                    if (scalarR == scalarH):
                        label = 330
                
                #300IFW(R+1,S)<>0THEN330
                case 300:
                    label = 310
                    if (matrixW[self.as_int(scalarR+1)][self.as_int(scalarS)] != 0):
                        label = 330
                
                #310X=INT(RND(1)*3+1)
                case 310:
                    label = 320
                    scalarX = self.round_down_to_int(self.random(1)*3+1)
                
                #320ONXGOTO790,820,860
                case 320:
                    label = 330
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 820
                    if self.as_int(scalarX) == 3:
                        label = 860
                
                #330IFS<>VTHEN340
                case 330:
                    label = 334
                    if (scalarS != scalarV):
                        label = 340
                
                #334IFZ=1THEN370
                case 334:
                    label = 338
                    if (scalarZ == 1):
                        label = 370
                
                #338Q=1:GOTO350
                case 338:
                    label = 340
                    scalarQ = 1
                    label = 350
                
                #340IFW(R,S+1)<>0THEN370
                case 340:
                    label = 350
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 370
                
                #350X=INT(RND(1)*3+1)
                case 350:
                    label = 360
                    scalarX = self.round_down_to_int(self.random(1)*3+1)
                
                #360ONXGOTO790,820,910
                case 360:
                    label = 370
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 820
                    if self.as_int(scalarX) == 3:
                        label = 910
                
                #370X=INT(RND(1)*2+1)
                case 370:
                    label = 380
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #380ONXGOTO790,820
                case 380:
                    label = 390
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 820
                
                #390IFR=HTHEN470
                case 390:
                    label = 400
                    if (scalarR == scalarH):
                        label = 470
                
                #400IFW(R+1,S)<>0THEN470
                case 400:
                    label = 405
                    if (matrixW[self.as_int(scalarR+1)][self.as_int(scalarS)] != 0):
                        label = 470
                
                #405IFS<>VTHEN420
                case 405:
                    label = 410
                    if (scalarS != scalarV):
                        label = 420
                
                #410IFZ=1THEN450
                case 410:
                    label = 415
                    if (scalarZ == 1):
                        label = 450
                
                #415Q=1:GOTO430
                case 415:
                    label = 420
                    scalarQ = 1
                    label = 430
                
                #420IFW(R,S+1)<>0THEN450
                case 420:
                    label = 430
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 450
                
                #430X=INT(RND(1)*3+1)
                case 430:
                    label = 440
                    scalarX = self.round_down_to_int(self.random(1)*3+1)
                
                #440ONXGOTO790,860,910
                case 440:
                    label = 450
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 860
                    if self.as_int(scalarX) == 3:
                        label = 910
                
                #450X=INT(RND(1)*2+1)
                case 450:
                    label = 460
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #460ONXGOTO790,860
                case 460:
                    label = 470
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 860
                
                #470IFS<>VTHEN490
                case 470:
                    label = 480
                    if (scalarS != scalarV):
                        label = 490
                
                #480IFZ=1THEN520
                case 480:
                    label = 485
                    if (scalarZ == 1):
                        label = 520
                
                #485Q=1:GOTO500
                case 485:
                    label = 490
                    scalarQ = 1
                    label = 500
                
                #490IFW(R,S+1)<>0THEN520
                case 490:
                    label = 500
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 520
                
                #500X=INT(RND(1)*2+1)
                case 500:
                    label = 510
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #510ONXGOTO790,910
                case 510:
                    label = 520
                    if self.as_int(scalarX) == 1:
                        label = 790
                    if self.as_int(scalarX) == 2:
                        label = 910
                
                #520GOTO790
                case 520:
                    label = 530
                    label = 790
                
                #530IFS-1=0THEN670
                case 530:
                    label = 540
                    if (scalarS-1 == 0):
                        label = 670
                
                #540IFW(R,S-1)<>0THEN670
                case 540:
                    label = 545
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS-1)] != 0):
                        label = 670
                
                #545IFR=HTHEN610
                case 545:
                    label = 547
                    if (scalarR == scalarH):
                        label = 610
                
                #547IFW(R+1,S)<>0THEN610
                case 547:
                    label = 550
                    if (matrixW[self.as_int(scalarR+1)][self.as_int(scalarS)] != 0):
                        label = 610
                
                #550IFS<>VTHEN560
                case 550:
                    label = 552
                    if (scalarS != scalarV):
                        label = 560
                
                #552IFZ=1THEN590
                case 552:
                    label = 554
                    if (scalarZ == 1):
                        label = 590
                
                #554Q=1:GOTO570
                case 554:
                    label = 560
                    scalarQ = 1
                    label = 570
                
                #560IFW(R,S+1)<>0THEN590
                case 560:
                    label = 570
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 590
                
                #570X=INT(RND(1)*3+1)
                case 570:
                    label = 580
                    scalarX = self.round_down_to_int(self.random(1)*3+1)
                
                #580ONXGOTO820,860,910
                case 580:
                    label = 590
                    if self.as_int(scalarX) == 1:
                        label = 820
                    if self.as_int(scalarX) == 2:
                        label = 860
                    if self.as_int(scalarX) == 3:
                        label = 910
                
                #590X=INT(RND(1)*2+1)
                case 590:
                    label = 600
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #600ONXGOTO820,860
                case 600:
                    label = 610
                    if self.as_int(scalarX) == 1:
                        label = 820
                    if self.as_int(scalarX) == 2:
                        label = 860
                
                #610IFS<>VTHEN630
                case 610:
                    label = 620
                    if (scalarS != scalarV):
                        label = 630
                
                #620IFZ=1THEN660
                case 620:
                    label = 625
                    if (scalarZ == 1):
                        label = 660
                
                #625Q=1:GOTO640
                case 625:
                    label = 630
                    scalarQ = 1
                    label = 640
                
                #630IFW(R,S+1)<>0THEN660
                case 630:
                    label = 640
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 660
                
                #640X=INT(RND(1)*2+1)
                case 640:
                    label = 650
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #650ONXGOTO820,910
                case 650:
                    label = 660
                    if self.as_int(scalarX) == 1:
                        label = 820
                    if self.as_int(scalarX) == 2:
                        label = 910
                
                #660GOTO820
                case 660:
                    label = 670
                    label = 820
                
                #670IFR=HTHEN740
                case 670:
                    label = 680
                    if (scalarR == scalarH):
                        label = 740
                
                #680IFW(R+1,S)<>0THEN740
                case 680:
                    label = 685
                    if (matrixW[self.as_int(scalarR+1)][self.as_int(scalarS)] != 0):
                        label = 740
                
                #685IFS<>VTHEN700
                case 685:
                    label = 690
                    if (scalarS != scalarV):
                        label = 700
                
                #690IFZ=1THEN730
                case 690:
                    label = 695
                    if (scalarZ == 1):
                        label = 730
                
                #695Q=1:GOTO710
                case 695:
                    label = 700
                    scalarQ = 1
                    label = 710
                
                #700IFW(R,S+1)<>0THEN730
                case 700:
                    label = 710
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 730
                
                #710X=INT(RND(1)*2+1)
                case 710:
                    label = 720
                    scalarX = self.round_down_to_int(self.random(1)*2+1)
                
                #720ONXGOTO860,910
                case 720:
                    label = 730
                    if self.as_int(scalarX) == 1:
                        label = 860
                    if self.as_int(scalarX) == 2:
                        label = 910
                
                #730GOTO860
                case 730:
                    label = 740
                    label = 860
                
                #740IFS<>VTHEN760
                case 740:
                    label = 750
                    if (scalarS != scalarV):
                        label = 760
                
                #750IFZ=1THEN780
                case 750:
                    label = 755
                    if (scalarZ == 1):
                        label = 780
                
                #755Q=1:GOTO770
                case 755:
                    label = 760
                    scalarQ = 1
                    label = 770
                
                #760IFW(R,S+1)<>0THEN780
                case 760:
                    label = 770
                    if (matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] != 0):
                        label = 780
                
                #770GOTO910
                case 770:
                    label = 780
                    label = 910
                
                #780GOTO1000
                case 780:
                    label = 790
                    label = 1000
                
                #790W(R-1,S)=C
                case 790:
                    label = 800
                    matrixW[self.as_int(scalarR-1)][self.as_int(scalarS)] = scalarC
                
                #800C=C+1:V(R-1,S)=2:R=R-1
                case 800:
                    label = 810
                    scalarC = scalarC+1
                    matrixV[self.as_int(scalarR-1)][self.as_int(scalarS)] = 2
                    scalarR = scalarR-1
                
                #810IFC=H*V+1THEN1010
                case 810:
                    label = 815
                    if (scalarC == scalarH*scalarV+1):
                        label = 1010
                
                #815Q=0:GOTO260
                case 815:
                    label = 820
                    scalarQ = 0
                    label = 260
                
                #820W(R,S-1)=C
                case 820:
                    label = 830
                    matrixW[self.as_int(scalarR)][self.as_int(scalarS-1)] = scalarC
                
                #830C=C+1
                case 830:
                    label = 840
                    scalarC = scalarC+1
                
                #840V(R,S-1)=1:S=S-1:IFC=H*V+1THEN1010
                case 840:
                    label = 850
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS-1)] = 1
                    scalarS = scalarS-1
                    if (scalarC == scalarH*scalarV+1):
                        label = 1010
                
                #850Q=0:GOTO260
                case 850:
                    label = 860
                    scalarQ = 0
                    label = 260
                
                #860W(R+1,S)=C
                case 860:
                    label = 870
                    matrixW[self.as_int(scalarR+1)][self.as_int(scalarS)] = scalarC
                
                #870C=C+1:IFV(R,S)=0THEN880
                case 870:
                    label = 875
                    scalarC = scalarC+1
                    if (matrixV[self.as_int(scalarR)][self.as_int(scalarS)] == 0):
                        label = 880
                
                #875V(R,S)=3:GOTO890
                case 875:
                    label = 880
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 3
                    label = 890
                
                #880V(R,S)=2
                case 880:
                    label = 890
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 2
                
                #890R=R+1
                case 890:
                    label = 900
                    scalarR = scalarR+1
                
                #900IFC=H*V+1THEN1010
                case 900:
                    label = 905
                    if (scalarC == scalarH*scalarV+1):
                        label = 1010
                
                #905GOTO530
                case 905:
                    label = 910
                    label = 530
                
                #910IFQ=1THEN960
                case 910:
                    label = 920
                    if (scalarQ == 1):
                        label = 960
                
                #920W(R,S+1)=C:C=C+1:IFV(R,S)=0THEN940
                case 920:
                    label = 930
                    matrixW[self.as_int(scalarR)][self.as_int(scalarS+1)] = scalarC
                    scalarC = scalarC+1
                    if (matrixV[self.as_int(scalarR)][self.as_int(scalarS)] == 0):
                        label = 940
                
                #930V(R,S)=3:GOTO950
                case 930:
                    label = 940
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 3
                    label = 950
                
                #940V(R,S)=1
                case 940:
                    label = 950
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 1
                
                #950S=S+1:IFC=H*V+1THEN1010
                case 950:
                    label = 955
                    scalarS = scalarS+1
                    if (scalarC == scalarH*scalarV+1):
                        label = 1010
                
                #955GOTO260
                case 955:
                    label = 960
                    label = 260
                
                #960Z=1
                case 960:
                    label = 970
                    scalarZ = 1
                
                #970IFV(R,S)=0THEN980
                case 970:
                    label = 975
                    if (matrixV[self.as_int(scalarR)][self.as_int(scalarS)] == 0):
                        label = 980
                
                #975V(R,S)=3:Q=0:GOTO1000
                case 975:
                    label = 980
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 3
                    scalarQ = 0
                    label = 1000
                
                #980V(R,S)=1:Q=0:R=1:S=1:GOTO250
                case 980:
                    label = 1000
                    matrixV[self.as_int(scalarR)][self.as_int(scalarS)] = 1
                    scalarQ = 0
                    scalarR = 1
                    scalarS = 1
                    label = 250
                
                #1000GOTO210
                case 1000:
                    label = 1010
                    label = 210
                
                #1010IFZ=1THEN1015
                case 1010:
                    label = 1011
                    if (scalarZ == 1):
                        label = 1015
                
                #1011X=INT(RND(1)*H+1)
                case 1011:
                    label = 1012
                    scalarX = self.round_down_to_int(self.random(1)*scalarH+1)
                
                #1012IFV(X,V)=0THEN1014
                case 1012:
                    label = 1013
                    if (matrixV[self.as_int(scalarX)][self.as_int(scalarV)] == 0):
                        label = 1014
                
                #1013V(X,V)=3:GOTO1015
                case 1013:
                    label = 1014
                    matrixV[self.as_int(scalarX)][self.as_int(scalarV)] = 3
                    label = 1015
                
                #1014V(X,V)=1
                case 1014:
                    label = 1015
                    matrixV[self.as_int(scalarX)][self.as_int(scalarV)] = 1
                
                #1015FORJ=1TOV
                case 1015:
                    label = 1016
                    if loopActive1015 == False:
                        scalarJ = 1
                        loopActive1015 = True
                    if (scalarJ - scalarV) * 1 > 0:
                        label = 1073
                
                #1016PRINT"I";
                case 1016:
                    label = 1017
                    self.print_expr("I")
                
                #1017FORI=1TOH
                case 1017:
                    label = 1018
                    if loopActive1017 == False:
                        scalarI = 1
                        loopActive1017 = True
                    if (scalarI - scalarH) * 1 > 0:
                        label = 1041
                
                #1018IFV(I,J)<2THEN1030
                case 1018:
                    label = 1020
                    if (matrixV[self.as_int(scalarI)][self.as_int(scalarJ)] < 2):
                        label = 1030
                
                #1020PRINT"";
                case 1020:
                    label = 1021
                    self.print_expr("   ")
                
                #1021GOTO1040
                case 1021:
                    label = 1030
                    label = 1040
                
                #1030PRINT"I";
                case 1030:
                    label = 1040
                    self.print_expr("  I")
                
                #1040NEXTI
                case 1040:
                    label = 1041
                    scalarI = scalarI + 1
                    label = 1017
                
                #1041PRINT
                case 1041:
                    label = 1043
                    self.println()
                
                #1043FORI=1TOH
                case 1043:
                    label = 1045
                    if loopActive1043 == False:
                        scalarI = 1
                        loopActive1043 = True
                    if (scalarI - scalarH) * 1 > 0:
                        label = 1071
                
                #1045IFV(I,J)=0THEN1060
                case 1045:
                    label = 1050
                    if (matrixV[self.as_int(scalarI)][self.as_int(scalarJ)] == 0):
                        label = 1060
                
                #1050IFV(I,J)=2THEN1060
                case 1050:
                    label = 1051
                    if (matrixV[self.as_int(scalarI)][self.as_int(scalarJ)] == 2):
                        label = 1060
                
                #1051PRINT":";
                case 1051:
                    label = 1052
                    self.print_expr(":  ")
                
                #1052GOTO1070
                case 1052:
                    label = 1060
                    label = 1070
                
                #1060PRINT":--";
                case 1060:
                    label = 1070
                    self.print_expr(":--")
                
                #1070NEXTI
                case 1070:
                    label = 1071
                    scalarI = scalarI + 1
                    label = 1043
                
                #1071PRINT"."
                case 1071:
                    label = 1072
                    self.print_expr(".")
                    self.println()
                
                #1072NEXTJ
                case 1072:
                    label = 1073
                    scalarJ = scalarJ + 1
                    label = 1015
                
                #1073END
                case 1073:
                    label = 9999
                    label = 9999

                case 9999:
                    break

                case _:
                    raise ValueError(f"The label {label} is not recognized.")

    # The original run() method now only displays the maze
    def run(self):
        maze = self.generate_maze()
        print(maze)

if __name__ == "__main__":
    Main().run()

