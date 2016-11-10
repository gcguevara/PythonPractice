import random

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3),
         (1, 0), (1, 1), (1, 2), (1, 3),
         (2, 0), (2, 1), (2, 2), (2, 3),
         (3, 0), (3, 1), (3, 2), (3, 3),
         (4, 0), (4, 1), (4, 2), (4, 3),
         (5, 0), (5, 1), (5, 2), (5, 3)]


def generate_locations():
    # generate random locations for start/end
    # generate random locations for enemies
    quicksand = random.choice(CELLS)
    pit = random.choice(CELLS)
    crocodiles = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    # if any of these equal each other, generate locations again
    if quicksand == door or quicksand == start or door == start or pit == start or pit == door \
            or crocodiles == start or crocodiles == door:
        return generate_locations()

    return quicksand, pit, crocodiles, door, start


def move_player(player, move):
    x, y = player

    # define player movements with grid movements
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x, y


def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    # if the player is against the left wall
    if player[1] == 0:
        moves.remove('LEFT')
    # if the player is against the right wall
    if player[1] == 3:
        moves.remove('RIGHT')
    # if the player is against the top wall
    if player[0] == 0:
        moves.remove('UP')
    # if the player is against the bottom wall
    if player[0] == 5:
        moves.remove('DOWN')

    return moves


def draw_map(player):
    # draw the top wall
    print(' _ _ _ _ ')
    tile = '|{}'

    # draw an x tile for the player location
    for idx, cell in enumerate(CELLS):
        # if the player index is in the left or middle cells
        if idx in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))


def game():
    reset = True
    quicksand, pit, crocodiles, door, player = generate_locations()

    print("You walk deeper into the jungle and discover ancient ruins covered in vines."
          "\nYou walk up to the door and see a sign that reads: ")

    user_name = input("Hello, what is your name? ")

    print("Welcome to the Temple of Doom, " + user_name + "!")
    print("\nUnfortunately, you've fallen through a trap door and into pitch black darkness."
          "\nIf you can dodge quicksand, a bottomless pit, and hungry crocodiles to find the "
          "\nescape rope, you can still survive. Good luck and watch your step!\n")

    while True:
        moves = get_moves(player)

        print("You're currently in room {}".format(player))

        draw_map(player)

        print("\nYou can move {}".format(moves))
        print("Enter 'QUIT' if you give up.")
        print("Which way will you go?")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print("\nInstead of dying a quick death, you choose to lie down in fear and die "
                  "of starvation in the dark. Nice one. \nGAME OVER")
            break

        if move in moves:
            player = move_player(player, move)
            print("\nHmm, nothing here.\n")
        else:
            print("\nYou reach out your hands and touch the wall. Can't go this way.\n")
            continue

        if player == door:
            print("\nYou grab a hold of the escape rope, and pull yourself to freedom! \nCONGRATULATIONS!")
            break
        elif player == quicksand:
            print("\n*squish* Oh no, you've stepped in quicksand. You slowly sink to your death. \nGAME OVER")
            break
        elif player == pit:
            print("WAAAHHHH! You fall down a bottomless pit. It seemed cooler in Spy Kids. \nGAME OVER")
            break
        elif player == crocodiles:
            print("CHOMP! Too bad you aren't Indiana Jones or you might have swung miraculously over "
                  "that pit of crocodiles. \nGAME OVER")
            break

    while reset:
        play_again = (input("\nWould you like to play again? y/n ").lower())
        if play_again == 'y':
            reset = False
            game()
        elif play_again == 'n':
            reset = False
            print("Til next time.")
        elif play_again != 'y' or 'n':
            print("Whoops, {} is not an accepted value. Type 'y' for YES or 'n' for NO. ".format(play_again))

game()
