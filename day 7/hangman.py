import random
import hangman_art
import hangman_words
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)
guessed_word = []
for n in range(len(chosen_word)):
    guessed_word.append("_")
print(guessed_word)
no_of_lives = 6
end_game = False
def letter_pick():
    guess = input("enter a letter.").lower()
    if guess in guessed_word:
        print("You have guessed this letter already. ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            guessed_word[position] = guess
            if "_" not in guessed_word:
                global end_game
                end_game = True
                print("Game Over.You Win")
    if guess  not in chosen_word:
        print(f"{guess} is not in the word")
        global no_of_lives
        print(hangman_art.stages[no_of_lives])
        if no_of_lives > 1:
            print(f"you have {no_of_lives} lives left")
        elif no_of_lives == 1:
            print(f"you have {no_of_lives} life left")
        elif no_of_lives == 0:
            end_game = True
            print(f"Game Over.You Lose\nThe word is {chosen_word}")
        no_of_lives -= 1
    print(guessed_word)



while end_game == False :
    letter_pick()

