import sys, pygame, time


# generate rectangles for each square. rectangles for squares can be reference based on rectlist[x][y]
def generate_rectlist(coorlist):
    rectlist = []
    for pair in coorlist:
        rectlist.append((pygame.Rect(0 + (62.5 * pair[0]), 437.5 - (62.5 * pair[1]), 62.5, 62.5), pair))
    return rectlist


def shade_area(x, y):
    screen.blit(blue_square, (31.25 + (62.5 * x) - 25, 500 - 31.5 - 25 - (62.5 * y)))
    pygame.display.flip()


# draw board and pieces in pygame window based on squarelist
def reset_board(squarelist, shadelist=[]):
    screen.blit(background, (0, 0))
    for coor_pair in shadelist:
        shade_area(coor_pair[0], coor_pair[1])
    for column in squarelist:
        for space in column:
            if space:
                if space.color == True:
                    if space.type == 'rook':
                        screen.blit(b_rook, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'knight':
                        screen.blit(b_knight, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'bishop':
                        screen.blit(b_bishop, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'queen':
                        screen.blit(b_queen, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'king':
                        screen.blit(b_king, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'pawn':
                        screen.blit(b_pawn, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                else:
                    if space.type == 'rook':
                        screen.blit(w_rook, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'knight':
                        screen.blit(w_knight, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'bishop':
                        screen.blit(w_bishop, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'queen':
                        screen.blit(w_queen, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'king':
                        screen.blit(w_king, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                    if space.type == 'pawn':
                        screen.blit(w_pawn, (10 + space.square[0] * 62.5, 445 - space.square[1] * 62.5))
                # commented out because it didn't work for obvious reasons, but above seems very inneficient
                '''
                if space.color == True:
                    prefix = 'b_'
                else:
                    prefix = 'w_'
                screen.blit(prefix + space.type, (10 + space.square[0]*62.5, 445 - space.square[1]*)2.5))
                '''

    pygame.display.flip()


# size of piece in pixels: 500 / 8 = 62.5 px len per side
def generate_squarelist():
    # hardcoded stuff cause I already had it and I didn't feel like writing another way
    squarelist = [['w_rook', 'w_pawn', '', '', '', '', 'b_pawn', 'b_rook'],
                  ['w_knight', 'w_pawn', '', '', '', '', 'b_pawn', 'b_knight'],
                  ['w_bishop', 'w_pawn', '', '', '', '', 'b_pawn', 'b_bishop'],
                  ['w_queen', 'w_pawn', '', '', '', '', 'b_pawn', 'b_queen'],
                  ['w_king', 'w_pawn', '', '', '', '', 'b_pawn', 'b_king'],
                  ['w_bishop', 'w_pawn', '', '', '', '', 'b_pawn', 'b_bishop'],
                  ['w_knight', 'w_pawn', '', '', '', '', 'b_pawn', 'b_knight'],
                  ['w_rook', 'w_pawn', '', '', '', '', 'b_pawn', 'b_rook']]
    for column in range(0, 8):
        for row in range(0, 8):
            item = squarelist[column][row]
            if item != '':
                generated_piece = Piece()
                # fix color
                if item[0] == 'b':
                    generated_piece.color = True
                generated_piece.type = item[2::]
                generated_piece.square = (column, row)
                squarelist[column][row] = generated_piece
            else:
                squarelist[column][row] = None
    return squarelist


class Piece:
    # rook, knight, bishop, queen, king, pawn
    type = ''
    # True = black, False = white
    color = False
    square = ()
    possible_moves = []

    # funky stuff happening here check back when ur good to fix it
    def get_possible_moves(self, white_possible_moves, black_possible_moves):
        self.possible_moves = []

        # CHECK FOR ROOK
        def check_diagonals():
            # check north-east
            y = self.square[1]
            for x in range(self.square[0] + 1, 8):
                y += 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check south-east
            y = self.square[1]
            for x in range(self.square[0] + 1, 8):
                y -= 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check north-west
            y = self.square[1]
            for x in range(self.square[0] - 1, -1, -1):
                y += 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))
            # check south-west
            y = self.square[1]
            for x in range(self.square[0] - 1, -1, -1):
                y -= 1
                if y > 7 or y < 0:
                    break
                if squarelist[x][y]:
                    if self.color != squarelist[x][y].color:
                        self.possible_moves.append((x, y))
                    break
                else:
                    self.possible_moves.append((x, y))

        def check_parallels():
            # check left
            for xcor in range(self.square[0] - 1, -1, -1):

                if squarelist[xcor][self.square[1]]:
                    if self.color != squarelist[xcor][self.square[1]].color:
                        self.possible_moves.append((xcor, self.square[1]))
                    break
                else:
                    self.possible_moves.append((xcor, self.square[1]))
            # check right
            for xcor in range(self.square[0] + 1, 8):

                if squarelist[xcor][self.square[1]]:
                    if self.color != squarelist[xcor][self.square[1]].color:
                        self.possible_moves.append((xcor, self.square[1]))
                    break
                else:
                    self.possible_moves.append((xcor, self.square[1]))
            # check up
            for ycor in range(self.square[1] + 1, 8):

                if squarelist[self.square[0]][ycor]:
                    if self.color != squarelist[self.square[0]][ycor].color:
                        self.possible_moves.append((self.square[0], ycor))
                    break
                else:
                    self.possible_moves.append((self.square[0], ycor))
            # check down
            for ycor in range(self.square[1] - 1, -1, -1):

                if squarelist[self.square[0]][ycor]:
                    if self.color != squarelist[self.square[0]][ycor].color:
                        self.possible_moves.append((self.square[0], ycor))
                    break
                else:
                    self.possible_moves.append((self.square[0], ycor))

        if self.type == 'rook':
            check_parallels()
        # CHECK FOR KNIGHT
        if self.type == 'knight':
            # calculate all possible moves
            moves = [(self.square[0] - 2, self.square[1] + 1), (self.square[0] - 2, self.square[1] - 1),
                     (self.square[0] + 2, self.square[1] + 1), (self.square[0] + 2, self.square[1] - 1),
                     (self.square[0] + 1, self.square[1] + 2), (self.square[0] - 1, self.square[1] + 2),
                     (self.square[0] + 1, self.square[1] - 2), (self.square[0] - 1, self.square[1] - 2)]
            for pair in moves:
                # for each possible move check if really possible, if so add to list
                if pair[0] <= 7 and pair[0] >= 0 and pair[1] <= 7 and pair[1] >= 0:
                    if squarelist[pair[0]][pair[1]]:
                        if self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
                    else:
                        self.possible_moves.append((pair[0], pair[1]))
        # CHECK FOR BISHOP
        if self.type == 'bishop':
            check_diagonals()
        # CHECK FOR QUEEN
        if self.type == 'queen':
            check_diagonals()
            check_parallels()
        # CHECK FOR PAWN
        if self.type == 'pawn':
            if self.color == True:
                yiteration = -1
            else:
                yiteration = 1
            # check diagonal moves
            attacks = [(self.square[0] - 1, self.square[1] + yiteration),
                       (self.square[0] + 1, self.square[1] + yiteration)]
            for pair in attacks:
                if pair[0] <= 7 and pair[1] <= 7 and pair[0] >= 0 and pair[1] >= 0:

                    if squarelist[pair[0]][pair[1]]:
                        if self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
            # check forward moves (including 2 up if hasnt moved)
            moves = [(self.square[0], self.square[1] + yiteration)]
            if self.square[1] == 1 and self.color == False:
                moves.append((self.square[0], self.square[1] + 2))
            elif self.square[1] == 6 and self.color == True:
                moves.append((self.square[0], self.square[1] - 2))
            # add to list if move empty
            for move in moves:
                if move[0] <= 7 and move[1] <= 7 and move[0] >= 0 and move[1] >= 0:
                    if squarelist[move[0]][move[1]] == None:
                        self.possible_moves.append((move[0], move[1]))

        # CHECK FOR KING
        if self.type == 'king':
            moves = [(self.square[0] + 1, self.square[1] + 1), (self.square[0] + 1, self.square[1] - 1),
                     (self.square[0], self.square[1] + 1), (self.square[0], self.square[1] - 1),
                     (self.square[0] - 1, self.square[1] + 1), (self.square[0] - 1, self.square[1] - 1),
                     (self.square[0] + 1, self.square[1]), (self.square[0] - 1, self.square[1])]
            if self.color == True:
                checklist = white_possible_moves
            else:
                checklist = black_possible_moves
            for pair in moves:
                # for each possible move check if really possible, if so add to list
                if pair[0] <= 7 and pair[0] >= 0 and pair[1] <= 7 and pair[1] >= 0 and pair not in checklist:
                    if squarelist[pair[0]][pair[1]]:
                        if self.color != squarelist[pair[0]][pair[1]].color:
                            self.possible_moves.append((pair[0], pair[1]))
                    else:
                        self.possible_moves.append((pair[0], pair[1]))


def move_piece(init, final):
    init_x, init_y, final_x, final_y = init[0], init[1], final[0], final[1]
    '''
    if squarelist[final_x][final_y]:
        #play_animation

    else:
        #play_animation switching Piece object and None
    '''
    squarelist[final_x][final_y] = squarelist[init_x][init_y]
    squarelist[init_x][init_y] = None
    squarelist[final_x][final_y].square = final


def take_turn(currcolor):
    player_piece_coord = []
    black_possible_moves = []
    white_possible_moves = []
    for column in squarelist:
        for item in column:
            if item:
                if item.color == currcolor:
                    player_piece_coord.append(item.square)
                item.get_possible_moves(white_possible_moves, black_possible_moves)
                if item.type == 'king':
                    # if king has no possible moves and is in check
                    if item.possible_moves == [] and (item.square in black_possible_moves or item.square in white_possible_moves):
                        gameover = True
                        if item.color == True:
                            print('White Wins!!!')
                        else:
                            print('Black Wins!!!')
                        time.sleep(5)
                        raise SystemExit
                if item.color == True:
                    for move in item.possible_moves:
                        if move not in black_possible_moves:
                            black_possible_moves.append(move)
                else:
                    for move in item.possible_moves:
                        if move not in white_possible_moves:
                            white_possible_moves.append(move)
    # generate list of rectangles ( could change to list of tuples that have coordinates too: eg
    rect_list = generate_rectlist(player_piece_coord)
    # wait for input then shade and select it
    turnover = False
    selectedsquare = None
    shadelist = []
    possible_moves = []
    while turnover == False:
        oldsquarelist = squarelist
        oldshadelist = shadelist
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            # if user clicks
            if event.type == pygame.MOUSEBUTTONUP:
                # pos = mouse click position
                pos = pygame.mouse.get_pos()
                # if no piece currently selected and turn still going
                if selectedsquare == None and turnover == False:
                    for rect_tuple in rect_list:
                        if rect_tuple[0].collidepoint(pos):
                            selectedsquare = (rect_tuple[1][0], rect_tuple[1][1])
                            possible_moves = squarelist[rect_tuple[1][0]][rect_tuple[1][1]].possible_moves
                            # if no moves, deselect and break rect checking loop
                            if len(possible_moves) == 0:
                                selectedsquare = None
                                break
                            shadelist = [(rect_tuple[1][0], rect_tuple[1][1])]
                            rect_list_possible_moves = generate_rectlist(possible_moves)
                            for move in squarelist[rect_tuple[1][0]][rect_tuple[1][1]].possible_moves:
                                shadelist.append((move[0], move[1]))

                # if piece is currently selected and turn still going
                elif turnover == False:
                    for rect_tuple in rect_list_possible_moves:
                        if rect_tuple[0].collidepoint(pos):
                            move_piece(selectedsquare, (rect_tuple[1][0], rect_tuple[1][1]))
                            turnover = True
                    # if click wasn't on possible move, deselect square or if turn done, deselect square
                    selectedsquare = None
                    shadelist = []
        if shadelist != oldshadelist or squarelist != oldsquarelist:
            reset_board(squarelist,shadelist)



# set up pygame window
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)

# load test images for UBUNTU LAPTOP
'''
background = pygame.image.load("/home/jeremy/Pictures/background.png")
blue_square = pygame.image.load('/home/jeremy/Pictures/blue.png')
blue_square = blue_square.convert()
blue_square.set_alpha(100)
b_king = pygame.image.load("/home/jeremy/Pictures/king.png")
b_queen = pygame.image.load("/home/jeremy/Pictures/queen.png")
b_knight = pygame.image.load("/home/jeremy/Pictures/knight.png")
b_bishop = pygame.image.load("/home/jeremy/Pictures/bishop.png")
b_rook = pygame.image.load("/home/jeremy/Pictures/rook.png")
b_pawn = pygame.image.load("/home/jeremy/Pictures/pawn.png")
w_king = b_king
w_queen = b_queen
w_knight = b_knight
w_bishop = b_bishop
w_rook = b_bishop
w_pawn = b_pawn
'''
# load images for WINDOWS DESKTOP

background = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\finalchessboard.png")
blue_square = pygame.image.load('C:\\Users\\Jeremy\\Pictures\\chess\\blue.png')
blue_square = blue_square.convert()
blue_square.set_alpha(100)
b_king = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_king.png")
b_queen = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_queen.png")
b_knight = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_knight.png")
b_bishop = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_bishop.png")
b_rook = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_rook.png")
b_pawn = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\b_pawn.png")
w_king = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_king.png")
w_queen = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_queen.png")
w_knight = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_knight.png")
w_bishop = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_bishop.png")
w_rook = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_rook.png")
w_pawn = pygame.image.load("C:\\Users\\Jeremy\\Pictures\\chess\\w_pawn.png")


# generate squarelist
squarelist = generate_squarelist()
reset_board(squarelist)

currcolor = False
while True:
    take_turn(currcolor)
    currcolor = not currcolor

# comment out for use in testing drawing function and correct board-piece placement
'''
xcordinate = int(input("x: "))
ycordinate = int(input("y: "))
coordinates = (xcordinate, ycordinate)
squarelist[0][0].square = coordinates
squarelist[coordinates[0]][coordinates[1]],squarelist[0][0] = squarelist[0][0],squarelist[coordinates[0]][coordinates[1]]
reset_board(squarelist)
input()
'''