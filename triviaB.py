# import the necessary modules
import random

# define the main function
def main():
  # list of tuples containing the questions and answers
  questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest country in the world?", "Russia"),
    ("What is the currency of Japan?", "Yen"),
    ("What is the highest mountain in the world?", "Mount Everest"),
    ("What is the name of the oldest living animal?", "Linnea"),
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

  # print the number of correct answers
  print(f"You got {correct} out of {len(questions)} correct.")

# run the main function
if __name__ == "__main__":
  main()
