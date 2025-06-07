import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue
    else:
        player_number = int(player_input)

        if player_number == computer_number:
            print("You guess it!")
            computer_number = random.randint(1, 200)
            while True:
                player_input = input("Guess the number (1-200): ")

                if not player_input.isdigit():
                    print("Invalid input. Try again...")
                    continue
                else:
                    player_number = int(player_input)

                    if player_number == computer_number:
                        print("You guess it!")
                        computer_number = random.randint(1, 500)

                        while True:
                            player_input = input("Guess the number (1-500): ")

                            if not player_input.isdigit():
                                print("Invalid input. Try again...")
                                continue
                            else:
                                player_number = int(player_input)

                                if player_number == computer_number:
                                    print("You guess it!")
                                    computer_number = random.randint(1, 1000)

                                    while True:
                                        player_input = input("Guess the number (1-1000): ")

                                        if not player_input.isdigit():
                                            print("Invalid input. Try again...")
                                            continue
                                        else:
                                            player_number = int(player_input)

                                            if player_number == computer_number:
                                                print("You guess it!")
                                                computer_number = random.randint(1, 2000)

                                                while True:
                                                    player_input = input("Guess the number (1-2000): ")

                                                    if not player_input.isdigit():
                                                        print("Invalid input. Try again...")
                                                        continue
                                                    else:
                                                        player_number = int(player_input)

                                                        if player_number == computer_number:
                                                            print("You guess it!")
                                                            computer_number = random.randint(1, 5000)

                                                            while True:
                                                                player_input = input("Guess the number (1-5000): ")

                                                                if not player_input.isdigit():
                                                                    print("Invalid input. Try again...")
                                                                    continue
                                                                else:
                                                                    player_number = int(player_input)

                                                                    if player_number == computer_number:
                                                                        print("You guess it!")
                                                                        computer_number = random.randint(1, 10000)

                                                                        while True:
                                                                            player_input = input(
                                                                                "Guess the number (1-10000): ")

                                                                            if not player_input.isdigit():
                                                                                print("Invalid input. Try again...")
                                                                                continue
                                                                            else:
                                                                                player_number = int(player_input)

                                                                                if player_number == computer_number:
                                                                                    print("You guess it!")
                                                                                    break
                                                                                elif player_number > computer_number:
                                                                                    print("Too High!")
                                                                                else:
                                                                                    print("Too Low!")
                                                                        break
                                                                    elif player_number > computer_number:
                                                                        print("Too High!")
                                                                    else:
                                                                        print("Too Low!")
                                                            break
                                                        elif player_number > computer_number:
                                                            print("Too High!")
                                                        else:
                                                            print("Too Low!")
                                                break
                                            elif player_number > computer_number:
                                                print("Too High!")
                                            else:
                                                print("Too Low!")
                                    break
                                elif player_number > computer_number:
                                    print("Too High!")
                                else:
                                    print("Too Low!")
                        break
                    elif player_number > computer_number:
                        print("Too High!")
                    else:
                        print("Too Low!")
            break
        elif player_number > computer_number:
            print("Too High!")
        else:
            print("Too Low!")