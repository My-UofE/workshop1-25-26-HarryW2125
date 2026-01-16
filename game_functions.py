import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    middleVal = len(poss_values)//2   
    x = poss_values[middleVal]
    return x

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    temp=[]
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            temp.append(i)
    
    if len(temp) > 0:
        print("Well done!", letter,"is in the word")
        return True
    else:
        print("sorry,", letter,"is not in the word")
        return False
    




def check_higher_lower(current_val, next_val, user_input):
    if current_val > next_val:
        if user_input == 'l':
            return True
        
        return False
    
    if next_val > current_val:
        if user_input == 'h':
            return True
        
        return False
