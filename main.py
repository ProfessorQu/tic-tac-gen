print(" |X| \n------\n | | \n------\n | | ")
move = input("move: ")
if move == "9":
    print(" |X|X\n------\n | | \n------\n | |O")
    move = input("move: ")
    if move == "7":
        print(" |X|X\n------\n | | \n------\nO|X|O")
        move = input("move: ")
        if move == "5":
            print("X|X|X\n------\n |O| \n------\nO|X|O")
            print("result: X Won")
        elif move == "4":
            print("X|X|X\n------\nO| | \n------\nO|X|O")
            print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\n |X| \n------\nO|X|O")
            print("result: X Won")
        elif move == "6":
            print(" |X|X\n------\nX| |O\n------\nO|X|O")
            move = input("move: ")
            if move == "1":
                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                print("result: X Won")
            elif move == "5":
                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                print("result: X Won")
    elif move == "5":
        print("X|X|X\n------\n |O| \n------\n | |O")
        print("result: X Won")
    elif move == "8":
        print(" |X|X\n------\n | | \n------\nX|O|O")
        move = input("move: ")
        if move == "4":
            print("X|X|X\n------\nO| | \n------\nX|O|O")
            print("result: X Won")
        elif move == "5":
            print("X|X|X\n------\n |O| \n------\nX|O|O")
            print("result: X Won")
        elif move == "6":
            print("X|X|X\n------\n | |O\n------\nX|O|O")
            print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\n |X| \n------\nX|O|O")
            print("result: X Won")
    elif move == "1":
        print("O|X|X\n------\n |X| \n------\n | |O")
        move = input("move: ")
        if move == "6":
            print("O|X|X\n------\nX|X|O\n------\n | |O")
            move = input("move: ")
            if move == "7":
                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                print("result: X Won")
            elif move == "8":
                print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                print("result: X Won")
        elif move == "7":
            print("O|X|X\n------\n |X| \n------\nO|X|O")
            print("result: X Won")
        elif move == "8":
            print("O|X|X\n------\n |X| \n------\nX|O|O")
            print("result: X Won")
        elif move == "4":
            print("O|X|X\n------\nO|X| \n------\n |X|O")
            print("result: X Won")
    elif move == "4":
        print(" |X|X\n------\nO|X| \n------\n | |O")
        move = input("move: ")
        if move == "7":
            print(" |X|X\n------\nO|X| \n------\nO|X|O")
            print("result: X Won")
        elif move == "6":
            print(" |X|X\n------\nO|X|O\n------\nX| |O")
            print("result: X Won")
        elif move == "8":
            print("X|X|X\n------\nO|X| \n------\n |O|O")
            print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\nO|X| \n------\n |X|O")
            print("result: X Won")
    elif move == "6":
        print("X|X|X\n------\n | |O\n------\n | |O")
        print("result: X Won")
elif move == "3":
    print(" |X|O\n------\n | |X\n------\n | | ")
    move = input("move: ")
    if move == "4":
        print(" |X|O\n------\nO|X|X\n------\n | | ")
        move = input("move: ")
        if move == "8":
            print(" |X|O\n------\nO|X|X\n------\n |O|X")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                print("result: Draw")
            elif move == "7":
                print("X|X|O\n------\nO|X|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "1":
            print("O|X|O\n------\nO|X|X\n------\n |X| ")
            print("result: X Won")
        elif move == "9":
            print(" |X|O\n------\nO|X|X\n------\n |X|O")
            print("result: X Won")
        elif move == "7":
            print("X|X|O\n------\nO|X|X\n------\nO| | ")
            move = input("move: ")
            if move == "9":
                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                print("result: X Won")
            elif move == "8":
                print("X|X|O\n------\nO|X|X\n------\nO|O|X")
                print("result: X Won")
    elif move == "7":
        print(" |X|O\n------\n |X|X\n------\nO| | ")
        move = input("move: ")
        if move == "1":
            print("O|X|O\n------\nX|X|X\n------\nO| | ")
            print("result: X Won")
        elif move == "8":
            print(" |X|O\n------\n |X|X\n------\nO|O|X")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nO|X|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "9":
            print(" |X|O\n------\nX|X|X\n------\nO| |O")
            print("result: X Won")
        elif move == "4":
            print(" |X|O\n------\nO|X|X\n------\nO|X| ")
            print("result: X Won")
    elif move == "8":
        print(" |X|O\n------\nX| |X\n------\n |O| ")
        move = input("move: ")
        if move == "5":
            print(" |X|O\n------\nX|O|X\n------\nX|O| ")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
            elif move == "9":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
        elif move == "7":
            print(" |X|O\n------\nX|X|X\n------\nO|O| ")
            print("result: X Won")
        elif move == "9":
            print(" |X|O\n------\nX| |X\n------\nX|O|O")
            move = input("move: ")
            if move == "5":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                print("result: X Won")
        elif move == "1":
            print("O|X|O\n------\nX|X|X\n------\n |O| ")
            print("result: X Won")
    elif move == "1":
        print("O|X|O\n------\n |X|X\n------\n | | ")
        move = input("move: ")
        if move == "8":
            print("O|X|O\n------\nX|X|X\n------\n |O| ")
            print("result: X Won")
        elif move == "4":
            print("O|X|O\n------\nO|X|X\n------\n |X| ")
            print("result: X Won")
        elif move == "9":
            print("O|X|O\n------\n |X|X\n------\n |X|O")
            print("result: X Won")
        elif move == "7":
            print("O|X|O\n------\nX|X|X\n------\nO| | ")
            print("result: X Won")
    elif move == "5":
        print(" |X|O\n------\n |O|X\n------\nX| | ")
        move = input("move: ")
        if move == "9":
            print("X|X|O\n------\n |O|X\n------\nX| |O")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                print("result: Draw")
            elif move == "8":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
        elif move == "1":
            print("O|X|O\n------\n |O|X\n------\nX| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
            elif move == "4":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
        elif move == "4":
            print(" |X|O\n------\nO|O|X\n------\nX| |X")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                print("result: Draw")
        elif move == "8":
            print(" |X|O\n------\nX|O|X\n------\nX|O| ")
            move = input("move: ")
            if move == "9":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
    elif move == "9":
        print(" |X|O\n------\n |X|X\n------\n | |O")
        move = input("move: ")
        if move == "1":
            print("O|X|O\n------\n |X|X\n------\n |X|O")
            print("result: X Won")
        elif move == "4":
            print(" |X|O\n------\nO|X|X\n------\n |X|O")
            print("result: X Won")
        elif move == "8":
            print(" |X|O\n------\nX|X|X\n------\n |O|O")
            print("result: X Won")
        elif move == "7":
            print(" |X|O\n------\nX|X|X\n------\nO| |O")
            print("result: X Won")
elif move == "6":
    print(" |X|X\n------\n | |O\n------\n | | ")
    move = input("move: ")
    if move == "1":
        print("O|X|X\n------\n |X|O\n------\n | | ")
        move = input("move: ")
        if move == "9":
            print("O|X|X\n------\n |X|O\n------\nX| |O")
            print("result: X Won")
        elif move == "4":
            print("O|X|X\n------\nO|X|O\n------\nX| | ")
            print("result: X Won")
        elif move == "7":
            print("O|X|X\n------\n |X|O\n------\nO|X| ")
            print("result: X Won")
        elif move == "8":
            print("O|X|X\n------\n |X|O\n------\nX|O| ")
            print("result: X Won")
    elif move == "8":
        print(" |X|X\n------\n | |O\n------\nX|O| ")
        move = input("move: ")
        if move == "4":
            print("X|X|X\n------\nO| |O\n------\nX|O| ")
            print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\n |X|O\n------\nX|O| ")
            print("result: X Won")
        elif move == "9":
            print(" |X|X\n------\nX| |O\n------\nX|O|O")
            move = input("move: ")
            if move == "5":
                print("X|X|X\n------\nX|O|O\n------\nX|O|O")
                print("result: X Won")
            elif move == "1":
                print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                print("result: X Won")
        elif move == "5":
            print("X|X|X\n------\n |O|O\n------\nX|O| ")
            print("result: X Won")
    elif move == "4":
        print("X|X|X\n------\nO| |O\n------\n | | ")
        print("result: X Won")
    elif move == "9":
        print(" |X|X\n------\n | |O\n------\nX| |O")
        move = input("move: ")
        if move == "5":
            print("X|X|X\n------\n |O|O\n------\nX| |O")
            print("result: X Won")
        elif move == "8":
            print("X|X|X\n------\n | |O\n------\nX|O|O")
            print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\n |X|O\n------\nX| |O")
            print("result: X Won")
        elif move == "4":
            print(" |X|X\n------\nO|X|O\n------\nX| |O")
            print("result: X Won")
    elif move == "5":
        print("X|X|X\n------\n |O|O\n------\n | | ")
        print("result: X Won")
    elif move == "7":
        print("X|X|X\n------\n | |O\n------\nO| | ")
        print("result: X Won")
elif move == "1":
    print("O|X| \n------\n | | \n------\n | |X")
    move = input("move: ")
    if move == "4":
        print("O|X| \n------\nO| | \n------\nX| |X")
        move = input("move: ")
        if move == "8":
            print("O|X|X\n------\nO| | \n------\nX|O|X")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nO|X|O\n------\nX|O|X")
                print("result: X Won")
            elif move == "5":
                print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                print("result: X Won")
        elif move == "6":
            print("O|X| \n------\nO| |O\n------\nX|X|X")
            print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\nO| | \n------\nX|X|X")
            print("result: X Won")
        elif move == "5":
            print("O|X| \n------\nO|O|X\n------\nX| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
    elif move == "3":
        print("O|X|O\n------\n | | \n------\n |X|X")
        move = input("move: ")
        if move == "7":
            print("O|X|O\n------\n |X| \n------\nO|X|X")
            print("result: X Won")
        elif move == "4":
            print("O|X|O\n------\nO| | \n------\nX|X|X")
            print("result: X Won")
        elif move == "6":
            print("O|X|O\n------\n |X|O\n------\n |X|X")
            print("result: X Won")
        elif move == "5":
            print("O|X|O\n------\n |O| \n------\nX|X|X")
            print("result: X Won")
    elif move == "6":
        print("O|X| \n------\n | |O\n------\n |X|X")
        move = input("move: ")
        if move == "3":
            print("O|X|O\n------\nX| |O\n------\n |X|X")
            move = input("move: ")
            if move == "5":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "7":
                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                print("result: X Won")
        elif move == "5":
            print("O|X| \n------\n |O|O\n------\nX|X|X")
            print("result: X Won")
        elif move == "4":
            print("O|X| \n------\nO|X|O\n------\n |X|X")
            print("result: X Won")
        elif move == "7":
            print("O|X| \n------\n |X|O\n------\nO|X|X")
            print("result: X Won")
    elif move == "8":
        print("O|X| \n------\n | |X\n------\n |O|X")
        move = input("move: ")
        if move == "4":
            print("O|X|X\n------\nO| |X\n------\n |O|X")
            print("result: X Won")
        elif move == "7":
            print("O|X|X\n------\n | |X\n------\nO|O|X")
            print("result: X Won")
        elif move == "5":
            print("O|X|X\n------\n |O|X\n------\n |O|X")
            print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\nX| |X\n------\n |O|X")
            move = input("move: ")
            if move == "5":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
    elif move == "5":
        print("O|X| \n------\nX|O| \n------\n | |X")
        move = input("move: ")
        if move == "3":
            print("O|X|O\n------\nX|O| \n------\nX| |X")
            move = input("move: ")
            if move == "6":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
        elif move == "7":
            print("O|X|X\n------\nX|O| \n------\nO| |X")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                print("result: Draw")
            elif move == "8":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "6":
            print("O|X| \n------\nX|O|O\n------\nX| |X")
            move = input("move: ")
            if move == "3":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                print("result: Draw")
        elif move == "8":
            print("O|X|X\n------\nX|O| \n------\n |O|X")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                print("result: Draw")
            elif move == "7":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
    elif move == "7":
        print("O|X| \n------\nX| | \n------\nO| |X")
        move = input("move: ")
        if move == "8":
            print("O|X| \n------\nX| |X\n------\nO|O|X")
            move = input("move: ")
            if move == "5":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\nX|X| \n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "6":
                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                print("result: X Won")
        elif move == "5":
            print("O|X|X\n------\nX|O| \n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "6":
                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                print("result: Draw")
        elif move == "6":
            print("O|X| \n------\nX|X|O\n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                print("result: Draw")
            elif move == "3":
                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                print("result: X Won")
elif move == "7":
    print("X|X| \n------\n | | \n------\nO| | ")
    move = input("move: ")
    if move == "4":
        print("X|X| \n------\nO|X| \n------\nO| | ")
        move = input("move: ")
        if move == "8":
            print("X|X|X\n------\nO|X| \n------\nO|O| ")
            print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\nO|X| \n------\nO| |X")
            print("result: X Won")
        elif move == "6":
            print("X|X|X\n------\nO|X|O\n------\nO| | ")
            print("result: X Won")
        elif move == "9":
            print("X|X| \n------\nO|X| \n------\nO|X|O")
            print("result: X Won")
    elif move == "3":
        print("X|X|O\n------\n |X| \n------\nO| | ")
        move = input("move: ")
        if move == "4":
            print("X|X|O\n------\nO|X| \n------\nO|X| ")
            print("result: X Won")
        elif move == "8":
            print("X|X|O\n------\n |X| \n------\nO|O|X")
            print("result: X Won")
        elif move == "6":
            print("X|X|O\n------\n |X|O\n------\nO| |X")
            print("result: X Won")
        elif move == "9":
            print("X|X|O\n------\n |X| \n------\nO|X|O")
            print("result: X Won")
    elif move == "5":
        print("X|X|X\n------\n |O| \n------\nO| | ")
        print("result: X Won")
    elif move == "6":
        print("X|X| \n------\n |X|O\n------\nO| | ")
        move = input("move: ")
        if move == "4":
            print("X|X| \n------\nO|X|O\n------\nO|X| ")
            print("result: X Won")
        elif move == "9":
            print("X|X| \n------\n |X|O\n------\nO|X|O")
            print("result: X Won")
        elif move == "8":
            print("X|X|X\n------\n |X|O\n------\nO|O| ")
            print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\n |X|O\n------\nO| |X")
            print("result: X Won")
    elif move == "9":
        print("X|X|X\n------\n | | \n------\nO| |O")
        print("result: X Won")
    elif move == "8":
        print("X|X| \n------\n | | \n------\nO|O|X")
        move = input("move: ")
        if move == "6":
            print("X|X| \n------\nX| |O\n------\nO|O|X")
            move = input("move: ")
            if move == "5":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "3":
                print("X|X|O\n------\nX|X|O\n------\nO|O|X")
                print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\n |X| \n------\nO|O|X")
            print("result: X Won")
        elif move == "4":
            print("X|X|X\n------\nO| | \n------\nO|O|X")
            print("result: X Won")
        elif move == "5":
            print("X|X|X\n------\n |O| \n------\nO|O|X")
            print("result: X Won")
elif move == "4":
    print(" |X| \n------\nO|X| \n------\n | | ")
    move = input("move: ")
    if move == "3":
        print("X|X|O\n------\nO|X| \n------\n | | ")
        move = input("move: ")
        if move == "9":
            print("X|X|O\n------\nO|X| \n------\n |X|O")
            print("result: X Won")
        elif move == "8":
            print("X|X|O\n------\nO|X| \n------\n |O|X")
            print("result: X Won")
        elif move == "7":
            print("X|X|O\n------\nO|X| \n------\nO|X| ")
            print("result: X Won")
        elif move == "6":
            print("X|X|O\n------\nO|X|O\n------\n |X| ")
            print("result: X Won")
    elif move == "7":
        print("X|X| \n------\nO|X| \n------\nO| | ")
        move = input("move: ")
        if move == "8":
            print("X|X|X\n------\nO|X| \n------\nO|O| ")
            print("result: X Won")
        elif move == "6":
            print("X|X| \n------\nO|X|O\n------\nO|X| ")
            print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\nO|X| \n------\nO|X| ")
            print("result: X Won")
        elif move == "9":
            print("X|X| \n------\nO|X| \n------\nO|X|O")
            print("result: X Won")
    elif move == "6":
        print(" |X| \n------\nO|X|O\n------\n | |X")
        move = input("move: ")
        if move == "7":
            print(" |X| \n------\nO|X|O\n------\nO|X|X")
            print("result: X Won")
        elif move == "1":
            print("O|X| \n------\nO|X|O\n------\nX| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nO|X|O\n------\nX|O|X")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nO|X|O\n------\nX|X|X")
                print("result: X Won")
        elif move == "3":
            print(" |X|O\n------\nO|X|O\n------\n |X|X")
            print("result: X Won")
        elif move == "8":
            print(" |X| \n------\nO|X|O\n------\nX|O|X")
            move = input("move: ")
            if move == "1":
                print("O|X|X\n------\nO|X|O\n------\nX|O|X")
                print("result: X Won")
            elif move == "3":
                print("X|X|O\n------\nO|X|O\n------\nX|O|X")
                print("result: X Won")
    elif move == "8":
        print("X|X| \n------\nO|X| \n------\n |O| ")
        move = input("move: ")
        if move == "9":
            print("X|X|X\n------\nO|X| \n------\n |O|O")
            print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\nO|X| \n------\n |O|X")
            print("result: X Won")
        elif move == "7":
            print("X|X| \n------\nO|X| \n------\nO|O|X")
            print("result: X Won")
        elif move == "6":
            print("X|X| \n------\nO|X|O\n------\n |O|X")
            print("result: X Won")
    elif move == "9":
        print(" |X| \n------\nO|X| \n------\nX| |O")
        move = input("move: ")
        if move == "8":
            print(" |X|X\n------\nO|X| \n------\nX|O|O")
            print("result: X Won")
        elif move == "3":
            print(" |X|O\n------\nO|X| \n------\nX|X|O")
            print("result: X Won")
        elif move == "6":
            print(" |X|X\n------\nO|X|O\n------\nX| |O")
            print("result: X Won")
        elif move == "1":
            print("O|X| \n------\nO|X|X\n------\nX| |O")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nO|X|X\n------\nX|O|O")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                print("result: X Won")
    elif move == "1":
        print("O|X| \n------\nO|X| \n------\nX| | ")
        move = input("move: ")
        if move == "6":
            print("O|X|X\n------\nO|X|O\n------\nX| | ")
            print("result: X Won")
        elif move == "8":
            print("O|X|X\n------\nO|X| \n------\nX|O| ")
            print("result: X Won")
        elif move == "9":
            print("O|X| \n------\nO|X| \n------\nX|X|O")
            print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\nO|X| \n------\nX|X| ")
            print("result: X Won")
elif move == "5":
    print(" |X| \n------\n |O| \n------\n | |X")
    move = input("move: ")
    if move == "8":
        print(" |X|X\n------\n |O| \n------\n |O|X")
        move = input("move: ")
        if move == "1":
            print("O|X|X\n------\n |O|X\n------\n |O|X")
            print("result: X Won")
        elif move == "7":
            print("X|X|X\n------\n |O| \n------\nO|O|X")
            print("result: X Won")
        elif move == "4":
            print("X|X|X\n------\nO|O| \n------\n |O|X")
            print("result: X Won")
        elif move == "6":
            print("X|X|X\n------\n |O|O\n------\n |O|X")
            print("result: X Won")
    elif move == "4":
        print(" |X| \n------\nO|O|X\n------\n | |X")
        move = input("move: ")
        if move == "1":
            print("O|X| \n------\nO|O|X\n------\nX| |X")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
        elif move == "8":
            print(" |X|X\n------\nO|O|X\n------\n |O|X")
            print("result: X Won")
        elif move == "7":
            print(" |X|X\n------\nO|O|X\n------\nO| |X")
            print("result: X Won")
        elif move == "3":
            print(" |X|O\n------\nO|O|X\n------\nX| |X")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                print("result: Draw")
    elif move == "1":
        print("O|X| \n------\n |O| \n------\nX| |X")
        move = input("move: ")
        if move == "6":
            print("O|X| \n------\n |O|O\n------\nX|X|X")
            print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\n |O| \n------\nX|X|X")
            print("result: X Won")
        elif move == "8":
            print("O|X|X\n------\n |O| \n------\nX|O|X")
            move = input("move: ")
            if move == "4":
                print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                print("result: X Won")
            elif move == "6":
                print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                print("result: Draw")
        elif move == "4":
            print("O|X| \n------\nO|O|X\n------\nX| |X")
            move = input("move: ")
            if move == "3":
                print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                print("result: X Won")
    elif move == "3":
        print(" |X|O\n------\n |O| \n------\nX| |X")
        move = input("move: ")
        if move == "1":
            print("O|X|O\n------\n |O| \n------\nX|X|X")
            print("result: X Won")
        elif move == "8":
            print("X|X|O\n------\n |O| \n------\nX|O|X")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                print("result: Draw")
            elif move == "6":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
        elif move == "4":
            print(" |X|O\n------\nO|O| \n------\nX|X|X")
            print("result: X Won")
        elif move == "6":
            print(" |X|O\n------\nX|O|O\n------\nX| |X")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
    elif move == "7":
        print(" |X|X\n------\n |O| \n------\nO| |X")
        move = input("move: ")
        if move == "6":
            print("X|X|X\n------\n |O|O\n------\nO| |X")
            print("result: X Won")
        elif move == "8":
            print(" |X|X\n------\nX|O| \n------\nO|O|X")
            move = input("move: ")
            if move == "1":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "6":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
        elif move == "1":
            print("O|X|X\n------\n |O|X\n------\nO| |X")
            print("result: X Won")
        elif move == "4":
            print(" |X|X\n------\nO|O|X\n------\nO| |X")
            print("result: X Won")
    elif move == "6":
        print(" |X| \n------\nX|O|O\n------\n | |X")
        move = input("move: ")
        if move == "7":
            print(" |X|X\n------\nX|O|O\n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "1":
                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                print("result: Draw")
        elif move == "8":
            print("X|X| \n------\nX|O|O\n------\n |O|X")
            move = input("move: ")
            if move == "3":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
            elif move == "7":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
        elif move == "1":
            print("O|X| \n------\nX|O|O\n------\nX| |X")
            move = input("move: ")
            if move == "3":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                print("result: Draw")
        elif move == "3":
            print(" |X|O\n------\nX|O|O\n------\nX| |X")
            move = input("move: ")
            if move == "1":
                print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                print("result: X Won")
            elif move == "8":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
elif move == "8":
    print(" |X| \n------\nX| | \n------\n |O| ")
    move = input("move: ")
    if move == "1":
        print("O|X| \n------\nX| |X\n------\n |O| ")
        move = input("move: ")
        if move == "5":
            print("O|X| \n------\nX|O|X\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
        elif move == "7":
            print("O|X| \n------\nX|X|X\n------\nO|O| ")
            print("result: X Won")
        elif move == "3":
            print("O|X|O\n------\nX|X|X\n------\n |O| ")
            print("result: X Won")
        elif move == "9":
            print("O|X| \n------\nX|X|X\n------\n |O|O")
            print("result: X Won")
    elif move == "7":
        print(" |X| \n------\nX| | \n------\nO|O|X")
        move = input("move: ")
        if move == "3":
            print(" |X|O\n------\nX|X| \n------\nO|O|X")
            move = input("move: ")
            if move == "6":
                print("X|X|O\n------\nX|X|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "5":
            print(" |X|X\n------\nX|O| \n------\nO|O|X")
            move = input("move: ")
            if move == "6":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "1":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
        elif move == "6":
            print("X|X| \n------\nX| |O\n------\nO|O|X")
            move = input("move: ")
            if move == "5":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "3":
                print("X|X|O\n------\nX|X|O\n------\nO|O|X")
                print("result: X Won")
        elif move == "1":
            print("O|X| \n------\nX| |X\n------\nO|O|X")
            move = input("move: ")
            if move == "3":
                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                print("result: X Won")
            elif move == "5":
                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                print("result: X Won")
    elif move == "3":
        print(" |X|O\n------\nX| |X\n------\n |O| ")
        move = input("move: ")
        if move == "1":
            print("O|X|O\n------\nX|X|X\n------\n |O| ")
            print("result: X Won")
        elif move == "7":
            print(" |X|O\n------\nX|X|X\n------\nO|O| ")
            print("result: X Won")
        elif move == "9":
            print(" |X|O\n------\nX| |X\n------\nX|O|O")
            move = input("move: ")
            if move == "5":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                print("result: X Won")
        elif move == "5":
            print(" |X|O\n------\nX|O|X\n------\nX|O| ")
            move = input("move: ")
            if move == "9":
                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                print("result: X Won")
            elif move == "1":
                print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                print("result: Draw")
    elif move == "9":
        print(" |X| \n------\nX| | \n------\nX|O|O")
        move = input("move: ")
        if move == "5":
            print("X|X| \n------\nX|O| \n------\nX|O|O")
            print("result: X Won")
        elif move == "1":
            print("O|X| \n------\nX|X| \n------\nX|O|O")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                print("result: X Won")
            elif move == "3":
                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                print("result: X Won")
        elif move == "3":
            print("X|X|O\n------\nX| | \n------\nX|O|O")
            print("result: X Won")
        elif move == "6":
            print(" |X|X\n------\nX| |O\n------\nX|O|O")
            move = input("move: ")
            if move == "1":
                print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                print("result: X Won")
            elif move == "5":
                print("X|X|X\n------\nX|O|O\n------\nX|O|O")
                print("result: X Won")
    elif move == "5":
        print("X|X| \n------\nX|O| \n------\n |O| ")
        move = input("move: ")
        if move == "3":
            print("X|X|O\n------\nX|O| \n------\nX|O| ")
            print("result: X Won")
        elif move == "6":
            print("X|X| \n------\nX|O|O\n------\nX|O| ")
            print("result: X Won")
        elif move == "9":
            print("X|X|X\n------\nX|O| \n------\n |O|O")
            print("result: X Won")
        elif move == "7":
            print("X|X|X\n------\nX|O| \n------\nO|O| ")
            print("result: X Won")
    elif move == "6":
        print("X|X| \n------\nX| |O\n------\n |O| ")
        move = input("move: ")
        if move == "3":
            print("X|X|O\n------\nX| |O\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("X|X|O\n------\nX|X|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "5":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
        elif move == "9":
            print("X|X| \n------\nX| |O\n------\nX|O|O")
            print("result: X Won")
        elif move == "5":
            print("X|X| \n------\nX|O|O\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                print("result: X Won")
            elif move == "3":
                print("X|X|O\n------\nX|O|O\n------\nX|O|X")
                print("result: X Won")
        elif move == "7":
            print("X|X|X\n------\nX| |O\n------\nO|O| ")
            print("result: X Won")
