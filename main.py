print(" | | \n------\n | | \n------\n | | ")
move = input("move: ")
if move == "7":
    print(" | | \n------\n |O| \n------\nX| | ")
    move = input("move: ")
    if move == "1":
        print("X| | \n------\nO|O| \n------\nX| | ")
        move = input("move: ")
        if move == "2":
            print("X|X| \n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
        elif move == "8":
            print("X| | \n------\nO|O|O\n------\nX|X| ")
            print("result: O Won")
        elif move == "3":
            print("X| |X\n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
        elif move == "9":
            print("X| | \n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
        elif move == "6":
            print("X| | \n------\nO|O|X\n------\nX| |O")
            move = input("move: ")
            if move == "8":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "3":
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
    elif move == "2":
        print(" |X| \n------\nO|O| \n------\nX| | ")
        move = input("move: ")
        if move == "8":
            print(" |X| \n------\nO|O|O\n------\nX|X| ")
            print("result: O Won")
        elif move == "6":
            print(" |X|O\n------\nO|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "1":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "1":
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "8":
                print(" |X|O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "1":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "1":
            print("X|X| \n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "8":
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
        elif move == "9":
            print(" |X| \n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
    elif move == "4":
        print("O| | \n------\nX|O| \n------\nX| | ")
        move = input("move: ")
        if move == "9":
            print("O| | \n------\nX|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "6":
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                move = input("move: ")
                if move == "6":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
                print("result: O Won")
        elif move == "8":
            print("O| | \n------\nX|O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "3":
            print("O| |X\n------\nX|O| \n------\nX| |O")
            print("result: O Won")
        elif move == "2":
            print("O|X| \n------\nX|O| \n------\nX| |O")
            print("result: O Won")
        elif move == "6":
            print("O| |O\n------\nX|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "8":
                print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
    elif move == "8":
        print(" | | \n------\n |O| \n------\nX|X|O")
        move = input("move: ")
        if move == "2":
            print(" |X| \n------\n |O|O\n------\nX|X|O")
            move = input("move: ")
            if move == "3":
                print(" |X|X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "4":
                print("O|X| \n------\nX|O|O\n------\nX|X|O")
                print("result: O Won")
        elif move == "4":
            print("O| | \n------\nX|O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "6":
            print("O| | \n------\n |O|X\n------\nX|X|O")
            print("result: O Won")
        elif move == "1":
            print("X| | \n------\nO|O| \n------\nX|X|O")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "3":
            print("O| |X\n------\n |O| \n------\nX|X|O")
            print("result: O Won")
    elif move == "3":
        print(" | |X\n------\n |O| \n------\nX|O| ")
        move = input("move: ")
        if move == "6":
            print(" | |X\n------\n |O|X\n------\nX|O|O")
            move = input("move: ")
            if move == "1":
                print("X|O|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "4":
                print("O| |X\n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
        elif move == "9":
            print(" |O|X\n------\n |O| \n------\nX|O|X")
            print("result: O Won")
        elif move == "4":
            print("O| |X\n------\nX|O| \n------\nX|O| ")
            move = input("move: ")
            if move == "9":
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
                print("result: O Won")
            elif move == "6":
                print("O| |X\n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
        elif move == "1":
            print("X|O|X\n------\n |O| \n------\nX|O| ")
            print("result: O Won")
        elif move == "2":
            print("O|X|X\n------\n |O| \n------\nX|O| ")
            move = input("move: ")
            if move == "4":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
    elif move == "6":
        print(" | |O\n------\n |O|X\n------\nX| | ")
        move = input("move: ")
        if move == "4":
            print("O| |O\n------\nX|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "8":
                print("O| |O\n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
        elif move == "8":
            print(" | |O\n------\n |O|X\n------\nX|X|O")
            move = input("move: ")
            if move == "2":
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "4":
                print("O| |O\n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "1":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "9":
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            move = input("move: ")
            if move == "1":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "4":
                print(" |O|O\n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "1":
            print("X| |O\n------\nO|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "8":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "9":
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "2":
            print(" |X|O\n------\n |O|X\n------\nX|O| ")
            move = input("move: ")
            if move == "9":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "1":
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
    elif move == "9":
        print(" | | \n------\n |O| \n------\nX|O|X")
        move = input("move: ")
        if move == "2":
            print(" |X| \n------\nO|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "1":
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "3":
                print(" |X|X\n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "6":
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "1":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "4":
            print(" |O| \n------\nX|O| \n------\nX|O|X")
            print("result: O Won")
        elif move == "1":
            print("X| | \n------\nO|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "3":
                print("X| |X\n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "6":
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
        elif move == "3":
            print(" |O|X\n------\n |O| \n------\nX|O|X")
            print("result: O Won")
        elif move == "6":
            print(" |O| \n------\n |O|X\n------\nX|O|X")
            print("result: O Won")
elif move == "6":
    print(" | | \n------\n |O|X\n------\n | | ")
    move = input("move: ")
    if move == "8":
        print(" | | \n------\n |O|X\n------\nO|X| ")
        move = input("move: ")
        if move == "1":
            print("X| |O\n------\n |O|X\n------\nO|X| ")
            print("result: O Won")
        elif move == "2":
            print("O|X| \n------\n |O|X\n------\nO|X| ")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "4":
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|X| \n------\nO|O|X\n------\nO|X|X")
                print("result: O Won")
        elif move == "3":
            print(" | |X\n------\n |O|X\n------\nO|X|O")
            move = input("move: ")
            if move == "4":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "4":
            print("O| | \n------\nX|O|X\n------\nO|X| ")
            move = input("move: ")
            if move == "3":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "9":
                print("O| |O\n------\nX|O|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
        elif move == "9":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
    elif move == "3":
        print(" | |X\n------\n |O|X\n------\n | |O")
        move = input("move: ")
        if move == "8":
            print("O| |X\n------\n |O|X\n------\n |X|O")
            print("result: O Won")
        elif move == "1":
            print("X|O|X\n------\n |O|X\n------\n | |O")
            move = input("move: ")
            if move == "8":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "4":
                print("X|O|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
            elif move == "7":
                print("X|O|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
        elif move == "4":
            print(" | |X\n------\nX|O|X\n------\nO| |O")
            move = input("move: ")
            if move == "2":
                print(" |X|X\n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "8":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "1":
                print("X| |X\n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
        elif move == "7":
            print(" |O|X\n------\n |O|X\n------\nX| |O")
            move = input("move: ")
            if move == "1":
                print("X|O|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "4":
                print(" |O|X\n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "8":
                print("O|O|X\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "2":
            print("O|X|X\n------\n |O|X\n------\n | |O")
            print("result: O Won")
    elif move == "9":
        print(" | |O\n------\n |O|X\n------\n | |X")
        move = input("move: ")
        if move == "1":
            print("X| |O\n------\n |O|X\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "4":
                print("X| |O\n------\nX|O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
        elif move == "7":
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            move = input("move: ")
            if move == "1":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "4":
                print(" |O|O\n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "4":
            print("O| |O\n------\nX|O|X\n------\n | |X")
            move = input("move: ")
            if move == "2":
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "7":
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("O| |O\n------\nX|O|X\n------\nO|X|X")
                print("result: O Won")
        elif move == "8":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
        elif move == "2":
            print(" |X|O\n------\n |O|X\n------\nO| |X")
            print("result: O Won")
    elif move == "1":
        print("X| | \n------\n |O|X\n------\n |O| ")
        move = input("move: ")
        if move == "3":
            print("X|O|X\n------\n |O|X\n------\n |O| ")
            print("result: O Won")
        elif move == "4":
            print("X| | \n------\nX|O|X\n------\nO|O| ")
            move = input("move: ")
            if move == "9":
                print("X| |O\n------\nX|O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X|O\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
        elif move == "9":
            print("X| |O\n------\n |O|X\n------\n |O|X")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "4":
                print("X| |O\n------\nX|O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "7":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
        elif move == "2":
            print("X|X|O\n------\n |O|X\n------\n |O| ")
            move = input("move: ")
            if move == "7":
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("X|X|O\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "9":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
        elif move == "7":
            print("X|O| \n------\n |O|X\n------\nX|O| ")
            print("result: O Won")
    elif move == "4":
        print(" | | \n------\nX|O|X\n------\n | |O")
        move = input("move: ")
        if move == "7":
            print("O| | \n------\nX|O|X\n------\nX| |O")
            print("result: O Won")
        elif move == "2":
            print("O|X| \n------\nX|O|X\n------\n | |O")
            print("result: O Won")
        elif move == "3":
            print(" | |X\n------\nX|O|X\n------\n |O|O")
            move = input("move: ")
            if move == "7":
                print(" |O|X\n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "2":
                print(" |X|X\n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "1":
                print("X| |X\n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
        elif move == "1":
            print("X| | \n------\nX|O|X\n------\nO| |O")
            move = input("move: ")
            if move == "8":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "2":
                print("X|X| \n------\nX|O|X\n------\nO|O|O")
                print("result: O Won")
        elif move == "8":
            print(" | | \n------\nX|O|X\n------\nO|X|O")
            move = input("move: ")
            if move == "3":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "1":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "2":
                print("O|X| \n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
    elif move == "7":
        print(" |O| \n------\n |O|X\n------\nX| | ")
        move = input("move: ")
        if move == "4":
            print("O|O| \n------\nX|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "3":
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                print("result: O Won")
            elif move == "9":
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "8":
                print("O|O| \n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "1":
            print("X|O| \n------\n |O|X\n------\nX|O| ")
            print("result: O Won")
        elif move == "8":
            print(" |O| \n------\n |O|X\n------\nX|X|O")
            move = input("move: ")
            if move == "4":
                print("O|O| \n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "3":
                print("O|O|X\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "1":
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "9":
            print(" |O| \n------\n |O|X\n------\nX|O|X")
            print("result: O Won")
        elif move == "3":
            print(" |O|X\n------\n |O|X\n------\nX| |O")
            move = input("move: ")
            if move == "4":
                print("O|O|X\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "8":
                print("O|O|X\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
    elif move == "2":
        print("O|X| \n------\n |O|X\n------\n | | ")
        move = input("move: ")
        if move == "7":
            print("O|X| \n------\n |O|X\n------\nX| |O")
            print("result: O Won")
        elif move == "8":
            print("O|X|O\n------\n |O|X\n------\n |X| ")
            move = input("move: ")
            if move == "4":
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|O\n------\n |O|X\n------\nO|X|X")
                print("result: O Won")
        elif move == "4":
            print("O|X| \n------\nX|O|X\n------\nO| | ")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nX|O|X\n------\nO| |O")
                print("result: O Won")
            elif move == "9":
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "8":
                print("O|X| \n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\n |O|X\n------\n | |O")
            print("result: O Won")
        elif move == "9":
            print("O|X|O\n------\n |O|X\n------\n | |X")
            move = input("move: ")
            if move == "4":
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "8":
                print("O|X|O\n------\n |O|X\n------\nO|X|X")
                print("result: O Won")
elif move == "4":
    print("O| | \n------\nX| | \n------\n | | ")
    move = input("move: ")
    if move == "9":
        print("O| | \n------\nX| |O\n------\n | |X")
        move = input("move: ")
        if move == "8":
            print("O| | \n------\nX| |O\n------\nO|X|X")
            move = input("move: ")
            if move == "2":
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "5":
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "3":
                print("O|O|X\n------\nX| |O\n------\nO|X|X")
                move = input("move: ")
                if move == "5":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "5":
            print("O| |O\n------\nX|X|O\n------\n | |X")
            move = input("move: ")
            if move == "7":
                print("O|O|O\n------\nX|X|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("O|O|O\n------\nX|X|O\n------\n |X|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "2":
            print("O|X| \n------\nX| |O\n------\n |O|X")
            move = input("move: ")
            if move == "5":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX| |O\n------\nO|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\nX| |O\n------\nX|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "7":
            print("O| | \n------\nX| |O\n------\nX|O|X")
            move = input("move: ")
            if move == "2":
                print("O|X|O\n------\nX| |O\n------\nX|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O| |O\n------\nX|X|O\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "3":
            print("O| |X\n------\nX| |O\n------\nO| |X")
            move = input("move: ")
            if move == "2":
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "8":
                print("O|O|X\n------\nX| |O\n------\nO|X|X")
                move = input("move: ")
                if move == "5":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "5":
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
    elif move == "7":
        print("O| |O\n------\nX| | \n------\nX| | ")
        move = input("move: ")
        if move == "8":
            print("O|O|O\n------\nX| | \n------\nX|X| ")
            print("result: O Won")
        elif move == "5":
            print("O|O|O\n------\nX|X| \n------\nX| | ")
            print("result: O Won")
        elif move == "6":
            print("O|O|O\n------\nX| |X\n------\nX| | ")
            print("result: O Won")
        elif move == "9":
            print("O|O|O\n------\nX| | \n------\nX| |X")
            print("result: O Won")
        elif move == "2":
            print("O|X|O\n------\nX| | \n------\nX| |O")
            move = input("move: ")
            if move == "6":
                print("O|X|O\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "5":
                print("O|X|O\n------\nX|X|O\n------\nX| |O")
                print("result: O Won")
            elif move == "8":
                print("O|X|O\n------\nX|O| \n------\nX|X|O")
                print("result: O Won")
    elif move == "3":
        print("O| |X\n------\nX|O| \n------\n | | ")
        move = input("move: ")
        if move == "9":
            print("O| |X\n------\nX|O|O\n------\n | |X")
            move = input("move: ")
            if move == "8":
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "7":
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "7":
            print("O| |X\n------\nX|O| \n------\nX|O| ")
            move = input("move: ")
            if move == "2":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
            elif move == "6":
                print("O| |X\n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
                print("result: O Won")
        elif move == "8":
            print("O| |X\n------\nX|O| \n------\n |X|O")
            print("result: O Won")
        elif move == "6":
            print("O| |X\n------\nX|O|X\n------\n | |O")
            print("result: O Won")
        elif move == "2":
            print("O|X|X\n------\nX|O| \n------\n | |O")
            print("result: O Won")
    elif move == "5":
        print("O| | \n------\nX|X|O\n------\n | | ")
        move = input("move: ")
        if move == "3":
            print("O| |X\n------\nX|X|O\n------\nO| | ")
            move = input("move: ")
            if move == "8":
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "9":
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "7":
            print("O| |O\n------\nX|X|O\n------\nX| | ")
            move = input("move: ")
            if move == "8":
                print("O|O|O\n------\nX|X|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|X|O\n------\nX| |O")
                print("result: O Won")
            elif move == "9":
                print("O|O|O\n------\nX|X|O\n------\nX| |X")
                print("result: O Won")
        elif move == "8":
            print("O|O| \n------\nX|X|O\n------\n |X| ")
            move = input("move: ")
            if move == "9":
                print("O|O|O\n------\nX|X|O\n------\n |X|X")
                print("result: O Won")
            elif move == "7":
                print("O|O|O\n------\nX|X|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "3":
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "9":
            print("O| | \n------\nX|X|O\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("O| |O\n------\nX|X|O\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "2":
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "9":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
    elif move == "2":
        print("O|X| \n------\nX| | \n------\n |O| ")
        move = input("move: ")
        if move == "9":
            print("O|X| \n------\nX| |O\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("O|X|O\n------\nX| |O\n------\nX|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX| |O\n------\nO|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "3":
            print("O|X|X\n------\nX| | \n------\n |O|O")
            move = input("move: ")
            if move == "7":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
            elif move == "5":
                print("O|X|X\n------\nX|X| \n------\nO|O|O")
                print("result: O Won")
        elif move == "7":
            print("O|X| \n------\nX|O| \n------\nX|O| ")
            move = input("move: ")
            if move == "6":
                print("O|X| \n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
        elif move == "5":
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            move = input("move: ")
            if move == "7":
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "9":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "6":
            print("O|X| \n------\nX|O|X\n------\n |O| ")
            move = input("move: ")
            if move == "9":
                print("O|X|O\n------\nX|O|X\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
            elif move == "7":
                print("O|X| \n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
    elif move == "8":
        print("O| |O\n------\nX| | \n------\n |X| ")
        move = input("move: ")
        if move == "7":
            print("O| |O\n------\nX| | \n------\nX|X|O")
            move = input("move: ")
            if move == "6":
                print("O|O|O\n------\nX| |X\n------\nX|X|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O| \n------\nX|X|O")
                print("result: O Won")
            elif move == "5":
                print("O| |O\n------\nX|X|O\n------\nX|X|O")
                print("result: O Won")
        elif move == "6":
            print("O|O|O\n------\nX| |X\n------\n |X| ")
            print("result: O Won")
        elif move == "9":
            print("O| |O\n------\nX| | \n------\nO|X|X")
            move = input("move: ")
            if move == "6":
                print("O| |O\n------\nX|O|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "5":
                print("O|O|O\n------\nX|X| \n------\nO|X|X")
                print("result: O Won")
        elif move == "5":
            print("O|O|O\n------\nX|X| \n------\n |X| ")
            print("result: O Won")
        elif move == "2":
            print("O|X|O\n------\nX|O| \n------\n |X| ")
            move = input("move: ")
            if move == "7":
                print("O|X|O\n------\nX|O| \n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|O\n------\nX|O|X\n------\n |X|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
                print("result: O Won")
    elif move == "6":
        print("O| | \n------\nX|O|X\n------\n | | ")
        move = input("move: ")
        if move == "2":
            print("O|X| \n------\nX|O|X\n------\n | |O")
            print("result: O Won")
        elif move == "8":
            print("O|O| \n------\nX|O|X\n------\n |X| ")
            move = input("move: ")
            if move == "3":
                print("O|O|X\n------\nX|O|X\n------\n |X|O")
                print("result: O Won")
            elif move == "9":
                print("O|O|O\n------\nX|O|X\n------\n |X|X")
                print("result: O Won")
            elif move == "7":
                print("O|O| \n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "3":
            print("O| |X\n------\nX|O|X\n------\n | |O")
            print("result: O Won")
        elif move == "7":
            print("O|O| \n------\nX|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "3":
                print("O|O|X\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "8":
                print("O|O| \n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
        elif move == "9":
            print("O| |O\n------\nX|O|X\n------\n | |X")
            move = input("move: ")
            if move == "7":
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "8":
                print("O| |O\n------\nX|O|X\n------\nO|X|X")
                print("result: O Won")
elif move == "1":
    print("X| | \n------\n |O| \n------\n | | ")
    move = input("move: ")
    if move == "8":
        print("X| | \n------\nO|O| \n------\n |X| ")
        move = input("move: ")
        if move == "2":
            print("X|X| \n------\nO|O|O\n------\n |X| ")
            print("result: O Won")
        elif move == "6":
            print("X| |O\n------\nO|O|X\n------\n |X| ")
            move = input("move: ")
            if move == "9":
                print("X| |O\n------\nO|O|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "7":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                print("result: O Won")
        elif move == "3":
            print("X| |X\n------\nO|O|O\n------\n |X| ")
            print("result: O Won")
        elif move == "7":
            print("X| | \n------\nO|O|O\n------\nX|X| ")
            print("result: O Won")
        elif move == "9":
            print("X| | \n------\nO|O| \n------\nO|X|X")
            move = input("move: ")
            if move == "3":
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "2":
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "6":
                print("X| |O\n------\nO|O|X\n------\nO|X|X")
                print("result: O Won")
    elif move == "7":
        print("X| | \n------\nO|O| \n------\nX| | ")
        move = input("move: ")
        if move == "2":
            print("X|X| \n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
        elif move == "8":
            print("X| | \n------\nO|O|O\n------\nX|X| ")
            print("result: O Won")
        elif move == "3":
            print("X| |X\n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
        elif move == "6":
            print("X| | \n------\nO|O|X\n------\nX| |O")
            move = input("move: ")
            if move == "8":
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "3":
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "9":
            print("X| | \n------\nO|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "3":
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "6":
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
                print("result: O Won")
    elif move == "3":
        print("X|O|X\n------\n |O| \n------\n | | ")
        move = input("move: ")
        if move == "4":
            print("X|O|X\n------\nX|O| \n------\n |O| ")
            print("result: O Won")
        elif move == "7":
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print("X|O|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "6":
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
                print("result: O Won")
        elif move == "6":
            print("X|O|X\n------\n |O|X\n------\n |O| ")
            print("result: O Won")
        elif move == "9":
            print("X|O|X\n------\n |O|O\n------\n | |X")
            move = input("move: ")
            if move == "7":
                print("X|O|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("X|O|X\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
            elif move == "4":
                print("X|O|X\n------\nX|O|O\n------\n |O|X")
                print("result: O Won")
        elif move == "8":
            print("X|O|X\n------\n |O| \n------\nO|X| ")
            move = input("move: ")
            if move == "4":
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "9":
                print("X|O|X\n------\n |O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "6":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
    elif move == "6":
        print("X| |O\n------\n |O|X\n------\n | | ")
        move = input("move: ")
        if move == "9":
            print("X| |O\n------\n |O|X\n------\n |O|X")
            move = input("move: ")
            if move == "4":
                print("X|O|O\n------\nX|O|X\n------\n |O|X")
                print("result: O Won")
            elif move == "7":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
        elif move == "4":
            print("X| |O\n------\nX|O|X\n------\nO| | ")
            print("result: O Won")
        elif move == "7":
            print("X| |O\n------\nO|O|X\n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "8":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "2":
            print("X|X|O\n------\n |O|X\n------\nO| | ")
            print("result: O Won")
        elif move == "8":
            print("X| |O\n------\n |O|X\n------\nO|X| ")
            print("result: O Won")
    elif move == "2":
        print("X|X|O\n------\n |O| \n------\n | | ")
        move = input("move: ")
        if move == "8":
            print("X|X|O\n------\n |O| \n------\n |X|O")
            move = input("move: ")
            if move == "7":
                print("X|X|O\n------\n |O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "4":
                print("X|X|O\n------\nX|O| \n------\nO|X|O")
                print("result: O Won")
        elif move == "4":
            print("X|X|O\n------\nX|O| \n------\nO| | ")
            print("result: O Won")
        elif move == "7":
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print("X|X|O\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "6":
            print("X|X|O\n------\n |O|X\n------\nO| | ")
            print("result: O Won")
        elif move == "9":
            print("X|X|O\n------\nO|O| \n------\n | |X")
            move = input("move: ")
            if move == "8":
                print("X|X|O\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
            elif move == "7":
                print("X|X|O\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
                print("result: O Won")
    elif move == "9":
        print("X| | \n------\n |O| \n------\n |O|X")
        move = input("move: ")
        if move == "3":
            print("X|O|X\n------\n |O| \n------\n |O|X")
            print("result: O Won")
        elif move == "6":
            print("X| |O\n------\n |O|X\n------\n |O|X")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "7":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "4":
                print("X|O|O\n------\nX|O|X\n------\n |O|X")
                print("result: O Won")
        elif move == "4":
            print("X| | \n------\nX|O| \n------\nO|O|X")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\nX|O| \n------\nO|O|X")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
                print("result: O Won")
            elif move == "6":
                print("X| |O\n------\nX|O|X\n------\nO|O|X")
                print("result: O Won")
        elif move == "2":
            print("X|X|O\n------\n |O| \n------\n |O|X")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nX|O| \n------\nO|O|X")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "7":
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                move = input("move: ")
                if move == "6":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "7":
            print("X| | \n------\nO|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "6":
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
                print("result: O Won")
    elif move == "4":
        print("X| | \n------\nX|O| \n------\nO| | ")
        move = input("move: ")
        if move == "6":
            print("X| | \n------\nX|O|X\n------\nO|O| ")
            move = input("move: ")
            if move == "9":
                print("X| |O\n------\nX|O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "2":
                print("X|X|O\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
        elif move == "8":
            print("X| |O\n------\nX|O| \n------\nO|X| ")
            print("result: O Won")
        elif move == "9":
            print("X|O| \n------\nX|O| \n------\nO| |X")
            move = input("move: ")
            if move == "6":
                print("X|O|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "8":
                print("X|O|O\n------\nX|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
                print("result: O Won")
        elif move == "2":
            print("X|X|O\n------\nX|O| \n------\nO| | ")
            print("result: O Won")
        elif move == "3":
            print("X|O|X\n------\nX|O| \n------\nO| | ")
            move = input("move: ")
            if move == "6":
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "9":
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
                print("result: O Won")
            elif move == "8":
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
elif move == "2":
    print("O|X| \n------\n | | \n------\n | | ")
    move = input("move: ")
    if move == "8":
        print("O|X| \n------\n |O| \n------\n |X| ")
        move = input("move: ")
        if move == "9":
            print("O|X| \n------\n |O| \n------\nO|X|X")
            move = input("move: ")
            if move == "4":
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "6":
                print("O|X|O\n------\n |O|X\n------\nO|X|X")
                print("result: O Won")
        elif move == "6":
            print("O|X|O\n------\n |O|X\n------\n |X| ")
            move = input("move: ")
            if move == "9":
                print("O|X|O\n------\n |O|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "4":
            print("O|X| \n------\nX|O| \n------\n |X|O")
            print("result: O Won")
        elif move == "7":
            print("O|X| \n------\n |O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\n |O|O\n------\n |X| ")
            move = input("move: ")
            if move == "7":
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
            elif move == "4":
                print("O|X|X\n------\nX|O|O\n------\n |X|O")
                print("result: O Won")
    elif move == "3":
        print("O|X|X\n------\nO| | \n------\n | | ")
        move = input("move: ")
        if move == "8":
            print("O|X|X\n------\nO| | \n------\nO|X| ")
            print("result: O Won")
        elif move == "7":
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "8":
                print("O|X|X\n------\nO|O| \n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
        elif move == "6":
            print("O|X|X\n------\nO| |X\n------\nO| | ")
            print("result: O Won")
        elif move == "5":
            print("O|X|X\n------\nO|X| \n------\nO| | ")
            print("result: O Won")
        elif move == "9":
            print("O|X|X\n------\nO| |O\n------\n | |X")
            move = input("move: ")
            if move == "5":
                print("O|X|X\n------\nO|X|O\n------\nO| |X")
                print("result: O Won")
            elif move == "8":
                print("O|X|X\n------\nO| |O\n------\nO|X|X")
                print("result: O Won")
            elif move == "7":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
    elif move == "7":
        print("O|X| \n------\n |O| \n------\nX| | ")
        move = input("move: ")
        if move == "6":
            print("O|X| \n------\n |O|X\n------\nX| |O")
            print("result: O Won")
        elif move == "9":
            print("O|X| \n------\n |O| \n------\nX|O|X")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "6":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "8":
            print("O|X| \n------\n |O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
        elif move == "4":
            print("O|X| \n------\nX|O| \n------\nX| |O")
            print("result: O Won")
    elif move == "6":
        print("O|X| \n------\n | |X\n------\nO| | ")
        move = input("move: ")
        if move == "4":
            print("O|X| \n------\nX|O|X\n------\nO| | ")
            move = input("move: ")
            if move == "8":
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\nX|O|X\n------\nO| |O")
                print("result: O Won")
            elif move == "9":
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
                print("result: O Won")
        elif move == "8":
            print("O|X| \n------\n |O|X\n------\nO|X| ")
            move = input("move: ")
            if move == "9":
                print("O|X| \n------\nO|O|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("O|X| \n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "5":
            print("O|X| \n------\nO|X|X\n------\nO| | ")
            print("result: O Won")
        elif move == "9":
            print("O|X| \n------\nO| |X\n------\nO| |X")
            print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\n | |X\n------\nO| |O")
            move = input("move: ")
            if move == "8":
                print("O|X|X\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "4":
                print("O|X|X\n------\nX|O|X\n------\nO| |O")
                print("result: O Won")
            elif move == "5":
                print("O|X|X\n------\n |X|X\n------\nO|O|O")
                print("result: O Won")
    elif move == "5":
        print("O|X| \n------\n |X| \n------\n |O| ")
        move = input("move: ")
        if move == "7":
            print("O|X|O\n------\n |X| \n------\nX|O| ")
            move = input("move: ")
            if move == "9":
                print("O|X|O\n------\nO|X| \n------\nX|O|X")
                move = input("move: ")
                if move == "6":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "6":
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "4":
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            move = input("move: ")
            if move == "9":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "3":
            print("O|X|X\n------\n |X| \n------\nO|O| ")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nO|X|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "4":
                print("O|X|X\n------\nX|X| \n------\nO|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|X| \n------\nO|O|X")
                print("result: O Won")
        elif move == "6":
            print("O|X| \n------\nO|X|X\n------\n |O| ")
            move = input("move: ")
            if move == "9":
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nO|X|X\n------\nO|O| ")
                print("result: O Won")
        elif move == "9":
            print("O|X|O\n------\n |X| \n------\n |O|X")
            move = input("move: ")
            if move == "6":
                print("O|X|O\n------\nO|X|X\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\n |X|O\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
    elif move == "9":
        print("O|X| \n------\n | | \n------\n |O|X")
        move = input("move: ")
        if move == "5":
            print("O|X| \n------\n |X| \n------\nO|O|X")
            move = input("move: ")
            if move == "6":
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\nO|X| \n------\nO|O|X")
                print("result: O Won")
            elif move == "4":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "4":
            print("O|X| \n------\nX| |O\n------\n |O|X")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "3":
            print("O|X|X\n------\n | |O\n------\n |O|X")
            move = input("move: ")
            if move == "4":
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O|X|X\n------\n |X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "6":
            print("O|X|O\n------\n | |X\n------\n |O|X")
            move = input("move: ")
            if move == "5":
                print("O|X|O\n------\nO|X|X\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "4":
                print("O|X|O\n------\nX|O|X\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
        elif move == "7":
            print("O|X|O\n------\n | | \n------\nX|O|X")
            move = input("move: ")
            if move == "4":
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                move = input("move: ")
                if move == "6":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O|X|O\n------\nO|X| \n------\nX|O|X")
                move = input("move: ")
                if move == "6":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "6":
                print("O|X|O\n------\nO| |X\n------\nX|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                    print("result: Draw")
    elif move == "4":
        print("O|X| \n------\nX| | \n------\n |O| ")
        move = input("move: ")
        if move == "9":
            print("O|X| \n------\nX| |O\n------\n |O|X")
            move = input("move: ")
            if move == "7":
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "5":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX| |O\n------\nO|O|X")
                move = input("move: ")
                if move == "5":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "3":
            print("O|X|X\n------\nX| | \n------\n |O|O")
            move = input("move: ")
            if move == "5":
                print("O|X|X\n------\nX|X| \n------\nO|O|O")
                print("result: O Won")
            elif move == "7":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\nX| |X\n------\nO|O|O")
                print("result: O Won")
        elif move == "7":
            print("O|X| \n------\nX|O| \n------\nX|O| ")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nX|O| \n------\nX|O|O")
                print("result: O Won")
            elif move == "6":
                print("O|X| \n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "5":
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            move = input("move: ")
            if move == "7":
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "9":
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "6":
            print("O|X| \n------\nX|O|X\n------\n |O| ")
            move = input("move: ")
            if move == "9":
                print("O|X|O\n------\nX|O|X\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X| \n------\nX|O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
elif move == "5":
    print(" | | \n------\n |X| \n------\nO| | ")
    move = input("move: ")
    if move == "9":
        print("O| | \n------\n |X| \n------\nO| |X")
        move = input("move: ")
        if move == "2":
            print("O|X| \n------\nO|X| \n------\nO| |X")
            print("result: O Won")
        elif move == "8":
            print("O| | \n------\nO|X| \n------\nO|X|X")
            print("result: O Won")
        elif move == "4":
            print("O| | \n------\nX|X|O\n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "3":
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "6":
            print("O| | \n------\nO|X|X\n------\nO| |X")
            print("result: O Won")
        elif move == "3":
            print("O| |X\n------\nO|X| \n------\nO| |X")
            print("result: O Won")
    elif move == "8":
        print(" |O| \n------\n |X| \n------\nO|X| ")
        move = input("move: ")
        if move == "1":
            print("X|O| \n------\n |X| \n------\nO|X|O")
            move = input("move: ")
            if move == "6":
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "3":
                print("X|O|X\n------\nO|X| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "4":
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
        elif move == "4":
            print(" |O| \n------\nX|X|O\n------\nO|X| ")
            move = input("move: ")
            if move == "1":
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
            elif move == "3":
                print(" |O|X\n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
            elif move == "9":
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "9":
            print("O|O| \n------\n |X| \n------\nO|X|X")
            move = input("move: ")
            if move == "3":
                print("O|O|X\n------\nO|X| \n------\nO|X|X")
                print("result: O Won")
            elif move == "6":
                print("O|O|O\n------\n |X|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("O|O|O\n------\nX|X| \n------\nO|X|X")
                print("result: O Won")
        elif move == "3":
            print("O|O|X\n------\n |X| \n------\nO|X| ")
            move = input("move: ")
            if move == "4":
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "6":
                print("O|O|X\n------\nO|X|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|O|X\n------\nO|X| \n------\nO|X|X")
                print("result: O Won")
        elif move == "6":
            print(" |O| \n------\nO|X|X\n------\nO|X| ")
            move = input("move: ")
            if move == "1":
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "9":
                print("O|O| \n------\nO|X|X\n------\nO|X|X")
                print("result: O Won")
            elif move == "3":
                print("O|O|X\n------\nO|X|X\n------\nO|X| ")
                print("result: O Won")
    elif move == "3":
        print("O| |X\n------\n |X| \n------\nO| | ")
        move = input("move: ")
        if move == "8":
            print("O| |X\n------\nO|X| \n------\nO|X| ")
            print("result: O Won")
        elif move == "9":
            print("O| |X\n------\nO|X| \n------\nO| |X")
            print("result: O Won")
        elif move == "4":
            print("O| |X\n------\nX|X|O\n------\nO| | ")
            move = input("move: ")
            if move == "8":
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "9":
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                move = input("move: ")
                if move == "9":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
        elif move == "2":
            print("O|X|X\n------\n |X| \n------\nO|O| ")
            move = input("move: ")
            if move == "4":
                print("O|X|X\n------\nX|X| \n------\nO|O|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\n |X|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|X| \n------\nO|O|X")
                print("result: O Won")
        elif move == "6":
            print("O| |X\n------\nO|X|X\n------\nO| | ")
            print("result: O Won")
    elif move == "2":
        print(" |X| \n------\n |X| \n------\nO|O| ")
        move = input("move: ")
        if move == "6":
            print(" |X| \n------\nO|X|X\n------\nO|O| ")
            move = input("move: ")
            if move == "3":
                print("O|X|X\n------\nO|X|X\n------\nO|O| ")
                print("result: O Won")
            elif move == "9":
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nO|X|X\n------\nO|O|O")
                print("result: O Won")
        elif move == "3":
            print("O|X|X\n------\n |X| \n------\nO|O| ")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\n |X|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "4":
                print("O|X|X\n------\nX|X| \n------\nO|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|X| \n------\nO|O|X")
                print("result: O Won")
        elif move == "4":
            print(" |X| \n------\nX|X| \n------\nO|O|O")
            print("result: O Won")
        elif move == "9":
            print("O|X| \n------\n |X| \n------\nO|O|X")
            move = input("move: ")
            if move == "6":
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "4":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|X|X\n------\nO|X| \n------\nO|O|X")
                print("result: O Won")
        elif move == "1":
            print("X|X| \n------\n |X| \n------\nO|O|O")
            print("result: O Won")
    elif move == "6":
        print(" | | \n------\nO|X|X\n------\nO| | ")
        move = input("move: ")
        if move == "2":
            print(" |X| \n------\nO|X|X\n------\nO|O| ")
            move = input("move: ")
            if move == "1":
                print("X|X| \n------\nO|X|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "3":
                print(" |X|X\n------\nO|X|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "9":
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
                print("result: O Won")
        elif move == "3":
            print("O| |X\n------\nO|X|X\n------\nO| | ")
            print("result: O Won")
        elif move == "1":
            print("X| | \n------\nO|X|X\n------\nO| |O")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nO|X|X\n------\nO|O|O")
                print("result: O Won")
            elif move == "8":
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "3":
                print("X| |X\n------\nO|X|X\n------\nO|O|O")
                print("result: O Won")
        elif move == "8":
            print("O| | \n------\nO|X|X\n------\nO|X| ")
            print("result: O Won")
        elif move == "9":
            print("O| | \n------\nO|X|X\n------\nO| |X")
            print("result: O Won")
    elif move == "1":
        print("X| | \n------\n |X| \n------\nO| |O")
        move = input("move: ")
        if move == "3":
            print("X| |X\n------\n |X| \n------\nO|O|O")
            print("result: O Won")
        elif move == "4":
            print("X| | \n------\nX|X| \n------\nO|O|O")
            print("result: O Won")
        elif move == "8":
            print("X|O| \n------\n |X| \n------\nO|X|O")
            move = input("move: ")
            if move == "3":
                print("X|O|X\n------\nO|X| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "4":
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
            elif move == "6":
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                    print("result: Draw")
        elif move == "2":
            print("X|X| \n------\n |X| \n------\nO|O|O")
            print("result: O Won")
        elif move == "6":
            print("X| | \n------\n |X|X\n------\nO|O|O")
            print("result: O Won")
    elif move == "4":
        print(" | | \n------\nX|X|O\n------\nO| | ")
        move = input("move: ")
        if move == "3":
            print(" |O|X\n------\nX|X|O\n------\nO| | ")
            move = input("move: ")
            if move == "9":
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "1":
                print("X|O|X\n------\nX|X|O\n------\nO| |O")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
            elif move == "8":
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "8":
            print(" |O| \n------\nX|X|O\n------\nO|X| ")
            move = input("move: ")
            if move == "9":
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "1":
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
            elif move == "3":
                print(" |O|X\n------\nX|X|O\n------\nO|X|O")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                    print("result: Draw")
        elif move == "1":
            print("X| | \n------\nX|X|O\n------\nO| |O")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nX|X|O\n------\nO|O|O")
                print("result: O Won")
            elif move == "8":
                print("X| |O\n------\nX|X|O\n------\nO|X|O")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nX|X|O\n------\nO|O|O")
                print("result: O Won")
        elif move == "2":
            print(" |X| \n------\nX|X|O\n------\nO|O| ")
            move = input("move: ")
            if move == "9":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print(" |X|X\n------\nX|X|O\n------\nO|O|O")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nX|X|O\n------\nO|O|O")
                print("result: O Won")
        elif move == "9":
            print("O| | \n------\nX|X|O\n------\nO| |X")
            move = input("move: ")
            if move == "2":
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                move = input("move: ")
                if move == "3":
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                    print("result: Draw")
            elif move == "3":
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "8":
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                move = input("move: ")
                if move == "3":
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                    print("result: Draw")
elif move == "9":
    print(" | | \n------\n |O| \n------\n | |X")
    move = input("move: ")
    if move == "2":
        print(" |X| \n------\nO|O| \n------\n | |X")
        move = input("move: ")
        if move == "7":
            print(" |X| \n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
        elif move == "3":
            print(" |X|X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
        elif move == "6":
            print(" |X|O\n------\nO|O|X\n------\n | |X")
            move = input("move: ")
            if move == "1":
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
                print("result: O Won")
            elif move == "7":
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "1":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "8":
                print(" |X|O\n------\nO|O|X\n------\nO|X|X")
                print("result: O Won")
        elif move == "1":
            print("X|X|O\n------\nO|O| \n------\n | |X")
            move = input("move: ")
            if move == "7":
                print("X|X|O\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
                print("result: O Won")
        elif move == "8":
            print(" |X| \n------\nO|O|O\n------\n |X|X")
            print("result: O Won")
    elif move == "1":
        print("X| | \n------\n |O|O\n------\n | |X")
        move = input("move: ")
        if move == "7":
            print("X| | \n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
        elif move == "4":
            print("X| | \n------\nX|O|O\n------\nO| |X")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\nX|O|O\n------\nO| |X")
                print("result: O Won")
            elif move == "8":
                print("X| |O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "8":
            print("X| | \n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("X| |O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "3":
            print("X| |X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
        elif move == "2":
            print("X|X| \n------\nO|O|O\n------\n | |X")
            print("result: O Won")
    elif move == "8":
        print(" | | \n------\n |O| \n------\nO|X|X")
        move = input("move: ")
        if move == "1":
            print("X| |O\n------\n |O| \n------\nO|X|X")
            print("result: O Won")
        elif move == "4":
            print(" | |O\n------\nX|O| \n------\nO|X|X")
            print("result: O Won")
        elif move == "6":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
        elif move == "3":
            print(" | |X\n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "4":
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "1":
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "2":
            print(" |X| \n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "3":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print(" |X|O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
    elif move == "3":
        print(" | |X\n------\n |O|O\n------\n | |X")
        move = input("move: ")
        if move == "2":
            print(" |X|X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
        elif move == "8":
            print(" | |X\n------\nO|O|O\n------\n |X|X")
            print("result: O Won")
        elif move == "4":
            print(" |O|X\n------\nX|O|O\n------\n | |X")
            move = input("move: ")
            if move == "8":
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "1":
                print("X|O|X\n------\nX|O|O\n------\n |O|X")
                print("result: O Won")
            elif move == "7":
                print(" |O|X\n------\nX|O|O\n------\nX|O|X")
                print("result: O Won")
        elif move == "1":
            print("X| |X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
        elif move == "7":
            print(" | |X\n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
    elif move == "6":
        print(" | |O\n------\n |O|X\n------\n | |X")
        move = input("move: ")
        if move == "4":
            print(" | |O\n------\nX|O|X\n------\nO| |X")
            print("result: O Won")
        elif move == "7":
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            move = input("move: ")
            if move == "4":
                print(" |O|O\n------\nX|O|X\n------\nX|O|X")
                print("result: O Won")
            elif move == "2":
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "4":
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "1":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
        elif move == "1":
            print("X| |O\n------\n |O|X\n------\n |O|X")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|O|X")
                print("result: O Won")
            elif move == "4":
                print("X|O|O\n------\nX|O|X\n------\n |O|X")
                print("result: O Won")
            elif move == "7":
                print("X|O|O\n------\n |O|X\n------\nX|O|X")
                print("result: O Won")
        elif move == "2":
            print(" |X|O\n------\n |O|X\n------\nO| |X")
            print("result: O Won")
        elif move == "8":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
    elif move == "7":
        print(" | | \n------\n |O| \n------\nX|O|X")
        move = input("move: ")
        if move == "4":
            print(" |O| \n------\nX|O| \n------\nX|O|X")
            print("result: O Won")
        elif move == "6":
            print(" |O| \n------\n |O|X\n------\nX|O|X")
            print("result: O Won")
        elif move == "1":
            print("X|O| \n------\n |O| \n------\nX|O|X")
            print("result: O Won")
        elif move == "2":
            print(" |X| \n------\nO|O| \n------\nX|O|X")
            move = input("move: ")
            if move == "1":
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
            elif move == "6":
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                move = input("move: ")
                if move == "1":
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                    print("result: Draw")
            elif move == "3":
                print(" |X|X\n------\nO|O|O\n------\nX|O|X")
                print("result: O Won")
        elif move == "3":
            print(" |O|X\n------\n |O| \n------\nX|O|X")
            print("result: O Won")
    elif move == "4":
        print(" | | \n------\nX|O| \n------\nO| |X")
        move = input("move: ")
        if move == "3":
            print(" | |X\n------\nX|O|O\n------\nO| |X")
            move = input("move: ")
            if move == "8":
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "1":
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "6":
            print(" | |O\n------\nX|O|X\n------\nO| |X")
            print("result: O Won")
        elif move == "1":
            print("X| |O\n------\nX|O| \n------\nO| |X")
            print("result: O Won")
        elif move == "8":
            print(" | |O\n------\nX|O| \n------\nO|X|X")
            print("result: O Won")
        elif move == "2":
            print(" |X|O\n------\nX|O| \n------\nO| |X")
            print("result: O Won")
elif move == "3":
    print(" | |X\n------\n |O| \n------\n | | ")
    move = input("move: ")
    if move == "8":
        print(" | |X\n------\nO|O| \n------\n |X| ")
        move = input("move: ")
        if move == "7":
            print(" | |X\n------\nO|O|O\n------\nX|X| ")
            print("result: O Won")
        elif move == "1":
            print("X| |X\n------\nO|O|O\n------\n |X| ")
            print("result: O Won")
        elif move == "2":
            print(" |X|X\n------\nO|O|O\n------\n |X| ")
            print("result: O Won")
        elif move == "6":
            print(" | |X\n------\nO|O|X\n------\n |X|O")
            move = input("move: ")
            if move == "7":
                print("O| |X\n------\nO|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|X\n------\nO|O|X\n------\n |X|O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                move = input("move: ")
                if move == "7":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "9":
            print(" | |X\n------\nO|O|O\n------\n |X|X")
            print("result: O Won")
    elif move == "6":
        print(" | |X\n------\n |O|X\n------\n | |O")
        move = input("move: ")
        if move == "4":
            print("O| |X\n------\nX|O|X\n------\n | |O")
            print("result: O Won")
        elif move == "8":
            print("O| |X\n------\n |O|X\n------\n |X|O")
            print("result: O Won")
        elif move == "7":
            print("O| |X\n------\n |O|X\n------\nX| |O")
            print("result: O Won")
        elif move == "1":
            print("X|O|X\n------\n |O|X\n------\n | |O")
            move = input("move: ")
            if move == "4":
                print("X|O|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
            elif move == "7":
                print("X|O|X\n------\n |O|X\n------\nX|O|O")
                print("result: O Won")
            elif move == "8":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
        elif move == "2":
            print("O|X|X\n------\n |O|X\n------\n | |O")
            print("result: O Won")
    elif move == "9":
        print(" | |X\n------\n |O|O\n------\n | |X")
        move = input("move: ")
        if move == "2":
            print(" |X|X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
        elif move == "4":
            print("O| |X\n------\nX|O|O\n------\n | |X")
            move = input("move: ")
            if move == "2":
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                move = input("move: ")
                if move == "8":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "8":
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "7":
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
        elif move == "7":
            print(" | |X\n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
        elif move == "8":
            print(" | |X\n------\nO|O|O\n------\n |X|X")
            print("result: O Won")
        elif move == "1":
            print("X| |X\n------\nO|O|O\n------\n | |X")
            print("result: O Won")
    elif move == "7":
        print(" | |X\n------\nO|O| \n------\nX| | ")
        move = input("move: ")
        if move == "9":
            print(" | |X\n------\nO|O|O\n------\nX| |X")
            print("result: O Won")
        elif move == "8":
            print(" | |X\n------\nO|O| \n------\nX|X|O")
            move = input("move: ")
            if move == "6":
                print("O| |X\n------\nO|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|X\n------\nO|O| \n------\nX|X|O")
                print("result: O Won")
            elif move == "1":
                print("X| |X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
        elif move == "2":
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "6":
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
        elif move == "6":
            print(" | |X\n------\nO|O|X\n------\nX| |O")
            move = input("move: ")
            if move == "8":
                print("O| |X\n------\nO|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "2":
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                move = input("move: ")
                if move == "8":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "1":
            print("X| |X\n------\nO|O|O\n------\nX| | ")
            print("result: O Won")
    elif move == "1":
        print("X|O|X\n------\n |O| \n------\n | | ")
        move = input("move: ")
        if move == "6":
            print("X|O|X\n------\n |O|X\n------\n |O| ")
            print("result: O Won")
        elif move == "9":
            print("X|O|X\n------\n |O| \n------\n |O|X")
            print("result: O Won")
        elif move == "8":
            print("X|O|X\n------\n |O|O\n------\n |X| ")
            move = input("move: ")
            if move == "9":
                print("X|O|X\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
            elif move == "7":
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "4":
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "4":
            print("X|O|X\n------\nX|O| \n------\n |O| ")
            print("result: O Won")
        elif move == "7":
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            move = input("move: ")
            if move == "9":
                print("X|O|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "6":
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
                print("result: O Won")
            elif move == "8":
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
    elif move == "4":
        print(" |O|X\n------\nX|O| \n------\n | | ")
        move = input("move: ")
        if move == "6":
            print(" |O|X\n------\nX|O|X\n------\n | |O")
            move = input("move: ")
            if move == "8":
                print("O|O|X\n------\nX|O|X\n------\n |X|O")
                print("result: O Won")
            elif move == "7":
                print("O|O|X\n------\nX|O|X\n------\nX| |O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\nX|O|X\n------\n |O|O")
                print("result: O Won")
        elif move == "8":
            print(" |O|X\n------\nX|O| \n------\n |X|O")
            move = input("move: ")
            if move == "1":
                print("X|O|X\n------\nX|O| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "7":
                print("O|O|X\n------\nX|O| \n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("O|O|X\n------\nX|O|X\n------\n |X|O")
                print("result: O Won")
        elif move == "1":
            print("X|O|X\n------\nX|O| \n------\n |O| ")
            print("result: O Won")
        elif move == "7":
            print(" |O|X\n------\nX|O| \n------\nX|O| ")
            print("result: O Won")
        elif move == "9":
            print(" |O|X\n------\nX|O| \n------\n |O|X")
            print("result: O Won")
    elif move == "2":
        print("O|X|X\n------\n |O| \n------\n | | ")
        move = input("move: ")
        if move == "4":
            print("O|X|X\n------\nX|O| \n------\n | |O")
            print("result: O Won")
        elif move == "8":
            print("O|X|X\n------\nO|O| \n------\n |X| ")
            move = input("move: ")
            if move == "7":
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
                print("result: O Won")
        elif move == "7":
            print("O|X|X\n------\n |O| \n------\nX| |O")
            print("result: O Won")
        elif move == "9":
            print("O|X|X\n------\n |O|O\n------\n | |X")
            move = input("move: ")
            if move == "4":
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                move = input("move: ")
                if move == "7":
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                    print("result: Draw")
            elif move == "7":
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
                print("result: O Won")
            elif move == "8":
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
        elif move == "6":
            print("O|X|X\n------\n |O|X\n------\n | |O")
            print("result: O Won")
elif move == "8":
    print(" | | \n------\n |O| \n------\n |X| ")
    move = input("move: ")
    if move == "2":
        print(" |X| \n------\n |O|O\n------\n |X| ")
        move = input("move: ")
        if move == "9":
            print(" |X| \n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "3":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print(" |X|O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "1":
                print("X|X|O\n------\n |O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "3":
            print(" |X|X\n------\nO|O|O\n------\n |X| ")
            print("result: O Won")
        elif move == "4":
            print(" |X|O\n------\nX|O|O\n------\n |X| ")
            move = input("move: ")
            if move == "1":
                print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                print("result: O Won")
            elif move == "7":
                print(" |X|O\n------\nX|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print(" |X|O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "7":
            print(" |X| \n------\n |O|O\n------\nX|X|O")
            move = input("move: ")
            if move == "3":
                print(" |X|X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "4":
                print(" |X|O\n------\nX|O|O\n------\nX|X|O")
                print("result: O Won")
        elif move == "1":
            print("X|X|O\n------\n |O|O\n------\n |X| ")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                print("result: O Won")
            elif move == "7":
                print("X|X|O\n------\n |O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "9":
                print("X|X|O\n------\nO|O|O\n------\n |X|X")
                print("result: O Won")
    elif move == "9":
        print(" | | \n------\n |O| \n------\nO|X|X")
        move = input("move: ")
        if move == "1":
            print("X| |O\n------\n |O| \n------\nO|X|X")
            print("result: O Won")
        elif move == "6":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
        elif move == "4":
            print(" | |O\n------\nX|O| \n------\nO|X|X")
            print("result: O Won")
        elif move == "3":
            print(" | |X\n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "2":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "1":
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "2":
            print(" |X| \n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "3":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "1":
                print("X|X| \n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print(" |X|O\n------\nX|O|O\n------\nO|X|X")
                print("result: O Won")
    elif move == "6":
        print(" | |O\n------\n |O|X\n------\n |X| ")
        move = input("move: ")
        if move == "1":
            print("X| |O\n------\n |O|X\n------\nO|X| ")
            print("result: O Won")
        elif move == "4":
            print(" |O|O\n------\nX|O|X\n------\n |X| ")
            move = input("move: ")
            if move == "7":
                print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                print("result: O Won")
            elif move == "9":
                print("O|O|O\n------\nX|O|X\n------\n |X|X")
                print("result: O Won")
            elif move == "1":
                print("X|O|O\n------\nX|O|X\n------\nO|X| ")
                print("result: O Won")
        elif move == "7":
            print(" | |O\n------\n |O|X\n------\nX|X|O")
            move = input("move: ")
            if move == "1":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "2":
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "4":
                print("O| |O\n------\nX|O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "2":
            print(" |X|O\n------\n |O|X\n------\n |X|O")
            move = input("move: ")
            if move == "1":
                print("X|X|O\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "4":
                print(" |X|O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
                print("result: O Won")
        elif move == "9":
            print(" | |O\n------\n |O|X\n------\nO|X|X")
            print("result: O Won")
    elif move == "4":
        print(" | | \n------\nX|O| \n------\n |X|O")
        move = input("move: ")
        if move == "1":
            print("X| | \n------\nX|O| \n------\nO|X|O")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\nX|O| \n------\nO|X|O")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "6":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "7":
            print("O| | \n------\nX|O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "2":
            print(" |X|O\n------\nX|O| \n------\n |X|O")
            move = input("move: ")
            if move == "6":
                print("O|X|O\n------\nX|O|X\n------\n |X|O")
                print("result: O Won")
            elif move == "1":
                print("X|X|O\n------\nX|O|O\n------\n |X|O")
                print("result: O Won")
            elif move == "7":
                print("O|X|O\n------\nX|O| \n------\nX|X|O")
                print("result: O Won")
        elif move == "6":
            print(" | | \n------\nX|O|X\n------\nO|X|O")
            move = input("move: ")
            if move == "3":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "1":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "2":
                print(" |X|O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "3":
            print("O| |X\n------\nX|O| \n------\n |X|O")
            print("result: O Won")
    elif move == "7":
        print(" | | \n------\n |O| \n------\nX|X|O")
        move = input("move: ")
        if move == "4":
            print("O| | \n------\nX|O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "3":
            print("O| |X\n------\n |O| \n------\nX|X|O")
            print("result: O Won")
        elif move == "2":
            print(" |X| \n------\nO|O| \n------\nX|X|O")
            move = input("move: ")
            if move == "1":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("O|X| \n------\nO|O|X\n------\nX|X|O")
                print("result: O Won")
            elif move == "3":
                print("O|X|X\n------\nO|O| \n------\nX|X|O")
                print("result: O Won")
        elif move == "6":
            print("O| | \n------\n |O|X\n------\nX|X|O")
            print("result: O Won")
        elif move == "1":
            print("X| | \n------\nO|O| \n------\nX|X|O")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "3":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
    elif move == "3":
        print(" | |X\n------\n |O| \n------\nO|X| ")
        move = input("move: ")
        if move == "9":
            print(" | |X\n------\n |O|O\n------\nO|X|X")
            move = input("move: ")
            if move == "1":
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "1":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print(" |X|X\n------\nO|O|O\n------\nO|X|X")
                print("result: O Won")
        elif move == "1":
            print("X|O|X\n------\n |O| \n------\nO|X| ")
            move = input("move: ")
            if move == "4":
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                move = input("move: ")
                if move == "9":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "6":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "9":
                print("X|O|X\n------\n |O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
        elif move == "4":
            print("O| |X\n------\nX|O| \n------\nO|X| ")
            move = input("move: ")
            if move == "9":
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                move = input("move: ")
                if move == "2":
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\nX|O| \n------\nO|X|O")
                print("result: O Won")
            elif move == "6":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "2":
            print("O|X|X\n------\n |O| \n------\nO|X| ")
            move = input("move: ")
            if move == "9":
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
                print("result: O Won")
            elif move == "4":
                print("O|X|X\n------\nX|O| \n------\nO|X|O")
                print("result: O Won")
            elif move == "6":
                print("O|X|X\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
        elif move == "6":
            print(" | |X\n------\n |O|X\n------\nO|X|O")
            move = input("move: ")
            if move == "4":
                print("O| |X\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "1":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "2":
                print("O|X|X\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
    elif move == "1":
        print("X| | \n------\n |O| \n------\n |X|O")
        move = input("move: ")
        if move == "2":
            print("X|X|O\n------\n |O| \n------\n |X|O")
            move = input("move: ")
            if move == "4":
                print("X|X|O\n------\nX|O|O\n------\n |X|O")
                print("result: O Won")
            elif move == "6":
                print("X|X|O\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "7":
                print("X|X|O\n------\n |O|O\n------\nX|X|O")
                print("result: O Won")
        elif move == "4":
            print("X| | \n------\nX|O| \n------\nO|X|O")
            move = input("move: ")
            if move == "2":
                print("X|X|O\n------\nX|O| \n------\nO|X|O")
                print("result: O Won")
            elif move == "6":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "3":
                print("X|O|X\n------\nX|O| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
        elif move == "3":
            print("X|O|X\n------\n |O| \n------\n |X|O")
            move = input("move: ")
            if move == "7":
                print("X|O|X\n------\nO|O| \n------\nX|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
            elif move == "4":
                print("X|O|X\n------\nX|O| \n------\nO|X|O")
                move = input("move: ")
                if move == "6":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "6":
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                move = input("move: ")
                if move == "7":
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "7":
            print("X| | \n------\nO|O| \n------\nX|X|O")
            move = input("move: ")
            if move == "2":
                print("X|X| \n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "3":
                print("X| |X\n------\nO|O|O\n------\nX|X|O")
                print("result: O Won")
            elif move == "6":
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                move = input("move: ")
                if move == "2":
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                    print("result: Draw")
        elif move == "6":
            print("X| | \n------\n |O|X\n------\nO|X|O")
            move = input("move: ")
            if move == "3":
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                move = input("move: ")
                if move == "4":
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                    print("result: Draw")
            elif move == "2":
                print("X|X|O\n------\n |O|X\n------\nO|X|O")
                print("result: O Won")
            elif move == "4":
                print("X| |O\n------\nX|O|X\n------\nO|X|O")
                print("result: O Won")
