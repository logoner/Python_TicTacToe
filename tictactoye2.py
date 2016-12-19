#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# title: "TicTacToy Game"
# ver.: 0.2.4

# lets run game

# initiations global arguments:
cells = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']

# define game function
    
#transform list to string
def lsttostr(lstin):
    strout = str()
    for i in range(len(lstin)):
        strout = strout + str(lstin[i])
    return strout

#user change gamepool
def usrchngegp(gpin, usrtrn):
    gplst = list(gpin)
        
    #for i in range(9):
    #    if (usrtrn == cells[i]) and (gplst[i] == '_'):
    #        gplst[i] = 'X'
    #        
    #WTF else ? !!!! errors!
    #for i in range(9):
    #    if usrtrn != cells[i]:
    #        print('Missed input!\nEnter a cels again.')
    #        print('')
    #        input('Press Enter key.')
    #        gplst[0] = 'X'
   

    if (usrtrn == 'a1') and (gplst[0] == '_'):
        gplst[0] = 'X'
    elif (usrtrn == 'a2') and (gplst[1] == '_'):
        gplst[1] = 'X'
    elif (usrtrn == 'a3') and (gplst[2] == '_'):
        gplst[2] = 'X'
    elif (usrtrn == 'b1') and (gplst[3] == '_'):
        gplst[3] = 'X'
    elif (usrtrn == 'b2') and (gplst[4] == '_'):
        gplst[4] = 'X'
    elif (usrtrn == 'b3') and (gplst[5] == '_'):
        gplst[5] = 'X'
    elif (usrtrn == 'c1') and (gplst[6] == '_'):
        gplst[6] = 'X'
    elif (usrtrn == 'c2') and (gplst[7] == '_'):
        gplst[7] = 'X'
    elif (usrtrn == 'c3') and (gplst[8] == '_'):
        gplst[8] = 'X'
    else:
        print('Missed input!\nEnter a cels again.')
        #print('')
        
        input('Press Enter key.')
        gplst[0] = 'X'
    
    return lsttostr(gplst)
#nxtturnchk(nxtturn)
def nxtturnchk(innxtturn):
    # cells is global arguments
    #gplst = list(gpin)
    for i in cells:
        if innxtturn == i:
            return True
    print('is not a1-a2')
    return False

#ai change game pool
def aichngegp(gpin):
    gplst = list(gpin)
    
    #test last states (ai winner!)
    #horisontal
    if gplst[0]+gplst[1]+gplst[2] == 'OO_':
        gplst[2] = 'O'
        #print('test')
    elif gplst[3]+gplst[4]+gplst[5] == 'OO_':
        gplst[5] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == 'OO_':
        gplst[8] = 'O'
        
    elif gplst[0]+gplst[1]+gplst[2] == 'O_O':
        gplst[1] = 'O'
    elif gplst[3]+gplst[4]+gplst[5] == 'O_O':
        gplst[4] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == 'O_O':
        gplst[7] = 'O'
        
    elif gplst[0]+gplst[1]+gplst[2] == '_OO':
        gplst[0] = 'O'
    elif gplst[3]+gplst[4]+gplst[5] == '_OO':
        gplst[3] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == '_OO':
        gplst[6] = 'O'
        
    #vertical
    elif gplst[0]+gplst[3]+gplst[6] == '_OO':
        gplst[0] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == '_OO':
        gplst[1] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == '_OO':
        gplst[2] = 'O'
        #print('test')
        
    elif gplst[0]+gplst[3]+gplst[6] == 'O_O':
        gplst[3] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == 'O_O':
        gplst[4] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == 'O_O':
        gplst[5] = 'O'
        
    elif gplst[0]+gplst[3]+gplst[6] == 'OO_':
        gplst[6] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == 'OO_':
        gplst[7] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == 'OO_':
        gplst[8] = 'O'
    
    #diagonal
    elif gplst[0]+gplst[4]+gplst[8] == '_OO':
        gplst[0] = 'O'
    elif gplst[2]+gplst[4]+gplst[6] == '_OO':
        gplst[2] = 'O'
        #print('test')
        
    elif gplst[0]+gplst[4]+gplst[8] == 'O_O':
        gplst[4] = 'O'
    elif gplst[2]+gplst[4]+gplst[6] == 'O_O':
        gplst[4] = 'O'
        
    elif gplst[0]+gplst[4]+gplst[8] == 'OO_':
        gplst[8] = 'O'
    elif gplst[2]+gplst[4]+gplst[6] == 'OO_':
        gplst[6] = 'O'
        
    #test diagonal
    #X_*
    #?O?
    #??X
    elif gplst[0]+gplst[1]+gplst[2]+gplst[4]+gplst[8] == 'X__OX':
        gplst[2] = 'O'
        #print('test')
    #X??
    #_O?
    #_?X
    elif gplst[0]+gplst[3]+gplst[6]+gplst[4]+gplst[8] == 'X__OX':
        gplst[6] = 'O'
        print('test')
        
    #test defens from beast_th
    #XXO
    #OOX
    #X__
    elif gpin == 'XXOOOXX__':
        gplst[7] = 'O'
    #OX_
    #XO_
    #XOX
    elif gpin == 'OX_XO_XOX':
        gplst[5] = 'O'
    #__X
    #XOO
    #OXX
    elif gpin == '__XXOOOXX':
        gplst[1] = 'O'
    #XOX
    #_OX
    #_XO
    elif gpin == 'XOX_OX_XO':
        gplst[7] = 'O'
    #
    #O__
    #OXX
    #X__
    elif gpin == 'O__OXXX__':
        gplst[1] = 'O'
    
    #XOO
    #_X_
    #_X_
    elif gpin == 'XOO_X__X_':
        gplst[5] = 'O'
    
    #__X
    #XXO
    #__O
    elif gpin == '__XXXO__O':
        gplst[7] = 'O'
    
    #_X_
    #_X_
    #OOX
    elif gpin == '_X__X_OOX':
        gplst[3] = 'O'
        
    #
    #O_X
    #XXO
    #*__
    elif gpin == 'O_XXXO___':
        gplst[6] = 'O'
    
    #*XO
    #_X_
    #_OX
    elif gpin == '_XO_X__OX':
        gplst[0] = 'O'
    
    #__*
    #OXX
    #X_O
    elif gpin == '___OXXX_O':
        gplst[2] = 'O'
    
    #XO_
    #_X_
    #OX*
    elif gpin == 'XO__X_OX_':
        gplst[8] = 'O'
    
    #test rows lef to right
    elif gplst[0]+gplst[1]+gplst[2] == 'XX_':
        gplst[2] = 'O'
    elif gplst[3]+gplst[4]+gplst[5] == 'XX_':
        gplst[5] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == 'XX_':
        gplst[8] = 'O'
        
    #test colums up to down
    elif gplst[0]+gplst[3]+gplst[6] == 'XX_':
        gplst[6] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == 'XX_':
        gplst[7] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == 'XX_':
        gplst[8] = 'O'
        
    #test rows right to left
    elif gplst[0]+gplst[1]+gplst[2] == '_XX':
        gplst[0] = 'O'
    elif gplst[3]+gplst[4]+gplst[5] == '_XX':
        gplst[3] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == '_XX':
        gplst[6] = 'O'
        
    #test colums down to up
    elif gplst[0]+gplst[3]+gplst[6] == '_XX':
        gplst[0] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == '_XX':
        gplst[1] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == '_XX':
        gplst[2] = 'O'
        
    #test median rows
    elif gplst[0]+gplst[1]+gplst[2] == 'X_X':
        gplst[1] = 'O'
    elif gplst[3]+gplst[4]+gplst[5] == 'X_X':
        gplst[4] = 'O'
    elif gplst[6]+gplst[7]+gplst[8] == 'X_X':
        gplst[7] = 'O'
        
    #test median colums
    elif gplst[0]+gplst[3]+gplst[6] == 'X_X':
        gplst[3] = 'O'
    elif gplst[1]+gplst[4]+gplst[7] == 'X_X':
        gplst[4] = 'O'
    elif gplst[2]+gplst[5]+gplst[8] == 'X_X':
        gplst[5] = 'O'
        
    #diagonal 'shuffle'
    elif gplst[0]+gplst[4]+gplst[8]+gplst[2] == 'OXX_':
        gplst[2] = 'O'
    #elif gplst[2]+gplst[4]+gplst[6]+gplst[5] == 'OXX_':
    #    gplst[5] = 'O'
    #elif gplst[8]+gplst[4]+gplst[0]+gplst[7] == 'OXX_':
    #    gplst[7] = 'O'
    #elif gplst[6]+gplst[4]+gplst[2]+gplst[3] == 'OXX_':
    #    gplst[3] = 'O'
        
    #test first states
    elif gplst[4] == '_':
        gplst[4] = 'O'
    elif gplst[0] == '_':
        gplst[0] = 'O'
        
    #no more chanse for you
    else:
        calc = 0
        for n in gpin:
            if n == '_':
                gplst[calc] = 'O'
                break
            calc = calc + 1
    
    return lsttostr(gplst)
    
#check game state, (who is winner)
def chkgmestate(gpin):

    gmst = gpin
    winx = 'XXX'
    wino = 'OOO'
    win = False
    
    # check user win
    for check in [winx, wino]:
    
        #test wtf. usr not win?
        #print(gmst[0]+gmst[3]+gmst[6])
        
        #horisontal
        if gmst[0]+gmst[1]+gmst[2] == check:
            win = True
        elif gmst[3]+gmst[4]+gmst[5] == check:
            win = True
        elif gmst[6]+gmst[7]+gmst[8] == check:
            win = True
        #vertcal
        elif gmst[0]+gmst[3]+gmst[6] == check:
            win = True
        elif gmst[1]+gmst[4]+gmst[7] == check:
            win = True
        elif gmst[2]+gmst[5]+gmst[8] == check:
            win = True
        #diagonal
        elif gmst[0]+gmst[4]+gmst[8] == check:
            win = True
        elif gmst[2]+gmst[4]+gmst[6] == check:
            win = True

    return win
#draw game area screen
def drawgmescrn(gpin):
    
    #
    print('')
    print('\t_|1|2|3|')
    print('\tA|'+gpin[0]+'|'+gpin[1]+'|'+gpin[2]+'|')
    print('\tB|'+gpin[3]+'|'+gpin[4]+'|'+gpin[5]+'|')
    print('\tC|'+gpin[6]+'|'+gpin[7]+'|'+gpin[8]+'|')
    print('')
    
# end of define functions


# score of game
usrscore = 0
aiscore = 0

exitgame = False
while exitgame == False:
    
    # initialization game variables:
    
    # the game pool variable
    gp = '_________'
    
    # draw menu screen
    print('')
    print('\tTicTacToy:')
    print('\tMenu:')
    print('\t1 - New game.')
    print('\t2 - Score.')
    print('\t3 - Exit.')
    print('')
    mnu = input('\tType your choise:')
    
    if mnu == '2':
        # draw score screen
        print('')
        print('\tTicTacToy:')
        print('\tScore:')
        print('\tYour wins:', usrscore)
        print('\tAI wins:', aiscore)
        print('')
        input('\tEnter any key for back:')
    elif mnu == '1':
        gameover = False
        while gameover == False:
        
            # game pool AI changed
            # in this place you need to add check ai
            # if usr did not move, did not check ai

            # draw game area screen
            print('')
            print('\tTicTacToy:')
            drawgmescrn(gp)
            
            # gamer next turn
            nxtturn = str(input('Type A1-C3 for place "X":\n\t'))
            
            if nxtturnchk(nxtturn) == True:
                gp = usrchngegp(gp, nxtturn)
           
                #user win chek
                gameover = chkgmestate(gp)            
                #test wtf. usr not win?
                #print("usr gameover", gameover)
            
            
                if gameover == True:
                    drawgmescrn(gp)
                    print('\tYOU WIN!')
                    usrscore = usrscore + 1
                    break
                
                gp = aichngegp(gp)
            
                #ai win chek
                gameover = chkgmestate(gp)
            
                if gameover == True:
                    drawgmescrn(gp)
                    print('\tAI WIN!')
                    aiscore = aiscore + 1
                    break
                
                #no winners check
                #XXO
                #OOX
                #XOX
                if gp == 'XXOOOXXOX':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #OXX
                #XOO
                #XOX
                elif gp == 'OXXXOOXOX':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #XOX
                #XOO
                #OXX
                elif gp == 'XOXXOOOXC':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #XOX
                #OOX
                #XXO
                elif gp == 'XOXOOXXXO':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break

                #
                #OXO
                #XXO
                #XOX
                elif gp == 'OXOXXOXOX':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #XXO
                #OXX
                #XOO
                elif gp == 'XXOOXXXOO':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #XOX
                #OXX
                #OXO
                elif gp == 'XOXOXXOXO':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                
                #OOX
                #XXO
                #OXX
                elif gp == 'OOXXXOOXX':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                #
                #OXX
                #XXO
                #OOX
                elif gp == 'OXXXXOOOX':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                    
                #OXO
                #OXX
                #XOX
                #elif gp == 'OXOOXXXOX':
                #    drawgmescrn(gp)
                #    print('\tNo winners!')
                #    gameover = True
                #    break
                    
                #XOO
                #OXX
                #XXO
                elif gp == 'XOOOXXXXO':
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break
                    
                #XOX
                #XXO
                #OXO
                #elif gp == 'XOXXXOOXO':
                #    drawgmescrn(gp)
                #    print('\tNo winners!')
                #    gameover = True
                #    break
                
                calc = 0
                for cellchk in gp:
                   
                    gameover = False
                    if cellchk == '_':
                        calc = calc + 1
                        
                if calc == 0:
                    drawgmescrn(gp)
                    print('\tNo winners!')
                    gameover = True
                    break   

    else:
        exitgame = True