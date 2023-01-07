# import the necessary modules
import random

# define the main function
def main():
  while True:
    # list of tuples containing the questions and answers
    questions = [
      ("Who was the drummer of The Beatles?", "Ringo Starr"),
      ("What was the title of The Beatles' first album?", "Please Please Me"),
      ("Who wrote the song 'Yesterday'?", "Paul McCartney"),
      ("What was the title of the last album released by The Beatles?", "Abbey Road"),
      ("Which member of The Beatles left the band first?", "Pete Best"),
    ]

    # list of tuples containing the questions and answers for the second round
    questions_2 = [
      ("What was the title of The Beatles' second album?", "With The Beatles"),
      ("Which member of The Beatles wrote the song 'Hey Jude'?", "Paul McCartney"),
      ("What was the title of the first album released by The Beatles after they disbanded?", "Let It Be"),
      ("What was the title of The Beatles' first single?", "Love Me Do"),
      ("What was the name of the band that Pete Best was a member of before joining The Beatles?", "The Blackjacks"),
    ]

    # shuffle the questions
    random.shuffle(questions)

    # counter for the number of correct answers
    correct = 0

    # iterate through the questions
    for question, answer in questions:
      # ask the question
      user_answer = input(f"{question}: ")

      # check if the answer is correct
      if user_answer.lower() == answer.lower():
        print("Correct!")
        correct += 1
      else:
        print("Incorrect.")

    # calculate the score
    score = 100 * correct / len(questions)

    # print the score
    print(f"Your score is {score:.2f}.")

    # ask the user if they want to play again
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.lower() != "y":
      break

    # set the questions to the second round of questions
    questions = questions_2

# run the main function
if __name__ == "__main__":
  main()
