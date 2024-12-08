a = input('move: ')
if a == '8':
    print(" | | \n------\n |O| \n------\n | |X")
    a = input('move: ')
    if a == '7':
        print(" | | \n------\n |O| \n------\nO|X|X")
        a = input('move: ')
        if a == '1':
            print("O|X| \n------\n |O| \n------\nO|X|X")
            a = input('move: ')
            if a == '3':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '5':
                print("O|X| \n------\nO|O|X\n------\nO|X|X")
            elif a == '2':
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" | | \n------\n |O|X\n------\nO|X|X")
            a = input('move: ')
            if a == '0':
                print("O| | \n------\n |O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("O| | \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O| \n------\nX|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X| \n------\n |O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X| \n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print(" | | \n------\nO|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print(" |X| \n------\nO|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X| \n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X| | \n------\nO|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O| \n------\nO|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O| \n------\n |O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print(" |O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O| \n------\nX|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X|O| \n------\n |O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O| \n------\nO|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| | \n------\nO|O| \n------\nO|X|X")
            a = input('move: ')
            if a == '2':
                print("X| |X\n------\nO|O| \n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("X|O|X\n------\nO|O| \n------\nO|X|X")
                    a = input('move: ')
                    if a == '5':
                        print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("X| | \n------\nO|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("X|O| \n------\nO|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| | \n------\nX|O| \n------\nO|X|X")
            a = input('move: ')
            if a == '5':
                print("O| | \n------\nX|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '2':
            print(" | |X\n------\n |O|O\n------\nO|X|X")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\n |O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X| |X\n------\nO|O|O\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '6':
        print(" | | \n------\n |O| \n------\nX|O|X")
        a = input('move: ')
        if a == '2':
            print(" | |X\n------\n |O| \n------\nX|O|X")
            a = input('move: ')
            if a == '3':
                print(" | |X\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X| |X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O| \n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O| |X\n------\nX|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O| \n------\nX|O|X")
                    elif a == '5':
                        print("O| |X\n------\nX|O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\n |O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X|X\n------\n |O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X| \n------\nO|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print(" |X|X\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nX|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| | \n------\nO|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
            elif a == '2':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            elif a == '1':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| | \n------\nX|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '1':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
            elif a == '2':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("O|X| \n------\n |O| \n------\n | |X")
        a = input('move: ')
        if a == '5':
            print("O|X|O\n------\n |O|X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            elif a == '7':
                print("O|X|O\n------\n |O|X\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X| \n------\n |O| \n------\nX|O|X")
            a = input('move: ')
            if a == '5':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X| \n------\n |O| \n------\n |X|X")
            a = input('move: ')
            if a == '2':
                print("O|X|O\n------\n |O| \n------\n |X|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\n |O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|O\n------\nX|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O|X|O\n------\nX|O| \n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X| \n------\nO|O| \n------\n |X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nO|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|O| \n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X| \n------\nO|O|X\n------\nO|X|X")
                    elif a == '2':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O|X| \n------\nO|O| \n------\nX|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X| \n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X| \n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X| \n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '3':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X|O\n------\nX|O| \n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '6':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X| | \n------\n |O|O\n------\n | |X")
        a = input('move: ')
        if a == '3':
            print("X| | \n------\nX|O|O\n------\nO| |X")
            a = input('move: ')
            if a == '1':
                print("X|X| \n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|X| \n------\nX|O|O\n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X| | \n------\nO|O|O\n------\n |X|X")
        elif a == '1':
            print("X|X| \n------\nO|O|O\n------\n | |X")
        elif a == '2':
            print("X| |X\n------\nO|O|O\n------\n | |X")
        elif a == '6':
            print("X| | \n------\nO|O|O\n------\nX| |X")
        else:
            print('INVALID MOVE')
    elif a == '3':
        print(" | | \n------\nX|O| \n------\nO| |X")
        a = input('move: ')
        if a == '0':
            print("X|O| \n------\nX|O| \n------\nO| |X")
            a = input('move: ')
            if a == '2':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            elif a == '5':
                print("X|O| \n------\nX|O|X\n------\nO|O|X")
            elif a == '7':
                print("X|O|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O| | \n------\nX|O| \n------\nO|X|X")
            a = input('move: ')
            if a == '2':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '5':
                print("O| | \n------\nX|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\nX|O| \n------\nO| |X")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '5':
                print("O|X| \n------\nX|O|X\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X| \n------\nX|O|X\n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print(" | |X\n------\nX|O|O\n------\nO| |X")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" | | \n------\nX|O|X\n------\nO| |X")
            a = input('move: ')
            if a == '7':
                print(" | | \n------\nX|O|X\n------\nO|O|X")
                a = input('move: ')
                if a == '0':
                    print("X| | \n------\nX|O|X\n------\nO|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O| \n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |X| \n------\nX|O|X\n------\nO|O|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X| \n------\nX|O|X\n------\nO|O|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| | \n------\nX|O|X\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O| | \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O| \n------\nX|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X| \n------\nX|O|X\n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X| \n------\nX|O|X\n------\nO|O|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O| \n------\nX|O|X\n------\nO| |X")
                a = input('move: ')
                if a == '0':
                    print("X|O| \n------\nX|O|X\n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O| \n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print(" |O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O| \n------\nX|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '2':
        print(" | |X\n------\n |O|O\n------\n | |X")
        a = input('move: ')
        if a == '0':
            print("X| |X\n------\nO|O|O\n------\n | |X")
        elif a == '7':
            print(" | |X\n------\n |O|O\n------\n |X|X")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("X|O|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O| |X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O| |X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print(" | |X\n------\n |O|O\n------\nX| |X")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\n |O|O\n------\nX| |X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|X\n------\nX|O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O|O\n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\n |O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\n |O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|O|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O| |X\n------\nX|O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O| |X\n------\nX|O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| |X\n------\nX|O|O\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '3':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print(" | |O\n------\n |O|X\n------\n | |X")
        a = input('move: ')
        if a == '0':
            print("X| |O\n------\nO|O|X\n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("X| |O\n------\nO|O|X\n------\nO|X|X")
            elif a == '6':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| |O\n------\nX|O|X\n------\n | |X")
            a = input('move: ')
            if a == '1':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            elif a == '6':
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
            elif a == '7':
                print("O| |O\n------\nX|O|X\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nX|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X|O\n------\nO|O|X\n------\n | |X")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            elif a == '6':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print(" |X|O\n------\nO|O|X\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("O|X|O\n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" | |O\n------\n |O|X\n------\n |X|X")
            a = input('move: ')
            if a == '0':
                print("O| |O\n------\n |O|X\n------\n |X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\n |O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O| |O\n------\nX|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O| |O\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print(" | |O\n------\nO|O|X\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X| |O\n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("X| |O\n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |X|O\n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O|O\n------\n |O|X\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|O\n------\n |O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|O\n------\nX|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|O\n------\nX|O|X\n------\n |X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '3':
    print("O| | \n------\nX| | \n------\n | | ")
    a = input('move: ')
    if a == '2':
        print("O| |X\n------\nX|O| \n------\n | | ")
        a = input('move: ')
        if a == '7':
            print("O| |X\n------\nX|O|O\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O| |X\n------\nX|O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| |X\n------\nX|O|O\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O| |X\n------\nX|O|X\n------\n | | ")
            a = input('move: ')
            if a == '6':
                print("O| |X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O| |X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|O|X\n------\nX|O|X\n------\n | | ")
                a = input('move: ')
                if a == '6':
                    print("O|O|X\n------\nX|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|O|X\n------\nX|O|X\n------\n |X| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O| |X\n------\nX|O|X\n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O| |X\n------\nX|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\nX|O|X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|O|X\n------\nX|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            elif a == '5':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            elif a == '7':
                print("O|O|X\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print("O| | \n------\nX| |X\n------\n | | ")
        a = input('move: ')
        if a == '2':
            print("O| |O\n------\nX| |X\n------\n | | ")
            a = input('move: ')
            if a == '8':
                print("O| |O\n------\nX| |X\n------\n | |X")
                a = input('move: ')
                if a == '6':
                    print("O| |O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O| |O\n------\nX| |X\n------\nX| | ")
                a = input('move: ')
                if a == '8':
                    print("O| |O\n------\nX| |X\n------\nX| |O")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|O|O\n------\nX| |X\n------\nX| | ")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX| |X\n------\n | | ")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nX|X|X\n------\nO| | ")
                    elif a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|O| \n------\nX| |X\n------\n | | ")
            a = input('move: ')
            if a == '6':
                print("O|O| \n------\nX| |X\n------\nX| | ")
                a = input('move: ')
                if a == '4':
                    print("O|O| \n------\nX|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nX| | ")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|O| \n------\nX|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O| \n------\nX|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|O| \n------\nX|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|O| \n------\nX| |X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX| |X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|O|X\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|O| \n------\nX|X|X\n------\nX|O| ")
                    elif a == '8':
                        print("O|O| \n------\nX| |X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|O| \n------\nX|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| | \n------\nX| |X\n------\n | |O")
            a = input('move: ')
            if a == '1':
                print("O|X| \n------\nX| |X\n------\n | |O")
                a = input('move: ')
                if a == '6':
                    print("O|X| \n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X| \n------\nX|X|X\n------\nO| |O")
                    elif a == '7':
                        print("O|X| \n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|X\n------\nO|X|O")
                        elif a == '2':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|X|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O| | \n------\nX| |X\n------\nX| |O")
                a = input('move: ')
                if a == '2':
                    print("O| |O\n------\nX| |X\n------\nX| |O")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|O| \n------\nX| |X\n------\nX| |O")
                    a = input('move: ')
                    if a == '4':
                        print("O|O| \n------\nX|X|X\n------\nX| |O")
                    elif a == '2':
                        print("O|O|X\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|O|X\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|O|X\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|O|X\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|O| \n------\nX| |X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|O| \n------\nX|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |X\n------\nX| |X\n------\n | |O")
                a = input('move: ')
                if a == '6':
                    print("O| |X\n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|X\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|O|X\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("O|O|X\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|O|X\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|O|X\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|O|X\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O| | \n------\nX| |X\n------\nO| | ")
            a = input('move: ')
            if a == '1':
                print("O|X| \n------\nX| |X\n------\nO| | ")
                a = input('move: ')
                if a == '8':
                    print("O|X| \n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|X| \n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X| \n------\nX|O|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X| \n------\nX|X|X\n------\nO| |O")
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("O|X| \n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX|O|X\n------\nO| | ")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X| \n------\nX|O|X\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X| \n------\nX|O|X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|X| \n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|X|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|X|X\n------\nO| | ")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|X| \n------\nX| |X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX| |X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X| \n------\nX|X|X\n------\nO|O| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("O|X| \n------\nX| |O\n------\n | | ")
        a = input('move: ')
        if a == '8':
            print("O|X| \n------\nX|O|O\n------\n | |X")
            a = input('move: ')
            if a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X| \n------\nX|O|O\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|X| \n------\nX|O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\nX| |O\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|X\n------\nX|O|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nX| |O\n------\nO|O|X")
                a = input('move: ')
                if a == '4':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|O\n------\nX| |O\n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX| |O\n------\nX|X| ")
                a = input('move: ')
                if a == '4':
                    print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nX| |O\n------\nX|O|X")
                a = input('move: ')
                if a == '4':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '6':
        print("O|O| \n------\nX| | \n------\nX| | ")
        a = input('move: ')
        if a == '4':
            print("O|O| \n------\nX|X| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|O| \n------\nX|X| \n------\nX|O| ")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X| \n------\nX|O| ")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|O| \n------\nX|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
            elif a == '2':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            elif a == '7':
                print("O|O|O\n------\nX|O|X\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|O| \n------\nX| | \n------\nX| |X")
            a = input('move: ')
            if a == '4':
                print("O|O| \n------\nX|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|O| \n------\nX|O| \n------\nX|X|X")
                elif a == '2':
                    print("O|O|X\n------\nX|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|O|X\n------\nX|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|O| \n------\nX|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|O| \n------\nX|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|O|X\n------\nX|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|O|X\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            elif a == '8':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|O| \n------\nX| | \n------\nX|X| ")
            a = input('move: ')
            if a == '4':
                print("O|O| \n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|O| \n------\nX|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '7':
        print("O| | \n------\nX|O| \n------\n |X| ")
        a = input('move: ')
        if a == '2':
            print("O| |X\n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '5':
                print("O| |X\n------\nX|O|X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O| | \n------\nX|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '5':
                print("O| | \n------\nX|O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O| |X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X| \n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |O\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O| |O\n------\nX|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|O| \n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O| \n------\nX|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|O|X\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| | \n------\nX|O| \n------\nO|X|X")
            a = input('move: ')
            if a == '2':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O| | \n------\nX|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O| | \n------\nX|O|X\n------\nO|X| ")
            a = input('move: ')
            if a == '8':
                print("O| | \n------\nX|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |X\n------\nX|O|X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print("O| |O\n------\nX| | \n------\n | |X")
        a = input('move: ')
        if a == '1':
            print("O|X|O\n------\nX|O| \n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            elif a == '7':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("O| |O\n------\nX|X|O\n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("O| |O\n------\nX|X|O\n------\n |X|X")
                a = input('move: ')
                if a == '6':
                    print("O| |O\n------\nX|X|O\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|O|O\n------\nX|X|O\n------\nX| |X")
            elif a == '1':
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|O|O\n------\nX| | \n------\nX| |X")
        elif a == '7':
            print("O| |O\n------\nX| | \n------\nO|X|X")
            a = input('move: ')
            if a == '5':
                print("O|O|O\n------\nX| |X\n------\nO|X|X")
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '4':
                print("O|O|O\n------\nX|X| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O| |O\n------\nX| |X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O| |O\n------\nX| |X\n------\nO| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|O|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|O|X\n------\nO| |X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '4':
        print("O| | \n------\nX|X|O\n------\n | | ")
        a = input('move: ')
        if a == '6':
            print("O| | \n------\nX|X|O\n------\nX| | ")
            a = input('move: ')
            if a == '1':
                print("O|O| \n------\nX|X|O\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|O| \n------\nX|X|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|O\n------\nX|X|O\n------\nX|X| ")
                    elif a == '8':
                        print("O|O| \n------\nX|X|O\n------\nX|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|X|O\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O| | \n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '1':
                    print("O|X| \n------\nX|X|O\n------\nX|O| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X| \n------\nX|X|O\n------\nX|O|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| | \n------\nX|X|O\n------\n |O|X")
            a = input('move: ')
            if a == '2':
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O| |O\n------\nX|X|O\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O| |X\n------\nX|X|O\n------\nO| | ")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|O| \n------\nX|X|O\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|O|O\n------\nX|X|O\n------\nX|X| ")
            elif a == '2':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '2':
    print(" | |X\n------\n |O| \n------\n | | ")
    a = input('move: ')
    if a == '6':
        print(" | |X\n------\nO|O| \n------\nX| | ")
        a = input('move: ')
        if a == '7':
            print(" | |X\n------\nO|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|X\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print(" |O|X\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print(" |O|X\n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O| |X\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            elif a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("O|X|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" | |X\n------\nO|O|X\n------\nX| |O")
            a = input('move: ')
            if a == '0':
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
            elif a == '7':
                print("O| |X\n------\nO|O|X\n------\nX|X|O")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" | |X\n------\nO|O| \n------\nX| |X")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print(" | |X\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print(" |X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X| |X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print(" | |X\n------\n |O|X\n------\n | |O")
        a = input('move: ')
        if a == '7':
            print("O| |X\n------\n |O|X\n------\n |X|O")
        elif a == '1':
            print("O|X|X\n------\n |O|X\n------\n | |O")
        elif a == '6':
            print("O| |X\n------\n |O|X\n------\nX| |O")
        elif a == '0':
            print("X|O|X\n------\n |O|X\n------\n | |O")
            a = input('move: ')
            if a == '6':
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|X\n------\nX|O|X\n------\nO| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| |X\n------\nX|O|X\n------\n | |O")
        else:
            print('INVALID MOVE')
    elif a == '8':
        print(" | |X\n------\n |O|O\n------\n | |X")
        a = input('move: ')
        if a == '6':
            print(" | |X\n------\n |O|O\n------\nX| |X")
            a = input('move: ')
            if a == '0':
                print("O| |X\n------\n |O|O\n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\n |O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\n |O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|O|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O| |X\n------\nX|O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O| |X\n------\nX|O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O|X\n------\n |O|O\n------\nX| |X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|X\n------\nX|O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| |X\n------\nO|O|O\n------\n | |X")
        elif a == '1':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '3':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print(" | |X\n------\nX|O|O\n------\n |O|X")
            a = input('move: ')
            if a == '0':
                print("X| |X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("X| |X\n------\nX|O|O\n------\nO|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O| |X\n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" | |X\n------\n |O|O\n------\n |X|X")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("X|O|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O| |X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O| |X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '7':
        print(" | |X\n------\n |O|O\n------\n |X| ")
        a = input('move: ')
        if a == '3':
            print(" | |X\n------\nX|O|O\n------\nO|X| ")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print(" | |X\n------\n |O|O\n------\nX|X| ")
            a = input('move: ')
            if a == '1':
                print(" |O|X\n------\n |O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                    elif a == '8':
                        print("X|O|X\n------\n |O|O\n------\nX|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O| |X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\n |O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| |X\n------\nO|O|O\n------\n |X| ")
        elif a == '1':
            print("O|X|X\n------\n |O|O\n------\n |X| ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '3':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" | |X\n------\n |O|O\n------\n |X|X")
            a = input('move: ')
            if a == '0':
                print("O| |X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O| |X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O| |X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O|X\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("X|O|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |O|X\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '3':
        print(" | |X\n------\nX|O| \n------\nO| | ")
        a = input('move: ')
        if a == '5':
            print(" | |X\n------\nX|O|X\n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print(" | |X\n------\nX|O|X\n------\nO|O| ")
                a = input('move: ')
                if a == '0':
                    print("X| |X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|X\n------\nX|O|X\n------\nO|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |O|X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print(" |O|X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |O|X\n------\nX|O|X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X|O|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|X\n------\nX|O|X\n------\nO| |O")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("X|O|X\n------\nX|O|X\n------\nO|O| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O| |X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|O|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            elif a == '8':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O| |X\n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O| |X\n------\nX|O|X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" | |X\n------\nX|O|O\n------\nO| |X")
            a = input('move: ')
            if a == '7':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X|O|X\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '3':
            print("X|O|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            elif a == '8':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            elif a == '7':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            elif a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X|O|X\n------\n |O|O\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '8':
                print("X|O|X\n------\nO|O|O\n------\n |X|X")
            elif a == '3':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|O|X\n------\n |O|X\n------\n | |O")
            a = input('move: ')
            if a == '3':
                print("X|O|X\n------\nX|O|X\n------\nO| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|O|X\n------\n |O| \n------\n | |X")
            a = input('move: ')
            if a == '3':
                print("X|O|X\n------\nO|O| \n------\n | |X")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O|X\n------\nO|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("X|O|X\n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O|X\n------\n |O| \n------\nO| |X")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|O| \n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nX|O| \n------\nO|O|X")
                    elif a == '5':
                        print("X|O|X\n------\nX|O|O\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O|X\n------\n |O| \n------\nO|X|X")
                    a = input('move: ')
                    if a == '5':
                        print("X|O|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("X|O|X\n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("O|X|X\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '3':
            print("O|X|X\n------\nX|O| \n------\n |O| ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nX|O|X\n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nX|O|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|X|X\n------\n |O|X\n------\n | | ")
            a = input('move: ')
            if a == '7':
                print("O|X|X\n------\n |O|X\n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\n |O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nX|O|X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|X\n------\nO|O|X\n------\n | | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\n |X| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O|X|X\n------\nO|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\n |O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\n |O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            elif a == '3':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("O|X|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X|X\n------\nO|O| \n------\n |X| ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '5':
    print(" | |O\n------\n | |X\n------\n | | ")
    a = input('move: ')
    if a == '7':
        print("O| |O\n------\n | |X\n------\n |X| ")
        a = input('move: ')
        if a == '6':
            print("O| |O\n------\n | |X\n------\nX|X| ")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nO| |X\n------\nX|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nO| |X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X|O\n------\nO| |X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("O| |O\n------\nO|X|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O| |O\n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|O\n------\nO|X|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| |O\n------\n | |X\n------\n |X|X")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nO| |X\n------\n |X|X")
                a = input('move: ')
                if a == '6':
                    print("O| |O\n------\nO| |X\n------\nX|X|X")
                elif a == '1':
                    print("O|X|O\n------\nO| |X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO| |X\n------\nO|X|X")
                    elif a == '4':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("O| |O\n------\nO|X|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O| |O\n------\nO|X|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| |O\n------\nX| |X\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O| |O\n------\nX| |X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX| |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O| |O\n------\nX| |X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX| |X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |O\n------\nX| |X\n------\n |X|O")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX| |X\n------\n |X|O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O| |O\n------\nX| |X\n------\nX|X|O")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX| |X\n------\nX|X|O")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("O| |O\n------\n |X|X\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O| |O\n------\n |X|X\n------\nO|X| ")
                a = input('move: ')
                if a == '3':
                    print("O| |O\n------\nX|X|X\n------\nO|X| ")
                elif a == '8':
                    print("O| |O\n------\n |X|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O| |O\n------\nO|X|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |O\n------\n |X|X\n------\n |X|O")
                a = input('move: ')
                if a == '3':
                    print("O| |O\n------\nX|X|X\n------\n |X|O")
                elif a == '6':
                    print("O| |O\n------\n |X|X\n------\nX|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("O| |O\n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nO|X|X\n------\n |X| ")
                a = input('move: ')
                if a == '6':
                    print("O| |O\n------\nO|X|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O| |O\n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|O\n------\nO|X|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O| |O\n------\nO|X|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O| |O\n------\nO|X|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|O\n------\n | |X\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\n | |X\n------\nO|X| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX| |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                    elif a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|O\n------\n | |X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO| |X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nO| |X\n------\n |X| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nO| |X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nO| |X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|O\n------\nO| |X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO| |X\n------\nO|X|X")
                    elif a == '4':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\n | |X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\n | |X\n------\nX|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO| |X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|O\n------\nX| |X\n------\n |X|O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print("O| |O\n------\n | |X\n------\n | |X")
        a = input('move: ')
        if a == '3':
            print("O| |O\n------\nX| |X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O| |O\n------\nX| |X\n------\nO| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nX|O|X\n------\nO| |X")
                    elif a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|O|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|O\n------\nO| |X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nO| |X\n------\nX|O|X")
                a = input('move: ')
                if a == '4':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|O\n------\nO| |X\n------\nO|X|X")
            elif a == '4':
                print("O|X|O\n------\nO|X|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("O| |O\n------\nO|X|X\n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("O| |O\n------\nO|X|X\n------\nO|X|X")
            elif a == '6':
                print("O|O|O\n------\nO|X|X\n------\nX| |X")
            elif a == '1':
                print("O|X|O\n------\nO|X|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O| |O\n------\n | |X\n------\n |X|X")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nO| |X\n------\n |X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nO| |X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO| |X\n------\nO|X|X")
                    elif a == '4':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("O| |O\n------\nO|X|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O| |O\n------\nO|X|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O| |O\n------\nO| |X\n------\nX|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O| |O\n------\n | |X\n------\nX| |X")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nO| |X\n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nO| |X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|O\n------\nO| |X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("O| |O\n------\nO|X|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O| |O\n------\nO|X|X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|O\n------\nO|X|X\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '6':
        print(" | |O\n------\nO| |X\n------\nX| | ")
        a = input('move: ')
        if a == '8':
            print(" | |O\n------\nO| |X\n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nO| |X\n------\nX|O|X")
                a = input('move: ')
                if a == '4':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("O| |O\n------\nO|X|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| |O\n------\nO| |X\n------\nX|O| ")
            a = input('move: ')
            if a == '1':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("X| |O\n------\nO|X|X\n------\nX|O|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X|O\n------\nO| |X\n------\nX|O| ")
            a = input('move: ')
            if a == '4':
                print(" |X|O\n------\nO|X|X\n------\nX|O|O")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO| |X\n------\nX|O|O")
                a = input('move: ')
                if a == '4':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" | |O\n------\nO| |X\n------\nX|X|O")
            a = input('move: ')
            if a == '1':
                print(" |X|O\n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print(" |O|O\n------\nO|X|X\n------\nX|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|O\n------\nO| |X\n------\nX|X|O")
                a = input('move: ')
                if a == '4':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("O| |O\n------\nO|X|X\n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O|O\n------\nO|X|X\n------\nX| |X")
            elif a == '7':
                print("O|O|O\n------\nO|X|X\n------\nX|X| ")
            elif a == '1':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '3':
        print(" | |O\n------\nX| |X\n------\n | | ")
        a = input('move: ')
        if a == '6':
            print(" | |O\n------\nX| |X\n------\nO| | ")
            a = input('move: ')
            if a == '0':
                print("X| |O\n------\nX| |X\n------\nO| | ")
                a = input('move: ')
                if a == '1':
                    print("X|O|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|O|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X|O|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("X|O|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("X|O|O\n------\nX|X|X\n------\nO| | ")
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("X| |O\n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '1':
                        print("X|X|O\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |X|O\n------\nX| |X\n------\nO| | ")
                a = input('move: ')
                if a == '0':
                    print("O|X|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|X|X\n------\nO| | ")
                    elif a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print(" |X|O\n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print(" | |O\n------\nX| |X\n------\nO| |X")
                a = input('move: ')
                if a == '0':
                    print("O| |O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |O|O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '0':
                        print("X|O|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO| |X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |O|O\n------\nX| |X\n------\n | | ")
            a = input('move: ')
            if a == '8':
                print(" |O|O\n------\nX| |X\n------\n | |X")
                a = input('move: ')
                if a == '0':
                    print("O|O|O\n------\nX| |X\n------\n | |X")
                elif a == '6':
                    print(" |O|O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '0':
                        print("X|O|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("X|O|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print(" |O|O\n------\nX| |X\n------\nX| | ")
                a = input('move: ')
                if a == '4':
                    print(" |O|O\n------\nX|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '0':
                        print("X|O|O\n------\nX|O|X\n------\nX| | ")
                    elif a == '7':
                        print(" |O|O\n------\nX|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print(" |O|O\n------\nX|O|X\n------\nX|X|O")
                            a = input('move: ')
                            if a == '0':
                                print("X|O|O\n------\nX|O|X\n------\nX|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '0':
                            print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print(" |O|O\n------\nX|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '0':
                            print("O|O|O\n------\nX|O|X\n------\nX| |X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print(" |O|O\n------\nX| |X\n------\nX| |O")
                    a = input('move: ')
                    if a == '0':
                        print("X|O|O\n------\nX| |X\n------\nX| |O")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print(" |O|O\n------\nX| |X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '0':
                        print("X|O|O\n------\nX| |X\n------\nX|O| ")
                    elif a == '8':
                        print(" |O|O\n------\nX| |X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|O|O\n------\nX| |X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("O|O|O\n------\nX| |X\n------\nX| | ")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|O\n------\nX| |X\n------\n | | ")
                a = input('move: ')
                if a == '8':
                    print("X|O|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("X|O|O\n------\nX| |X\n------\nX| |O")
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("X|O|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("X|O|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("X|O|O\n------\nX|X|X\n------\nO| | ")
                    elif a == '7':
                        print("X|O|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|O|O\n------\nX|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|O|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O|O\n------\nX| |X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("X|O|O\n------\nX| |X\n------\nX|O| ")
                    elif a == '8':
                        print("X|O|O\n------\nX| |X\n------\n |O|X")
                        a = input('move: ')
                        if a == '6':
                            print("X|O|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|O|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("X|O|O\n------\nX|O|X\n------\n | | ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|O\n------\nX|O|X\n------\n | |X")
                        a = input('move: ')
                        if a == '6':
                            print("X|O|O\n------\nX|O|X\n------\nO| |X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("X|O|O\n------\nX|O|X\n------\nX| | ")
                    elif a == '7':
                        print("X|O|O\n------\nX|O|X\n------\n |X| ")
                        a = input('move: ')
                        if a == '6':
                            print("X|O|O\n------\nX|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|O|O\n------\nX|O|X\n------\n |X|O")
                            a = input('move: ')
                            if a == '6':
                                print("X|O|O\n------\nX|O|X\n------\nX|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("O| |O\n------\nX| |X\n------\n | | ")
            a = input('move: ')
            if a == '6':
                print("O| |O\n------\nX| |X\n------\nX| | ")
                a = input('move: ')
                if a == '1':
                    print("O|O|O\n------\nX| |X\n------\nX| | ")
                elif a == '8':
                    print("O| |O\n------\nX| |X\n------\nX| |O")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX| |X\n------\n | | ")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX| |X\n------\nO| | ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|X|X\n------\nO| | ")
                    elif a == '7':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |O\n------\nX| |X\n------\n | |X")
                a = input('move: ')
                if a == '6':
                    print("O| |O\n------\nX| |X\n------\nO| |X")
                    a = input('move: ')
                    if a == '1':
                        print("O|X|O\n------\nX| |X\n------\nO| |X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO| |X")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nO|O|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|O|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" | |O\n------\nX| |X\n------\n | |O")
            a = input('move: ')
            if a == '1':
                print(" |X|O\n------\nX| |X\n------\n | |O")
                a = input('move: ')
                if a == '6':
                    print(" |X|O\n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("O|X|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nX| |X\n------\nX| |O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nX| |O")
                        elif a == '7':
                            print("O|X|O\n------\nX| |X\n------\nX|O|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X| |O\n------\nX| |X\n------\n | |O")
                a = input('move: ')
                if a == '1':
                    print("X|O|O\n------\nX| |X\n------\n | |O")
                    a = input('move: ')
                    if a == '6':
                        print("X|O|O\n------\nX| |X\n------\nX| |O")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X| |O\n------\nX| |X\n------\n |O|O")
                    a = input('move: ')
                    if a == '6':
                        print("X| |O\n------\nX| |X\n------\nX|O|O")
                    elif a == '1':
                        print("X|X|O\n------\nX| |X\n------\n |O|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|X\n------\n |O|O")
                            a = input('move: ')
                            if a == '6':
                                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '6':
                            print("X|X|O\n------\nX| |X\n------\nO|O|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("X| |O\n------\nX|O|X\n------\n | |O")
                    a = input('move: ')
                    if a == '1':
                        print("X|X|O\n------\nX|O|X\n------\n | |O")
                        a = input('move: ')
                        if a == '6':
                            print("X|X|O\n------\nX|O|X\n------\nO| |O")
                        elif a == '7':
                            print("X|X|O\n------\nX|O|X\n------\n |O|O")
                            a = input('move: ')
                            if a == '6':
                                print("X|X|O\n------\nX|O|X\n------\nX|O|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("X| |O\n------\nX|O|X\n------\nX| |O")
                    elif a == '7':
                        print("X| |O\n------\nX|O|X\n------\n |X|O")
                        a = input('move: ')
                        if a == '6':
                            print("X| |O\n------\nX|O|X\n------\nO|X|O")
                        elif a == '1':
                            print("X|O|O\n------\nX|O|X\n------\n |X|O")
                            a = input('move: ')
                            if a == '6':
                                print("X|O|O\n------\nX|O|X\n------\nX|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("X| |O\n------\nX| |X\n------\nO| |O")
                    a = input('move: ')
                    if a == '1':
                        print("X|X|O\n------\nX| |X\n------\nO| |O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|X\n------\nO| |O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print(" |X|O\n------\n | |X\n------\n |O| ")
        a = input('move: ')
        if a == '0':
            print("X|X|O\n------\nO| |X\n------\n |O| ")
            a = input('move: ')
            if a == '8':
                print("X|X|O\n------\nO|O|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print(" |X|O\n------\nX|O|X\n------\n |O| ")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nX|O|X\n------\nO|O| ")
            elif a == '6':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nX|O|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" |X|O\n------\n |O|X\n------\n |O|X")
            a = input('move: ')
            if a == '3':
                print("O|X|O\n------\nX|O|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO|O|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print(" |X|O\n------\n |O|X\n------\nX|O| ")
            a = input('move: ')
            if a == '8':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print(" |X|O\n------\nO|X|X\n------\n |O| ")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print(" |X|O\n------\nO|X|X\n------\nX|O|O")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nO|X|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X| |O\n------\nO| |X\n------\n | | ")
        a = input('move: ')
        if a == '1':
            print("X|X|O\n------\nO| |X\n------\n | |O")
            a = input('move: ')
            if a == '4':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|X|O\n------\nO|O|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X| |O\n------\nO|O|X\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X| |O\n------\nO|O|X\n------\nO|X|X")
            elif a == '1':
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("X| |O\n------\nO| |X\n------\nX|O| ")
            a = input('move: ')
            if a == '4':
                print("X| |O\n------\nO|X|X\n------\nX|O|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nO| |X\n------\nX|O|O")
                a = input('move: ')
                if a == '4':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print("X| |O\n------\nO|X|X\n------\n | |O")
            a = input('move: ')
            if a == '6':
                print("X|O|O\n------\nO|X|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|O\n------\nO|X|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X| |O\n------\nO|O|X\n------\n | |X")
            a = input('move: ')
            if a == '1':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            elif a == '7':
                print("X| |O\n------\nO|O|X\n------\nO|X|X")
            elif a == '6':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '4':
        print(" | |O\n------\nO|X|X\n------\n | | ")
        a = input('move: ')
        if a == '6':
            print(" | |O\n------\nO|X|X\n------\nX| |O")
            a = input('move: ')
            if a == '0':
                print("X|O|O\n------\nO|X|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |X|O\n------\nO|X|X\n------\nX|O|O")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print(" |O|O\n------\nO|X|X\n------\nX|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| |O\n------\nO|X|X\n------\n | |O")
            a = input('move: ')
            if a == '1':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O|O\n------\nO|X|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|O\n------\nO|X|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X|O\n------\nO|X|X\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO|X|X\n------\n |O|O")
                a = input('move: ')
                if a == '6':
                    print("X|X|O\n------\nO|X|X\n------\nX|O|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nO|X|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| |O\n------\nO|X|X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|O|O\n------\nO|X|X\n------\nX| |X")
            elif a == '1':
                print("O|X|O\n------\nO|X|X\n------\nO| |X")
            elif a == '7':
                print("O| |O\n------\nO|X|X\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" |O|O\n------\nO|X|X\n------\n |X| ")
            a = input('move: ')
            if a == '8':
                print("O|O|O\n------\nO|X|X\n------\n |X|X")
            elif a == '0':
                print("X|O|O\n------\nO|X|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|O\n------\nO|X|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|O|O\n------\nO|X|X\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '7':
    print(" | | \n------\n | | \n------\nO|X| ")
    a = input('move: ')
    if a == '3':
        print(" | | \n------\nX| |O\n------\nO|X| ")
        a = input('move: ')
        if a == '1':
            print(" |X| \n------\nX|O|O\n------\nO|X| ")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nX|O|O\n------\nO|X| ")
            elif a == '8':
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|O| \n------\nX| |O\n------\nO|X| ")
            a = input('move: ')
            if a == '4':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nX| |O\n------\nO|X|O")
                a = input('move: ')
                if a == '4':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|O| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" | | \n------\nX|O|O\n------\nO|X|X")
            a = input('move: ')
            if a == '2':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print(" |O|X\n------\nX| |O\n------\nO|X| ")
            a = input('move: ')
            if a == '0':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print(" |O|X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '4':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '4':
            print(" |O| \n------\nX|X|O\n------\nO|X| ")
            a = input('move: ')
            if a == '0':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print(" |O|X\n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X|O| \n------\n | | \n------\nO|X| ")
        a = input('move: ')
        if a == '4':
            print("X|O| \n------\n |X| \n------\nO|X|O")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|X| \n------\nO|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("X|O|X\n------\n | | \n------\nO|X|O")
            a = input('move: ')
            if a == '4':
                print("X|O|X\n------\nO|X| \n------\nO|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|X\n------\nX| |O\n------\nO|X|O")
                a = input('move: ')
                if a == '4':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("X|O|X\n------\nO| |X\n------\nO|X|O")
                a = input('move: ')
                if a == '4':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|O| \n------\n |O|X\n------\nO|X| ")
            a = input('move: ')
            if a == '3':
                print("X|O|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '2':
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|O| \n------\n |O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("X|O| \n------\nO|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("X|O| \n------\nX| | \n------\nO|X|O")
            a = input('move: ')
            if a == '4':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nX| |O\n------\nO|X|O")
                a = input('move: ')
                if a == '4':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("X|O| \n------\nX|O|X\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|O| \n------\n |O| \n------\nO|X|X")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\n |O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("X|O| \n------\nO|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|O\n------\nX|O| \n------\nO|X|X")
            elif a == '2':
                print("X|O|X\n------\n |O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print(" |X| \n------\n | | \n------\nO|X| ")
        a = input('move: ')
        if a == '0':
            print("O|X| \n------\n | | \n------\nO|X| ")
            a = input('move: ')
            if a == '3':
                print("O|X| \n------\nX| | \n------\nO|X| ")
                a = input('move: ')
                if a == '4':
                    print("O|X| \n------\nX|O| \n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X| \n------\nX|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|O\n------\nX|O| \n------\nO|X|X")
                        elif a == '5':
                            print("O|X| \n------\nX|O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|X\n------\nX|O| \n------\nO|X| ")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X| \n------\nX|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X| \n------\nX| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '4':
                        print("O|X| \n------\nX|X| \n------\nO|X|O")
                    elif a == '2':
                        print("O|X|X\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O| \n------\nO|X|O")
                        elif a == '5':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X| \n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|X\n------\nO|X|O")
                        elif a == '2':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\nX| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X| \n------\nX|X|O\n------\nO|X| ")
                    elif a == '8':
                        print("O|X| \n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X| \n------\nX|O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|X\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '8':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|X|O\n------\nX| | \n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O| \n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X|O\n------\nX|X| \n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\n | | \n------\nO|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|X|X\n------\n | |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\n | |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nO| |O\n------\nO|X|X")
                        elif a == '4':
                            print("O|X|X\n------\n |O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '3':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nO| | \n------\nO|X| ")
                elif a == '8':
                    print("O|X|X\n------\n | | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|X\n------\nX|O| \n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X|X\n------\n | |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nO| |X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X| \n------\n | |X\n------\nO|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|O\n------\n | |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X|O\n------\n | |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X| \n------\n | |X\n------\nO|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("O|X| \n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|X\n------\nO|X|O")
                        elif a == '2':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|X\n------\n | |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nO| |X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X| \n------\nO| |X\n------\nO|X| ")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\n | | \n------\nO|X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X| \n------\nO| | \n------\nO|X|X")
                elif a == '2':
                    print("O|X|O\n------\n | | \n------\nO|X|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\n | |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|O\n------\nX| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O| \n------\nO|X|X")
                        elif a == '5':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\n | |O\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X| \n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '2':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|X\n------\n | |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\n |O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '3':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '3':
                            print("O|X|X\n------\nO| |O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print(" |X| \n------\nO| | \n------\nO|X| ")
            a = input('move: ')
            if a == '8':
                print(" |X| \n------\nO| | \n------\nO|X|X")
                a = input('move: ')
                if a == '5':
                    print(" |X| \n------\nO| |O\n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("X|X| \n------\nO| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nO|O|O\n------\nO|X|X")
                        elif a == '2':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print(" |X|X\n------\nO| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|X\n------\nO| |O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("O|X| \n------\nO| | \n------\nO|X|X")
                elif a == '2':
                    print(" |X|O\n------\nO| | \n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nO| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O| \n------\nO|X|X")
                        elif a == '5':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print(" |X|O\n------\nO| |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print(" |X| \n------\nO| |X\n------\nO|X| ")
                a = input('move: ')
                if a == '2':
                    print(" |X|O\n------\nO| |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |X|O\n------\nO| |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("X|X|O\n------\nO| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("O|X| \n------\nO| |X\n------\nO|X| ")
                elif a == '8':
                    print(" |X| \n------\nO| |X\n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X| \n------\nO| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nO|O|X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nO|O|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '2':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print(" |X|X\n------\nO| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print(" |X|X\n------\nO|O|X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '0':
                                print("X|X|X\n------\nO|O|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '0':
                            print("O|X|X\n------\nO| |X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print(" |X|X\n------\nO| | \n------\nO|X| ")
                a = input('move: ')
                if a == '0':
                    print("O|X|X\n------\nO| | \n------\nO|X| ")
                elif a == '5':
                    print(" |X|X\n------\nO| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |X|X\n------\nO| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|X\n------\nO| |O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("X|X|X\n------\nO| |O\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print(" |X|X\n------\nO| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|X\n------\nO| | \n------\nO|X|O")
                    elif a == '5':
                        print(" |X|X\n------\nO| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print(" |X|X\n------\nO|O|X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '0':
                                print("X|X|X\n------\nO|O|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '0':
                            print("O|X|X\n------\nO| |X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print(" |X|X\n------\nO|O| \n------\nO|X| ")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|X\n------\nO|O| \n------\nO|X| ")
                    elif a == '8':
                        print(" |X|X\n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|X\n------\nO|O| \n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print(" |X|X\n------\nO|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                        elif a == '8':
                            print(" |X|X\n------\nO|O|X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '0':
                                print("X|X|X\n------\nO|O|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X| \n------\nO| | \n------\nO|X| ")
                a = input('move: ')
                if a == '4':
                    print("X|X| \n------\nO|O| \n------\nO|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("X|X| \n------\nO|O|X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '2':
                            print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|X| \n------\nO|O|X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nO|O|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X|X| \n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("X|X|O\n------\nO|O| \n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("X|X|X\n------\nO|O| \n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("X|X| \n------\nO| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '4':
                        print("X|X| \n------\nO|X| \n------\nO|X|O")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X|X| \n------\nO| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("X|X| \n------\nO|X|O\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|X|O\n------\nO| | \n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("X|X|O\n------\nO|X| \n------\nO|X| ")
                    elif a == '5':
                        print("X|X|O\n------\nO| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X|X|O\n------\nO| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("X|X|O\n------\nO|O| \n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" |X| \n------\n | |O\n------\nO|X| ")
            a = input('move: ')
            if a == '0':
                print("X|X| \n------\n | |O\n------\nO|X| ")
                a = input('move: ')
                if a == '3':
                    print("X|X| \n------\nO| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("X|X| \n------\nO|X|O\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|X|O\n------\n | |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|X|O\n------\n | |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("X|X|O\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("X|X| \n------\n |O|O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("X|X| \n------\nX|O|O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '2':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("X|X| \n------\n | |O\n------\nO|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("X|X| \n------\nX| |O\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print(" |X| \n------\nX| |O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print(" |X| \n------\nX| |O\n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X| \n------\nX| |O\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print(" |X|O\n------\nX| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print(" |X|O\n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print(" |X| \n------\nX|O|O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '2':
                        print(" |X|X\n------\nX|O|O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '8':
                            print(" |X|X\n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '0':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print(" |X| \n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X| \n------\nX|O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("X|X| \n------\nX|O|O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '2':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        elif a == '8':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("O|X| \n------\nX| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X| \n------\nX|X|O\n------\nO|X| ")
                    elif a == '2':
                        print("O|X|X\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                            a = input('move: ')
                            if a == '8':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X| \n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '2':
                                print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        elif a == '2':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print(" |X|O\n------\n | | \n------\nO|X| ")
            a = input('move: ')
            if a == '5':
                print(" |X|O\n------\n | |X\n------\nO|X| ")
                a = input('move: ')
                if a == '0':
                    print("O|X|O\n------\n | |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X|O\n------\n | |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |X|O\n------\nO| |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nO| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print(" |X|O\n------\nO| |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print(" |X|O\n------\n | |X\n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\n | |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print(" |X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\n | | \n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\n | | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '5':
                        print("X|X|O\n------\n | |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("X|X|O\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O| \n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X|X|O\n------\n | |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|X|O\n------\n | |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("X|X|O\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("X|X|O\n------\nO| | \n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("X|X|O\n------\nO|X| \n------\nO|X| ")
                    elif a == '5':
                        print("X|X|O\n------\nO| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O|X\n------\nO|X| ")
                        elif a == '8':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X|X|O\n------\nO| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O| \n------\nO|X|X")
                        elif a == '5':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print(" |X|O\n------\n | | \n------\nO|X|X")
                a = input('move: ')
                if a == '0':
                    print("O|X|O\n------\n | | \n------\nO|X|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\n | |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|O\n------\nX| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O| \n------\nO|X|X")
                        elif a == '5':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |X|O\n------\nO| | \n------\nO|X|X")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nO| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nO|O| \n------\nO|X|X")
                        elif a == '5':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print(" |X|O\n------\nO| |X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nO| |X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print(" |X|O\n------\n | |O\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print(" |X|O\n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("X|X|O\n------\n | |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print(" |X|O\n------\nX| | \n------\nO|X| ")
                a = input('move: ')
                if a == '0':
                    print("O|X|O\n------\nX| | \n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nX|X| \n------\nO|X| ")
                    elif a == '8':
                        print("O|X|O\n------\nX| | \n------\nO|X|X")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|O| \n------\nO|X|X")
                        elif a == '5':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X|O\n------\nX| |X\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        elif a == '4':
                            print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print(" |X|O\n------\nX| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O| \n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print(" |X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print(" |X|O\n------\nX| |O\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |X|O\n------\nX| |O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |O\n------\nO|X|X")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|O\n------\nO|X|X")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("X|X|O\n------\nX| |O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O|O\n------\nO|X| ")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" |X| \n------\n | | \n------\nO|X|O")
            a = input('move: ')
            if a == '3':
                print(" |X| \n------\nX| | \n------\nO|X|O")
                a = input('move: ')
                if a == '0':
                    print("O|X| \n------\nX| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|X\n------\nX|O| \n------\nO|X|O")
                        elif a == '5':
                            print("O|X|X\n------\nX| |O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|X\n------\nX|X|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X| \n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X| \n------\nX|O|X\n------\nO|X|O")
                        elif a == '2':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X| \n------\nX|X| \n------\nO|X|O")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print(" |X|O\n------\nX| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X|O\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O| \n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print(" |X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("O|X|O\n------\nX| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print(" |X| \n------\nX| |O\n------\nO|X|O")
                    a = input('move: ')
                    if a == '0':
                        print("X|X| \n------\nX| |O\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X| \n------\n | | \n------\nO|X|O")
                a = input('move: ')
                if a == '3':
                    print("X|X| \n------\nO| | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '4':
                        print("X|X| \n------\nO|X| \n------\nO|X|O")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|X|O\n------\n | | \n------\nO|X|O")
                    a = input('move: ')
                    if a == '5':
                        print("X|X|O\n------\n | |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '3':
                            print("X|X|O\n------\nO| |X\n------\nO|X|O")
                            a = input('move: ')
                            if a == '4':
                                print("X|X|O\n------\nO|X|X\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("X|X|O\n------\nX| | \n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X|O\n------\nX|O| \n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '4':
                    print("X|X| \n------\n |O| \n------\nO|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("X|X| \n------\nX|O| \n------\nO|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("X|X|O\n------\nX|O| \n------\nO|X|O")
                        elif a == '5':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X|X| \n------\n | |O\n------\nO|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("X|X| \n------\nX| |O\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("X|X| \n------\nX|O|O\n------\nO|X|O")
                            a = input('move: ')
                            if a == '2':
                                print("X|X|X\n------\nX|O|O\n------\nO|X|O")
                            else:
                                print('INVALID MOVE')
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '4':
        print(" |O| \n------\n |X| \n------\nO|X| ")
        a = input('move: ')
        if a == '2':
            print(" |O|X\n------\n |X| \n------\nO|X|O")
            a = input('move: ')
            if a == '5':
                print(" |O|X\n------\nO|X|X\n------\nO|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O|X\n------\n |X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print(" |O|X\n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|O| \n------\n |X| \n------\nO|X|O")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|X| \n------\nO|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print(" |O| \n------\nX|X|O\n------\nO|X| ")
            a = input('move: ')
            if a == '2':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|O| \n------\nX|X|O\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|X|O\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" |O| \n------\nO|X|X\n------\nO|X| ")
            a = input('move: ')
            if a == '2':
                print("O|O|X\n------\nO|X|X\n------\nO|X| ")
            elif a == '0':
                print("X|O| \n------\nO|X|X\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|X|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O| \n------\nO|X|X\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|O| \n------\n |X| \n------\nO|X|X")
            a = input('move: ')
            if a == '3':
                print("O|O|O\n------\nX|X| \n------\nO|X|X")
            elif a == '2':
                print("O|O|X\n------\nO|X| \n------\nO|X|X")
            elif a == '5':
                print("O|O| \n------\nO|X|X\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '2':
        print("O| |X\n------\n | | \n------\nO|X| ")
        a = input('move: ')
        if a == '3':
            print("O| |X\n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '8':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O| |X\n------\nX|O|X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|O|X\n------\nX|O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O| |X\n------\nO| |X\n------\nO|X| ")
        elif a == '4':
            print("O| |X\n------\nO|X| \n------\nO|X| ")
        elif a == '1':
            print("O|X|X\n------\nO| | \n------\nO|X| ")
        elif a == '8':
            print("O| |X\n------\nO| | \n------\nO|X|X")
        else:
            print('INVALID MOVE')
    elif a == '8':
        print("O| | \n------\n | | \n------\nO|X|X")
        a = input('move: ')
        if a == '4':
            print("O| | \n------\nO|X| \n------\nO|X|X")
        elif a == '2':
            print("O| |X\n------\nO| | \n------\nO|X|X")
        elif a == '5':
            print("O| | \n------\nO| |X\n------\nO|X|X")
        elif a == '1':
            print("O|X| \n------\nO| | \n------\nO|X|X")
        elif a == '3':
            print("O| | \n------\nX|O| \n------\nO|X|X")
            a = input('move: ')
            if a == '5':
                print("O| | \n------\nX|O|X\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|O| \n------\nX|O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|X\n------\nX|O|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |X\n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print("O| | \n------\n | |X\n------\nO|X| ")
        a = input('move: ')
        if a == '4':
            print("O| | \n------\nO|X|X\n------\nO|X| ")
        elif a == '8':
            print("O| | \n------\nO| |X\n------\nO|X|X")
        elif a == '2':
            print("O| |X\n------\nO| |X\n------\nO|X| ")
        elif a == '1':
            print("O|X| \n------\nO| |X\n------\nO|X| ")
        elif a == '3':
            print("O| | \n------\nX| |X\n------\nO|X| ")
            a = input('move: ')
            if a == '2':
                print("O| |O\n------\nX| |X\n------\nO|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX| |X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '4':
                        print("O|X|O\n------\nX|O|X\n------\nO|X| ")
                    elif a == '8':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O| |O\n------\nX| |X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX| |X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| | \n------\nX| |X\n------\nO|X|O")
                a = input('move: ')
                if a == '1':
                    print("O|X| \n------\nX| |X\n------\nO|X|O")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|X|O\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '4':
                        print("O|X| \n------\nX|O|X\n------\nO|X|O")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O| |X\n------\nX| |X\n------\nO|X|O")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX| |X\n------\nO|X|O")
                        a = input('move: ')
                        if a == '4':
                            print("O|O|X\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|O| \n------\nX| |X\n------\nO|X| ")
                a = input('move: ')
                if a == '4':
                    print("O|O| \n------\nX|X|X\n------\nO|X| ")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '6':
    print(" | | \n------\n |O| \n------\nX| | ")
    a = input('move: ')
    if a == '2':
        print(" |O|X\n------\n |O| \n------\nX| | ")
        a = input('move: ')
        if a == '7':
            print(" |O|X\n------\n |O| \n------\nX|X|O")
            a = input('move: ')
            if a == '3':
                print("O|O|X\n------\nX|O| \n------\nX|X|O")
            elif a == '0':
                print("X|O|X\n------\nO|O| \n------\nX|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|O|X\n------\n |O|X\n------\nX|X|O")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|O|X\n------\nX|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            elif a == '7':
                print("O|O|X\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" |O|X\n------\n |O|X\n------\nX| | ")
            a = input('move: ')
            if a == '3':
                print(" |O|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nO|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|X\n------\nO|O|X\n------\nX| |O")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("X|O|X\n------\nO|O|X\n------\nX|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print(" |O|X\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |O|X\n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("O|O|X\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O|O|X\n------\n |O|X\n------\nX| | ")
                a = input('move: ')
                if a == '3':
                    print("O|O|X\n------\nX|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|O|X\n------\nX|O|X\n------\nX|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|O|X\n------\n |O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|O|X\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" |O|X\n------\n |O| \n------\nX| |X")
            a = input('move: ')
            if a == '3':
                print(" |O|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '0':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print(" |O|X\n------\n |O|O\n------\nX| |X")
                a = input('move: ')
                if a == '3':
                    print(" |O|X\n------\nX|O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '0':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X|O|X\n------\n |O|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O|O|X\n------\n |O| \n------\nX| |X")
                a = input('move: ')
                if a == '3':
                    print("O|O|X\n------\nX|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|O|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|O|X\n------\nX|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            elif a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print(" | | \n------\n |O| \n------\nX|O|X")
        a = input('move: ')
        if a == '2':
            print(" | |X\n------\n |O| \n------\nX|O|X")
            a = input('move: ')
            if a == '3':
                print(" | |X\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X| |X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print(" |X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O| |X\n------\n |O| \n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O| |X\n------\nX|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O| |X\n------\nX|O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|X\n------\nX|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|X\n------\n |O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("O|X|X\n------\n |O|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| | \n------\nX|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '2':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            elif a == '5':
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            a = input('move: ')
            if a == '1':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nX|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| | \n------\nO|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
            elif a == '1':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X| \n------\n |O|O\n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
            elif a == '3':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("O|X| \n------\n |O| \n------\nX| | ")
        a = input('move: ')
        if a == '2':
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '8':
                print("O|X|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X| \n------\nX|O| \n------\nX|O| ")
            a = input('move: ')
            if a == '5':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|X|O\n------\n |O|X\n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|O\n------\n |O|X\n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X| \n------\n |O| \n------\nX|X| ")
            a = input('move: ')
            if a == '5':
                print("O|X| \n------\n |O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\n |O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X| \n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X| \n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|O\n------\n |O| \n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X|O\n------\n |O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X| \n------\n |O| \n------\nX|O|X")
            a = input('move: ')
            if a == '3':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '7':
        print(" | | \n------\n |O| \n------\nX|X|O")
        a = input('move: ')
        if a == '0':
            print("X| | \n------\nO|O| \n------\nX|X|O")
            a = input('move: ')
            if a == '5':
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nO|O| \n------\nX|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|O| \n------\nX|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\n |O| \n------\nX|X|O")
        elif a == '5':
            print("O| | \n------\n |O|X\n------\nX|X|O")
        elif a == '2':
            print("O| |X\n------\n |O| \n------\nX|X|O")
        elif a == '3':
            print("O| | \n------\nX|O| \n------\nX|X|O")
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X| | \n------\nO|O| \n------\nX| | ")
        a = input('move: ')
        if a == '1':
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|O| \n------\nO|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
            elif a == '7':
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X| | \n------\nO|O| \n------\nX| |X")
            a = input('move: ')
            if a == '2':
                print("X| |O\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|X|O\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X| |O\n------\nO|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("X| |O\n------\nO|O|X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|O| \n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '5':
                    print("X|O| \n------\nO|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O| \n------\nO|O|X\n------\nX|O|X")
                    elif a == '2':
                        print("X|O|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O| \n------\nO|O| \n------\nX|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X| | \n------\nO|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '2':
                print("X| |O\n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("X| |O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X| |O\n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("X|X|O\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("X|X|O\n------\nO|O|O\n------\nX|X| ")
                    elif a == '8':
                        print("X|X|O\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|O| \n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("X|O| \n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O| \n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("X|O|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|O|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|O|X\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '3':
        print("O| | \n------\nX|O| \n------\nX| | ")
        a = input('move: ')
        if a == '2':
            print("O|O|X\n------\nX|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            elif a == '5':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            elif a == '7':
                print("O|O|X\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O| | \n------\nX|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '1':
                print("O|O| \n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|O| \n------\nX|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|O|X\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |O\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O| |O\n------\nX|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX|O|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|O\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O| | \n------\nX|O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O| |X\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|X\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X| \n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| | \n------\nX|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '5':
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
            elif a == '2':
                print("O|O|X\n------\nX|O| \n------\nX|O|X")
            elif a == '1':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|O| \n------\nX|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|O| \n------\nX|O|X\n------\nX|O|X")
            elif a == '7':
                print("O|O|O\n------\nX|O|X\n------\nX|X| ")
            elif a == '2':
                print("O|O|X\n------\nX|O|X\n------\nX|O| ")
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\nX|O| \n------\nX|O| ")
            a = input('move: ')
            if a == '2':
                print("O|X|X\n------\nX|O|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print(" | |O\n------\n |O|X\n------\nX| | ")
        a = input('move: ')
        if a == '8':
            print(" | |O\n------\n |O|X\n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nX|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X| |O\n------\nO|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '1':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print(" |X|O\n------\n |O|X\n------\nX|O| ")
            a = input('move: ')
            if a == '3':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O| |O\n------\nX|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|O|O\n------\nX|O|X\n------\nX|X| ")
            elif a == '8':
                print("O|O|O\n------\nX|O|X\n------\nX| |X")
            elif a == '1':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" | |O\n------\n |O|X\n------\nX|X|O")
            a = input('move: ')
            if a == '1':
                print("O|X|O\n------\n |O|X\n------\nX|X|O")
            elif a == '0':
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nX|O|X\n------\nX|X|O")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '1':
    print(" |X| \n------\n |O| \n------\n | | ")
    a = input('move: ')
    if a == '7':
        print("O|X| \n------\n |O| \n------\n |X| ")
        a = input('move: ')
        if a == '5':
            print("O|X| \n------\nO|O|X\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|X| \n------\nO|O|X\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X| \n------\nO|O|X\n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X| \n------\n |O| \n------\nX|X| ")
            a = input('move: ')
            if a == '3':
                print("O|X| \n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|O\n------\n |O| \n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X|O\n------\n |O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X| \n------\n |O|O\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\n |O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X| \n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X| \n------\n |O| \n------\n |X|X")
            a = input('move: ')
            if a == '3':
                print("O|X| \n------\nO|O| \n------\n |X|X")
                a = input('move: ')
                if a == '5':
                    print("O|X| \n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X| \n------\nO|O|X\n------\nO|X|X")
                    elif a == '2':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O|X| \n------\nO|O| \n------\nX|X|X")
                elif a == '2':
                    print("O|X|X\n------\nO|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|O| \n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|O\n------\n |O| \n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O|X|O\n------\nX|O| \n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X|O\n------\n |O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|O\n------\nO|O|X\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X| \n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X| \n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X| \n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X| \n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\nO|O| \n------\n |X| ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '0':
        print("X|X|O\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '7':
            print("X|X|O\n------\nO|O| \n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("X|X|O\n------\nX|O| \n------\nO| | ")
        elif a == '6':
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|X|O\n------\nO|O| \n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|X|O\n------\nO|O|X\n------\n | | ")
            a = input('move: ')
            if a == '6':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            elif a == '7':
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print(" |X| \n------\n |O|O\n------\n | |X")
        a = input('move: ')
        if a == '3':
            print(" |X| \n------\nX|O|O\n------\nO| |X")
            a = input('move: ')
            if a == '0':
                print("X|X| \n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|X| \n------\nX|O|O\n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '0':
            print("X|X| \n------\nO|O|O\n------\n | |X")
        elif a == '7':
            print(" |X| \n------\n |O|O\n------\n |X|X")
            a = input('move: ')
            if a == '0':
                print("O|X| \n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X| \n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X| \n------\nX|O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("O|X|X\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|O\n------\n |X|X")
                    elif a == '6':
                        print("O|X|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print(" |X|O\n------\n |O|O\n------\n |X|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\n |O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|X|O\n------\nO|O|O\n------\n |X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print(" |X|O\n------\nX|O|O\n------\n |X|X")
                    a = input('move: ')
                    if a == '0':
                        print("O|X|O\n------\nX|O|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            elif a == '3':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print(" |X| \n------\n |O|O\n------\nX|O|X")
            a = input('move: ')
            if a == '0':
                print("X|X| \n------\nO|O|O\n------\nX|O|X")
            elif a == '2':
                print("O|X|X\n------\n |O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X| \n------\nX|O|O\n------\nX|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '2':
        print("O|X|X\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '5':
            print("O|X|X\n------\n |O|X\n------\n | | ")
            a = input('move: ')
            if a == '3':
                print("O|X|X\n------\nO|O|X\n------\n | | ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nO|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|X|X\n------\nO|O|X\n------\n |X| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\n |O|X\n------\nO| | ")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|X|X\n------\n |O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\n |O|X\n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\n |O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nX|O|X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X|X\n------\n |O|O\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX| |X")
            elif a == '3':
                print("O|X|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\n |X|X")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X|X\n------\nO|O| \n------\n |X| ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\nO|O| \n------\nO|X|X")
            elif a == '5':
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
            elif a == '6':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X|X\n------\nX|O| \n------\n |O| ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\nX|O|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|X\n------\nX|O|X\n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\nX|O|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|O|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '3':
        print(" |X|O\n------\nX|O| \n------\n | | ")
        a = input('move: ')
        if a == '0':
            print("X|X|O\n------\nX|O| \n------\nO| | ")
        elif a == '8':
            print("O|X|O\n------\nX|O| \n------\n | |X")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            elif a == '6':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|X|O\n------\nX|O|X\n------\n | | ")
            a = input('move: ')
            if a == '8':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            elif a == '7':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '6':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|X|O\n------\nX|O| \n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|O\n------\nX|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nX|O|O\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nX|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '6':
        print(" |X| \n------\nO|O| \n------\nX| | ")
        a = input('move: ')
        if a == '0':
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print(" |X| \n------\nO|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '2':
                print(" |X|O\n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print(" |X|O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print(" |X|O\n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '0':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '0':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '0':
                    print("X|X|O\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X|X|O\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("X|X|O\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("O|X| \n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|X| \n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print(" |X| \n------\nO|O|X\n------\nX| |O")
            a = input('move: ')
            if a == '0':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X| \n------\nO|O|X\n------\nX|X|O")
            elif a == '2':
                print("O|X|X\n------\nO|O|X\n------\nX| |O")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print(" |X| \n------\nO|O| \n------\nX|O|X")
            a = input('move: ')
            if a == '5':
                print(" |X|O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print(" |X|X\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '0':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '0':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '5':
                print("O|X|X\n------\nO|O|X\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|X\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nO|O| \n------\nX|O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print("O|X| \n------\n |O|X\n------\n | | ")
        a = input('move: ')
        if a == '7':
            print("O|X| \n------\nO|O|X\n------\n |X| ")
            a = input('move: ')
            if a == '8':
                print("O|X| \n------\nO|O|X\n------\nO|X|X")
            elif a == '2':
                print("O|X|X\n------\nO|O|X\n------\nO|X| ")
            elif a == '6':
                print("O|X| \n------\nO|O|X\n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|O\n------\n |O|X\n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\n |O|X\n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X| \n------\nX|O|X\n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print("O|X|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '8':
                print("O|X| \n------\nX|O|X\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|X| \n------\nX|O|X\n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|X|X\n------\n |O|X\n------\n | | ")
            a = input('move: ')
            if a == '3':
                print("O|X|X\n------\nO|O|X\n------\n | | ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nO|O|X\n------\nX| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("O|X|X\n------\nO|O|X\n------\n |X| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|X\n------\n |O|X\n------\nO| | ")
                a = input('move: ')
                if a == '7':
                    print("O|X|X\n------\n |O|X\n------\nO|X| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nO|X| ")
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nX|O|X\n------\nO| | ")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|X\n------\n |O|X\n------\n |O| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|O|X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nX|O|X\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|O|X\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O|X|X\n------\n |O|X\n------\nX|O| ")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|O|X\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X|O\n------\n |O|X\n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\n |O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|X|O\n------\n |O|X\n------\n |X|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nO|O|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|O\n------\nO|O|X\n------\nX|X|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|O|X\n------\nO| |X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '0':
    print("X| | \n------\n |O| \n------\n | | ")
    a = input('move: ')
    if a == '7':
        print("X| | \n------\n |O|O\n------\n |X| ")
        a = input('move: ')
        if a == '2':
            print("X| |X\n------\nO|O|O\n------\n |X| ")
        elif a == '6':
            print("X| | \n------\nO|O|O\n------\nX|X| ")
        elif a == '8':
            print("X| | \n------\nO|O|O\n------\n |X|X")
        elif a == '3':
            print("X| | \n------\nX|O|O\n------\nO|X| ")
            a = input('move: ')
            if a == '8':
                print("X|O| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|X|O\n------\nX|O|O\n------\nO|X| ")
            elif a == '2':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("X|X| \n------\nO|O|O\n------\n |X| ")
        else:
            print('INVALID MOVE')
    elif a == '2':
        print("X|O|X\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '3':
            print("X|O|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            elif a == '5':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|O|X\n------\n |O| \n------\n | |X")
            a = input('move: ')
            if a == '6':
                print("X|O|X\n------\n |O| \n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\n |O| \n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O|X\n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '5':
                        print("X|O|X\n------\n |O|O\n------\nO|X|X")
                        a = input('move: ')
                        if a == '3':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("X|O|X\n------\nX|O| \n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nX|O| \n------\nO|O|X")
                    elif a == '5':
                        print("X|O|X\n------\nX|O|O\n------\nO| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|X\n------\nO|O| \n------\n | |X")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O|X\n------\nO|O| \n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("X|O|X\n------\nO|O| \n------\nO|X|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|O|X\n------\n |O|X\n------\n | |O")
            a = input('move: ')
            if a == '3':
                print("X|O|X\n------\nX|O|X\n------\nO| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X|O|X\n------\n |O| \n------\n |X|O")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\n |O|X\n------\nO|X|O")
                a = input('move: ')
                if a == '3':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|X\n------\nX|O| \n------\nO|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O|X\n------\nO|O| \n------\nX|X|O")
                a = input('move: ')
                if a == '5':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print("X|O| \n------\n |O|X\n------\n | | ")
        a = input('move: ')
        if a == '2':
            print("X|O|X\n------\n |O|X\n------\n | |O")
            a = input('move: ')
            if a == '6':
                print("X|O|X\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("X|O|X\n------\nX|O|X\n------\nO| |O")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|O| \n------\n |O|X\n------\n | |X")
            a = input('move: ')
            if a == '3':
                print("X|O| \n------\nO|O|X\n------\n | |X")
                a = input('move: ')
                if a == '6':
                    print("X|O| \n------\nO|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O| \n------\nO|O|X\n------\nX|O|X")
                    elif a == '2':
                        print("X|O|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O| \n------\n |O|X\n------\nO| |X")
                a = input('move: ')
                if a == '3':
                    print("X|O| \n------\nX|O|X\n------\nO| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O| \n------\nX|O|X\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                elif a == '7':
                    print("X|O| \n------\n |O|X\n------\nO|X|X")
                    a = input('move: ')
                    if a == '3':
                        print("X|O| \n------\nO|O|X\n------\nO|X|X")
                        a = input('move: ')
                        if a == '2':
                            print("X|O|X\n------\nO|O|X\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("X|O| \n------\nO|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '2':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '8':
                print("X|O| \n------\nO|O|X\n------\nX|O|X")
            elif a == '7':
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X|O| \n------\n |O|X\n------\n |X|O")
            a = input('move: ')
            if a == '3':
                print("X|O| \n------\nX|O|X\n------\nO|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|X\n------\nO|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nO|O|X\n------\n |X|O")
                a = input('move: ')
                if a == '6':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("X|O| \n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("X|O| \n------\nX|O|X\n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print("X|O|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '2':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            elif a == '8':
                print("X|O| \n------\nX|O|X\n------\nO|O|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print("X| | \n------\n |O|O\n------\n | |X")
        a = input('move: ')
        if a == '3':
            print("X| | \n------\nX|O|O\n------\nO| |X")
            a = input('move: ')
            if a == '1':
                print("X|X| \n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|X| \n------\nX|O|O\n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|O| \n------\nX|O|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X|O|X\n------\nX|O|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("X|X| \n------\nO|O|O\n------\n | |X")
        elif a == '6':
            print("X| | \n------\nO|O|O\n------\nX| |X")
        elif a == '2':
            print("X| |X\n------\nO|O|O\n------\n | |X")
        elif a == '7':
            print("X| | \n------\nO|O|O\n------\n |X|X")
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("X|X|O\n------\n |O| \n------\n | | ")
        a = input('move: ')
        if a == '3':
            print("X|X|O\n------\nX|O| \n------\nO| | ")
        elif a == '6':
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '5':
                print("X|X|O\n------\nO|O|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X|X|O\n------\nO|O| \n------\n |X| ")
            a = input('move: ')
            if a == '5':
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
            elif a == '6':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|X|O\n------\nO|O|X\n------\n | | ")
            a = input('move: ')
            if a == '8':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            elif a == '6':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X|X|O\n------\nO|O|X\n------\nO|X| ")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|X|O\n------\nO|O| \n------\n | |X")
            a = input('move: ')
            if a == '5':
                print("X|X|O\n------\nO|O|X\n------\nO| |X")
            elif a == '7':
                print("X|X|O\n------\nO|O| \n------\nO|X|X")
            elif a == '6':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '3':
        print("X| | \n------\nX|O| \n------\nO| | ")
        a = input('move: ')
        if a == '1':
            print("X|X| \n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '7':
                print("X|X| \n------\nX|O| \n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("X|X| \n------\nX|O| \n------\nO|O|X")
                    a = input('move: ')
                    if a == '2':
                        print("X|X|O\n------\nX|O| \n------\nO|O|X")
                    elif a == '5':
                        print("X|X| \n------\nX|O|O\n------\nO|O|X")
                        a = input('move: ')
                        if a == '2':
                            print("X|X|X\n------\nX|O|O\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X|X| \n------\nX|O|X\n------\nO|O| ")
                    a = input('move: ')
                    if a == '2':
                        print("X|X|O\n------\nX|O|X\n------\nO|O| ")
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|X|X\n------\nX|O| \n------\nO|O| ")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X|O| \n------\nX|O|X\n------\nO| | ")
            a = input('move: ')
            if a == '8':
                print("X|O| \n------\nX|O|X\n------\nO|O|X")
            elif a == '7':
                print("X|O|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '2':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("X|O| \n------\nX|O| \n------\nO|X| ")
            a = input('move: ')
            if a == '2':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("X|O|O\n------\nX|O|X\n------\nO|X| ")
            elif a == '8':
                print("X|O|O\n------\nX|O| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X|O| \n------\nX|O| \n------\nO| |X")
            a = input('move: ')
            if a == '7':
                print("X|O|O\n------\nX|O| \n------\nO|X|X")
            elif a == '5':
                print("X|O| \n------\nX|O|X\n------\nO|O|X")
            elif a == '2':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("X|O|X\n------\nX|O| \n------\nO| | ")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\nX|O|X\n------\nO|O| ")
            elif a == '7':
                print("X|O|X\n------\nX|O|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("X|O|X\n------\nX|O|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|O|X\n------\nX|O| \n------\nO|O|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '6':
        print("X| | \n------\nO|O| \n------\nX| | ")
        a = input('move: ')
        if a == '7':
            print("X| | \n------\nO|O| \n------\nX|X| ")
            a = input('move: ')
            if a == '1':
                print("X|O| \n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("X|O|X\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("X|O|X\n------\nO|O|O\n------\nX|X| ")
                    elif a == '8':
                        print("X|O|X\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("X|O| \n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '2':
                        print("X|O|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("X|O| \n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("X|O|X\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("X| |O\n------\nO|O| \n------\nX|X| ")
                a = input('move: ')
                if a == '5':
                    print("X| |O\n------\nO|O|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("X| |O\n------\nO|O|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("X|O|O\n------\nO|O|X\n------\nX|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("X|X|O\n------\nO|O| \n------\nX|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("X|X|O\n------\nO|O|O\n------\nX|X| ")
                    elif a == '8':
                        print("X|X|O\n------\nO|O| \n------\nX|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("X|O|X\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '5':
                print("X|O|X\n------\nO|O|X\n------\nX|O| ")
            elif a == '7':
                print("X|O|X\n------\nO|O|O\n------\nX|X| ")
            elif a == '8':
                print("X|O|X\n------\nO|O| \n------\nX|O|X")
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("X|X|O\n------\nO|O| \n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("X|X|O\n------\nO|O|O\n------\nX|X| ")
            elif a == '5':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X|X|O\n------\nO|O| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("X| |O\n------\nO|O|X\n------\nX| | ")
            a = input('move: ')
            if a == '1':
                print("X|X|O\n------\nO|O|X\n------\nX| |O")
                a = input('move: ')
                if a == '7':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("X| |O\n------\nO|O|X\n------\nX|X|O")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|X|O")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("X| |O\n------\nO|O|X\n------\nX|O|X")
                a = input('move: ')
                if a == '1':
                    print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("X| | \n------\nO|O| \n------\nX| |X")
            a = input('move: ')
            if a == '2':
                print("X| |O\n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '5':
                    print("X| |O\n------\nO|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '1':
                        print("X|O|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("X| |O\n------\nO|O|X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("X|X|O\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|X|O\n------\nO|O| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("X|X|O\n------\nO|O|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("X|O| \n------\nO|O| \n------\nX| |X")
                a = input('move: ')
                if a == '7':
                    print("X|O| \n------\nO|O| \n------\nX|X|X")
                elif a == '5':
                    print("X|O| \n------\nO|O|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O| \n------\nO|O|X\n------\nX|O|X")
                    elif a == '2':
                        print("X|O|O\n------\nO|O|X\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("X|O|O\n------\nO|O|X\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '2':
                    print("X|O|X\n------\nO|O| \n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("X|O|X\n------\nO|O| \n------\nX|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
elif a == '4':
    print("O| | \n------\n |X| \n------\n | | ")
    a = input('move: ')
    if a == '6':
        print("O| |O\n------\n |X| \n------\nX| | ")
        a = input('move: ')
        if a == '7':
            print("O| |O\n------\n |X| \n------\nX|X| ")
            a = input('move: ')
            if a == '5':
                print("O| |O\n------\n |X|O\n------\nX|X| ")
                a = input('move: ')
                if a == '3':
                    print("O| |O\n------\nX|X|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX|X|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O| |O\n------\nO|X| \n------\nX|X| ")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\nO|X| \n------\nX|X| ")
                elif a == '5':
                    print("O| |O\n------\nO|X|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nO|X|X\n------\nX|X| ")
                    elif a == '8':
                        print("O| |O\n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O| |O\n------\n |X| \n------\nX|X|O")
                a = input('move: ')
                if a == '3':
                    print("O| |O\n------\nX|X| \n------\nX|X|O")
                    a = input('move: ')
                    if a == '1':
                        print("O|O|O\n------\nX|X| \n------\nX|X|O")
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O| |O\n------\n |X|X\n------\nX|X|O")
                    a = input('move: ')
                    if a == '3':
                        print("O| |O\n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|O|O\n------\nX|X| \n------\nX| | ")
        elif a == '8':
            print("O| |O\n------\n |X| \n------\nX| |X")
            a = input('move: ')
            if a == '3':
                print("O| |O\n------\nO|X| \n------\nX| |X")
                a = input('move: ')
                if a == '5':
                    print("O| |O\n------\nO|X|X\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O| |O\n------\nO|X|X\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|O\n------\nO|X|X\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                elif a == '1':
                    print("O|X|O\n------\nO|X| \n------\nX| |X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|O\n------\nO|X|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nO|X|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '7':
                        print("O|X|O\n------\nO|X| \n------\nX|O|X")
                        a = input('move: ')
                        if a == '5':
                            print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O| |O\n------\n |X|O\n------\nX| |X")
                a = input('move: ')
                if a == '1':
                    print("O|X|O\n------\n |X|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O|X|O\n------\n |X|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|O\n------\nO|X|O\n------\nX| |X")
                        a = input('move: ')
                        if a == '7':
                            print("O|X|O\n------\nO|X|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O| |O\n------\nX|X|O\n------\nX| |X")
                    a = input('move: ')
                    if a == '7':
                        print("O| |O\n------\nX|X|O\n------\nX|O|X")
                        a = input('move: ')
                        if a == '1':
                            print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '1':
                        print("O|O|O\n------\nX|X|O\n------\nX| |X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X|O\n------\n |X| \n------\nX|O| ")
            a = input('move: ')
            if a == '8':
                print("O|X|O\n------\n |X|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O| |O\n------\nO|X|X\n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O|O|O\n------\nO|X|X\n------\nX|X| ")
            elif a == '1':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O|O\n------\nO|X|X\n------\nX| |X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '5':
        print("O| | \n------\nO|X|X\n------\n | | ")
        a = input('move: ')
        if a == '1':
            print("O|X| \n------\nO|X|X\n------\nO| | ")
        elif a == '7':
            print("O| | \n------\nO|X|X\n------\nO|X| ")
        elif a == '6':
            print("O| |O\n------\nO|X|X\n------\nX| | ")
            a = input('move: ')
            if a == '1':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O|O\n------\nO|X|X\n------\nX|X| ")
            elif a == '8':
                print("O|O|O\n------\nO|X|X\n------\nX| |X")
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O| |X\n------\nO|X|X\n------\nO| | ")
        elif a == '8':
            print("O| | \n------\nO|X|X\n------\nO| |X")
        else:
            print('INVALID MOVE')
    elif a == '7':
        print("O|O| \n------\n |X| \n------\n |X| ")
        a = input('move: ')
        if a == '5':
            print("O|O| \n------\nO|X|X\n------\n |X| ")
            a = input('move: ')
            if a == '8':
                print("O|O| \n------\nO|X|X\n------\nO|X|X")
            elif a == '2':
                print("O|O|X\n------\nO|X|X\n------\nO|X| ")
            elif a == '6':
                print("O|O|O\n------\nO|X|X\n------\nX|X| ")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|O| \n------\n |X| \n------\n |X|X")
            a = input('move: ')
            if a == '3':
                print("O|O| \n------\nO|X| \n------\n |X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nO|X| \n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|O|X\n------\nO|X| \n------\nO|X|X")
                    elif a == '5':
                        print("O|O|X\n------\nO|X|O\n------\n |X|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|O|X\n------\nO|X|O\n------\nX|X|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '5':
                    print("O|O| \n------\nO|X|X\n------\n |X|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|O| \n------\nO|X|X\n------\nO|X|X")
                    else:
                        print('INVALID MOVE')
                elif a == '6':
                    print("O|O| \n------\nO|X| \n------\nX|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|O| \n------\nX|X| \n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|O| \n------\nX|X| \n------\nO|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X| \n------\nO|X| ")
                    a = input('move: ')
                    if a == '5':
                        print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|O|X\n------\nX|X| \n------\nO|X|O")
                        a = input('move: ')
                        if a == '5':
                            print("O|O|X\n------\nX|X|X\n------\nO|X|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|O| \n------\n |X| \n------\nX|X| ")
            a = input('move: ')
            if a == '3':
                print("O|O| \n------\nO|X| \n------\nX|X| ")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nO|X| \n------\nX|X| ")
                elif a == '5':
                    print("O|O| \n------\nO|X|X\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O| \n------\nO|X|X\n------\nX|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nO|X|X\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|O|O\n------\nO|X|X\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O|O|X\n------\n |X| \n------\nO|X| ")
            a = input('move: ')
            if a == '3':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|O|X\n------\nO|X|X\n------\nO|X| ")
            elif a == '8':
                print("O|O|X\n------\nO|X| \n------\nO|X|X")
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '8':
        print("O| | \n------\n |X| \n------\nO| |X")
        a = input('move: ')
        if a == '1':
            print("O|X| \n------\nO|X| \n------\nO| |X")
        elif a == '7':
            print("O| | \n------\nO|X| \n------\nO|X|X")
        elif a == '5':
            print("O| | \n------\nO|X|X\n------\nO| |X")
        elif a == '3':
            print("O| | \n------\nX|X|O\n------\nO| |X")
            a = input('move: ')
            if a == '1':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O| |X\n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '1':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O| |X\n------\nO|X| \n------\nO| |X")
        else:
            print('INVALID MOVE')
    elif a == '3':
        print("O| | \n------\nX|X|O\n------\n | | ")
        a = input('move: ')
        if a == '6':
            print("O| | \n------\nX|X|O\n------\nX| | ")
            a = input('move: ')
            if a == '7':
                print("O| | \n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '1':
                    print("O|X| \n------\nX|X|O\n------\nX|O| ")
                    a = input('move: ')
                    if a == '2':
                        print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '8':
                        print("O|X| \n------\nX|X|O\n------\nX|O|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|O| \n------\nX|X|O\n------\nX| | ")
                a = input('move: ')
                if a == '7':
                    print("O|O| \n------\nX|X|O\n------\nX|X| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|O| \n------\nX|X|O\n------\nX|X|O")
                        a = input('move: ')
                        if a == '2':
                            print("O|O|X\n------\nX|X|O\n------\nX|X|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '2':
                        print("O|O|O\n------\nX|X|O\n------\nX|X| ")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '1':
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '2':
            print("O| |X\n------\nX|X|O\n------\nO| | ")
            a = input('move: ')
            if a == '8':
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '1':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O|O| \n------\nX|X|O\n------\n |X| ")
            a = input('move: ')
            if a == '6':
                print("O|O|O\n------\nX|X|O\n------\nX|X| ")
            elif a == '8':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O| | \n------\nX|X|O\n------\nO| |X")
            a = input('move: ')
            if a == '1':
                print("O|X| \n------\nX|X|O\n------\nO|O|X")
                a = input('move: ')
                if a == '2':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O| \n------\nX|X|O\n------\nO|X|X")
                a = input('move: ')
                if a == '2':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    elif a == '2':
        print("O| |X\n------\n |X| \n------\nO| | ")
        a = input('move: ')
        if a == '5':
            print("O| |X\n------\nO|X|X\n------\nO| | ")
        elif a == '1':
            print("O|X|X\n------\nO|X| \n------\nO| | ")
        elif a == '8':
            print("O| |X\n------\nO|X| \n------\nO| |X")
        elif a == '3':
            print("O| |X\n------\nX|X|O\n------\nO| | ")
            a = input('move: ')
            if a == '1':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '7':
                print("O|O|X\n------\nX|X|O\n------\nO|X| ")
                a = input('move: ')
                if a == '8':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|O|X\n------\nX|X|O\n------\nO| |X")
                a = input('move: ')
                if a == '7':
                    print("O|O|X\n------\nX|X|O\n------\nO|X|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '7':
            print("O| |X\n------\nO|X| \n------\nO|X| ")
        else:
            print('INVALID MOVE')
    elif a == '1':
        print("O|X| \n------\n |X| \n------\n |O| ")
        a = input('move: ')
        if a == '2':
            print("O|X|X\n------\n |X| \n------\n |O| ")
            a = input('move: ')
            if a == '8':
                print("O|X|X\n------\n |X| \n------\n |O|O")
                a = input('move: ')
                if a == '5':
                    print("O|X|X\n------\n |X|X\n------\n |O|O")
                    a = input('move: ')
                    if a == '3':
                        print("O|X|X\n------\nO|X|X\n------\n |O|O")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nO|X|X\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '3':
                    print("O|X|X\n------\nX|X| \n------\n |O|O")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nX|X|O\n------\n |O|O")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O|X|X\n------\nX|X| \n------\nO|O|O")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|X\n------\nO|X| \n------\n |O| ")
                a = input('move: ')
                if a == '6':
                    print("O|X|X\n------\nO|X| \n------\nX|O| ")
                elif a == '5':
                    print("O|X|X\n------\nO|X|X\n------\n |O| ")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\nO|X|X\n------\nO|O| ")
                    elif a == '8':
                        print("O|X|X\n------\nO|X|X\n------\n |O|O")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nO|X|X\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|X\n------\nO|X| \n------\n |O|X")
                    a = input('move: ')
                    if a == '5':
                        print("O|X|X\n------\nO|X|O\n------\n |O|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nO|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O|X|X\n------\nO|X| \n------\nO|O|X")
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|X\n------\n |X|O\n------\n |O| ")
                a = input('move: ')
                if a == '3':
                    print("O|X|X\n------\nX|X|O\n------\n |O| ")
                    a = input('move: ')
                    if a == '8':
                        print("O|X|X\n------\nX|X|O\n------\n |O|O")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nX|X|O\n------\nX|O|O")
                        else:
                            print('INVALID MOVE')
                    elif a == '6':
                        print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                        a = input('move: ')
                        if a == '8':
                            print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                elif a == '8':
                    print("O|X|X\n------\n |X|O\n------\n |O|X")
                    a = input('move: ')
                    if a == '6':
                        print("O|X|X\n------\n |X|O\n------\nO|O|X")
                        a = input('move: ')
                        if a == '3':
                            print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                        else:
                            print('INVALID MOVE')
                    elif a == '3':
                        print("O|X|X\n------\nO|X|O\n------\n |O|X")
                        a = input('move: ')
                        if a == '6':
                            print("O|X|X\n------\nO|X|O\n------\nX|O|X")
                        else:
                            print('INVALID MOVE')
                    else:
                        print('INVALID MOVE')
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '5':
            print("O|X| \n------\nO|X|X\n------\n |O| ")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '2':
                print("O|X|X\n------\nO|X|X\n------\nO|O| ")
            elif a == '8':
                print("O|X| \n------\nO|X|X\n------\nO|O|X")
            else:
                print('INVALID MOVE')
        elif a == '8':
            print("O|X|O\n------\n |X| \n------\n |O|X")
            a = input('move: ')
            if a == '6':
                print("O|X|O\n------\nO|X| \n------\nX|O|X")
                a = input('move: ')
                if a == '5':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nO|X|X\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '6':
            print("O|X|O\n------\n |X| \n------\nX|O| ")
            a = input('move: ')
            if a == '8':
                print("O|X|O\n------\n |X|O\n------\nX|O|X")
                a = input('move: ')
                if a == '3':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '3':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '5':
                print("O|X|O\n------\nO|X|X\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nO|X|X\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        elif a == '3':
            print("O|X| \n------\nX|X|O\n------\n |O| ")
            a = input('move: ')
            if a == '2':
                print("O|X|X\n------\nX|X|O\n------\nO|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|X\n------\nX|X|O\n------\nO|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '6':
                print("O|X|O\n------\nX|X|O\n------\nX|O| ")
                a = input('move: ')
                if a == '8':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            elif a == '8':
                print("O|X|O\n------\nX|X|O\n------\n |O|X")
                a = input('move: ')
                if a == '6':
                    print("O|X|O\n------\nX|X|O\n------\nX|O|X")
                else:
                    print('INVALID MOVE')
            else:
                print('INVALID MOVE')
        else:
            print('INVALID MOVE')
    else:
        print('INVALID MOVE')
else:
    print('INVALID MOVE')
