# guess_a_number_by_slavy
This is a simple console game "Guess A Number" written in Python.

Description

Ultimate Number Guesser is a progressive number guessing game where the player must guess a random number selected by the computer. Each time the player guesses correctly, the number range increases, making the game progressively more challenging.

The game tests your intuition, patience, and ability to narrow down the correct number using logical hints.

How to Play

The game starts by asking you to guess a number between 1 and 100.

If your guess is:

Too high – the game will prompt: "Too High!"

Too low – the game will prompt: "Too Low!"

Correct – the game will congratulate you: "You guess it!" and move you to the next level with a higher number range.

The game continues with increasing difficulty:

Level 1: 1–100

Level 2: 1–200

Level 3: 1–500

Level 4: 1–1000

Level 5: 1–2000

Level 6: 1–5000

Level 7: 1–10000

You win the game by guessing the final number in the 1–10000 range.

Features

Progressive difficulty – The range increases after each correct guess.

Real-time feedback – "Too High", "Too Low", or "You guess it!"

Input validation – Only numeric guesses are accepted.

Looped gameplay – Each level continues until the correct number is guessed.

Requirements

Python 3.x

Run the Game

Clone the repository or copy the script into a .py file, then run:

python number_guesser.py

Note

This game is console-based and requires user input via the terminal.