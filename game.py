import random
from words import WORDS, HINTS
from stats import SessionStats

class HangmanGame:
    def __init__(self):
        self.score = 0
        self.streak = 0
        self.stats = SessionStats()
        self.category = "technology"
        self.secret = ""
        self.guessed_letters = set()
        self.wrong_letters = set()
        self.lives = 6
        self.hint_used = False
        
        self.current_difficulty = "medium"
        self.difficulty_lives = {"easy": 8, "medium": 6, "hard": 4}
        self.difficulty_mult = {"easy": 1, "medium": 2, "hard": 3}

    def start_round(self):
        self.secret = random.choice(WORDS[self.category])
        self.guessed_letters.clear()
        self.wrong_letters.clear()
        self.lives = self.difficulty_lives[self.current_difficulty]
        self.hint_used = False

    def masked(self):
        return " ".join(ch if ch in self.guessed_letters else "_" for ch in self.secret)

    def won(self):
        return all(ch in self.guessed_letters for ch in set(self.secret))

    def guess(self, letter):
        # Task 4: Robust input handling and clear feedback
        if len(letter) != 1 or not letter.isalpha():
            return "Invalid input. Please enter exactly one letter."
        
        if letter in self.guessed_letters:
            return f"You already guessed '{letter}'."
        
        self.guessed_letters.add(letter)
        
        if letter in self.secret:
            return "Correct guess!"
        
        self.wrong_letters.add(letter)
        self.lives -= 1
        return "Wrong guess."

    def use_hint(self):
        if self.hint_used:
            return "Hint already used this round."
        self.hint_used = True
        penalty = 1 * self.difficulty_mult[self.current_difficulty]
        self.score = max(0, self.score - penalty)
        return f"Hint: {HINTS.get(self.secret, 'No hint available.')}"

    def play_round(self):
        self.start_round()
        feedback = ""
        
        while self.lives > 0 and not self.won():
            print("\nWord:", self.masked())
            print("Wrong:", " ".join(sorted(self.wrong_letters)) or "-")
            print("Lives:", self.lives, "Score:", self.score, "Streak:", self.streak)
            
            # Task 4: Print feedback contextually before the next input
            if feedback:
                print(">>", feedback)
                feedback = ""
                
            raw = input("Letter, /hint, or /quit: ").strip().lower()
            
            if raw == "/quit":
                return False
            if raw == "/hint":
                if self.hint_used:
                    feedback = "Hint already used this round."
                else:
                    feedback = self.use_hint()
                continue
                
            feedback = self.guess(raw)

        if self.won():
            self.streak += 1
            round_score = (5 + self.streak) * self.difficulty_mult[self.current_difficulty]
            self.score += round_score
            print("\nSolved:", self.secret)
            print(f"Earned {round_score} points! Total Score: {self.score}")
            self.stats.record(True, self.streak)
            return True

        self.streak = 0
        print("\nOut of lives. The word was:", self.secret)
        self.stats.record(False, self.streak)
        return True

    def run(self):
        print("Hangman Challenge")
        print("A session consists of multiple rounds.")
        while True:
            print("\nCategories:", ", ".join(WORDS))
            
            # Task 4: Robust category selection loop
            while True:
                raw = input("Choose category or q: ").strip().lower()
                if raw == "q" or raw in WORDS:
                    break
                print("Unknown category. Please try again.")
                
            if raw == "q":
                break
                
            self.category = raw
            
            # Task 4: Robust difficulty selection loop
            while True:
                diff = input("Choose difficulty (easy/medium/hard): ").strip().lower()
                if diff in self.difficulty_lives:
                    self.current_difficulty = diff
                    break
                print("Invalid difficulty. Please enter easy, medium, or hard.")
                
            if not self.play_round():
                break
                
            again = input("Another round? [y/n]: ").strip().lower()
            if again != "y":
                break
                
        print("\n=== Session Statistics ===")
        print("Final score:", self.score, " Streak:", self.streak)
        print("Rounds Played:", self.stats.rounds)
        print("Rounds Won:", self.stats.wins)
        print("Best Streak:", self.stats.best_streak)