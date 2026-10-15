Hangman Challenge

A multi-round terminal word-guessing game with categories, dynamic difficulty, hints, and session tracking.

How to Run

No external dependencies are required (Python 3.9+ recommended).

python main.py


How to Play

Setup: Choose a category and a difficulty (Easy, Medium, Hard). Difficulty affects starting lives and score multipliers.

Commands: Enter a single letter to guess, /hint for a clue (costs points), or /quit to end the round.

Goal: Guess the word before losing all lives. String together wins to build your streak and earn bonus points!

Session: Play multiple rounds to track your total wins, rounds played, and best streak.

Completed Features & Fixes

Task 1 (Bug Fix): Prevented duplicate incorrect guesses from penalizing the player's life count multiple times.

Task 2 (Session Stats): Integrated the SessionStats tracker so rounds played, rounds won, and best streaks persist across multiple rounds.

Task 3 (Difficulty): Added Easy (8 lives, 1x score), Medium (6 lives, 2x score), and Hard (4 lives, 3x score) difficulty settings.

Task 4 (Robust UI): Improved input validation and feedback layout. Error messages (like invalid letters or repeated guesses) now display neatly above the prompt instead of reprinting the entire game board.