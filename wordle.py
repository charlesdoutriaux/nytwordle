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

cont = True

round = 0

def color_word(word, solution):
    out = ""
    temp_solution = solution
    for i, letter in enumerate(word):
        color = f"{Style.BOLD}{Fore.WHITE}"
        if letter not in temp_solution:
            color += f"{Back.BLACK}"
        elif letter in temp_solution:
            if letter == solution[i]:
                color += f"{Back.GREEN}"
            else:
                match = False
                for j in range(5):
                    if solution[j] == word[j] and solution[j]==letter:
                        match = True
                if not match:
                    color += f"{Back.RGB(245, 245, 220)}"
                temp_solution = temp_solution.replace(letter,"")
        out += f"{color}{letter}{Style.reset}"
    return out
    

while cont:
    ask = True
    while ask:
        word = input("enter a word: ").upper()
        if word in all:
            ask = False
        print(color_word(word, solution))
    cont = False
