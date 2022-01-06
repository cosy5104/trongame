players ={}

val1=int(input("Enter board size : "))
if val1>3:
        val=int(val1-1)
        players={
            1:(0,0),
            2:(val,val)
        }
        r=val1
        c=val1

        board=[ [ 0 for i in range(c) ] for j in range(r) ]
        board[0][0]=1
        board[val][val]=2
        print("\nBoard of size ("+ str(val1) + " * "+str(val1)+") created with default locations")

        for index,item in enumerate(board,start=1):
            print (item)
            if not index % 3:
                print
                
        print('''
            Move      Move Type      
            -------     ---------    
            R           RIGHT          
            L           LEFT 
            U           UP  
            D           DOWN                   
            ''')
        
else:
         print('''
                Size board should be greater tha 3....try again
                ''')

def validatemove(currentpos,r,c):
    lis=list(currentpos)
    lis[0]+=r
    lis[1]+=c
    if board[lis[0]][lis[1]]==0:
        return True
    return False

def changevalues(currentpos,r,c,currentplayer):
    lis=list(currentpos)
    board[lis[0]][lis[1]]='X'
    lis[0]+=r
    lis[1]+=c
    board[lis[0]][lis[1]]=currentplayer
    players[currentplayer]=tuple(lis)
    #print('\n\ncurrent position==>',tuple(lis))
    return

def changeplayer(currentplayer):
    if currentplayer==1:
        return 2
    return 1

def intfn(currentplayer,currentpos,move):
    if move=='r':
        c=1
        r=0
        valid=validatemove(currentpos,r,c)
        if valid:
            changevalues(currentpos,r,c,currentplayer)
            nextplayer=changeplayer(currentplayer)
            print('\nGame board==>')
            for index,item in enumerate(board,start=1):
                     print (item)
                     if not index % 3:
                              print
            
            extfn(nextplayer)
            return
        print('Game over !!!')
        print("Player "+str(changeplayer(currentplayer)) + " won")
        return
    if move=='l':
        c=-1
        r=0
        valid=validatemove(currentpos,r,c)
        if valid:
            changevalues(currentpos,r,c,currentplayer)
            nextplayer=changeplayer(currentplayer)
            print('\nGame board==>')
            for index,item in enumerate(board,start=1):
                     print (item)
                     if not index % 3:
                              print
           # print('\n\nboard==>',board)
            extfn(nextplayer)
            return
        print('Game over !!!')
        print("Player "+str(changeplayer(currentplayer)) + " won")
        return
    if move=='d':
        c=0
        r=1
        valid=validatemove(currentpos,r,c)
        if valid:
            changevalues(currentpos,r,c,currentplayer)
            nextplayer=changeplayer(currentplayer)
            print('\nGame board==>')
            for index,item in enumerate(board,start=1):
                     print (item)
                     if not index % 3:
                              print
            #print('\n\nboard==>',board)
            extfn(nextplayer)
            return
        print('Game over !!!')
        print("Player "+str(changeplayer(currentplayer)) + " won")
        return   
    if move=='u':
         c=0
         r=-1
         valid=validatemove(currentpos,r,c)
         if valid:
            changevalues(currentpos,r,c,currentplayer)
            nextplayer=changeplayer(currentplayer)
            print('\nGame board==>')
            for index,item in enumerate(board,start=1):
                     print (item)
                     if not index % 3:
                              print
           # print('\n\nboard==>',board)
            extfn(nextplayer)
            return
         print('Game over !!!')
         print("Player "+str(changeplayer(currentplayer)) + " won")
         return
      

def extfn(currentplayer):
    currentpos=players[currentplayer]
    
    move=input(f">>Enter the move of  {currentplayer} [R/L/U/D] : ").lower()
    if move=='r' or move=='l' or move=='u' or move=='d':
             #print('previous position=======>',currentpos)
             intfn(currentplayer,currentpos,move)
    else:
            print('''
                wrong move....try again
                ''')
            extfn(currentplayer)

 #main
    
try:
    currentplayer=1
    extfn(currentplayer)
    #print(players)
except Exception as e:
         print('''
          move is illegal
          ''')
         print("Player "+str(changeplayer(currentplayer)) + " won")r
         