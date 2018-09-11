X=' '
Y='x'
Z='o'
board=[X,X,X,X,X,X,X,X,X]
def drawBoard(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
drawBoard(board)

#after 4 moves atleast
def winMoves(list):
    tie = 0
    if (list[0]==list[1]==list[2]==Y) or (list[3]==list[4]==list[5]==Y) or (list[6]==list[7]==list[8]==Y):
        print("Player 1 wins")
    elif (list[0]==list[3]==list[6]==Y) or (list[1]==list[4]==list[7]==Y) or (list[2]==list[5]==list[8]==Y):
        print("Player 1 wins")
    elif (list[0]==list[4]==list[8]==Y) or (list[2]==list[4]==list[6]==Y):
        print("Player 1 wins")
    elif (list[0]==list[1]==list[2]==Z) or (list[3]==list[4]==list[5]==Z) or (list[6]==list[7]==list[8]==Z):
        print("Player 2 wins")
    elif (list[0]==list[3]==list[6]==Z) or (list[1]==list[4]==list[7]==Z) or (list[2]==list[5]==list[8]==Z):
        print("Player 2 wins")
    elif (list[0]==list[4]==list[8]==Z) or (list[2]==list[4]==list[6]==Z):
        print("Player 2 wins")
    elif (list[0]==list[1]!=list[2]!=X) or (list[3]==list[4]!=list[5]!=X) or (list[6]==list[7]!=list[8]!=X) or  (list[0]==list[3]!=list[6]!=X) or (list[1]==list[4]!=list[7]!=X):
        print ("Draw")
    elif (list[2]==list[5]!=list[8]!=X) or (list[0]==list[4]!=list[8]!=X) or (list[2]==list[4]!=list[6]!=X):
        print ("Draw")
    else:
        tie = 1
    return tie


while winMoves(board) is 1:
    ip=int(input("Player 1: Enter your turn between 1-9: "))
    board[ip-1]=Y
    print (drawBoard(board))
    ip2=int(input("Player 2: Enter your turn between 1-9: "))
    board[ip2-1]=Z
    print (drawBoard(board))
