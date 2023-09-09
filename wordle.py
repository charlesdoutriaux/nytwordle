import argparse
import random
from colored import Fore, Back, Style


p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

p.add_argument("--info", "-i", action="store_true")
p.add_argument("--cheat", "-c", action="store_true")

args = p.parse_args()

# if __name__ == "__main__":

# Read all words
with open("all_words.txt") as f:
    all = f.read().strip().split(",")

# Read wordle words
with open("wordle.txt") as f:
    wordle = f.read().strip().split(",")

# pick a word
solution = wordle[random.randint(0, len(wordle)-1)]
solution = "MEATY"
if args.cheat:
    print("Solution:", solution)

def color_word(word, solution, used):
    out = ""
    temp_solution = solution
    for i, letter in enumerate(word):
        color = f"{Style.BOLD}{Fore.WHITE}"
        if letter not in temp_solution:
            color += f"{Back.BLACK}"
            used[letter] = f"{Back.light_gray}"
        elif letter in temp_solution:
            if letter == solution[i]:
                color += f"{Back.GREEN}"
                used[letter] = color
            else:
                match = False
                for j in range(5):
                    if solution[j] == word[j] and solution[j]==letter:
                        match = True
                if not match:
                    color += f"{Back.RGB(245, 245, 220)}"
                temp_solution = temp_solution.replace(letter,"")
            if used[letter] == "":
                used[letter] = color
        out += f"{color}{letter}{Style.reset}"
    return out
    
def display(solution, used, guesses):
    for i, guess in enumerate(guesses):
        print(i+1, color_word(guess, solution, used))
    print()
    for row in layout:
        for letter in row:
            print(f"{used[letter]}{letter}{Style.reset}",end="")
        print(f"{Style.reset}")

# Setup used_words
used = {}
for i in range(65,91):
    used[chr(i)] = f"{Back.BLACK}{Fore.WHITE}"
    used[chr(i)] = ""
cont = True
round = 0
guesses = [[], ] * 6
layout = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
while cont:
    ask = True
    while ask:
        display(solution, used, guesses)
        word = input("enter a word: ").upper()
        if word in all:
            ask = False
    guesses[round] = word
    round +=1
    if round==6 or word==solution:
        display(solution, used, guesses)
        cont = False
