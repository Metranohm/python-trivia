# import the necessary modules
import random

# define the main function
def main():
  while True:
    # list of tuples containing the questions and answers
    questions = [
      ("What is the capital of France?", "Paris"),
      ("What is the largest country in the world?", "Russia"),
      ("What is the currency of Japan?", "Yen"),
      ("What is the highest mountain in the world?", "Mount Everest"),
      ("What is the name of the oldest living animal?", "Linnea"),
    ]

    # list of tuples containing the questions and answers for the second round
    questions_2 = [
      ("What is the capital of Italy?", "Rome"),
      ("What is the longest river in the world?", "Nile"),
      ("What is the currency of the United States?", "Dollar"),
      ("What is the highest peak in the United States?", "Mount Denali"),
      ("What is the name of the fastest land animal?", "Cheetah"),
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
