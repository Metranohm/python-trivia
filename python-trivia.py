# Define a list of questions and answers
questions = [
    ("Who created Python?", "Guido van Rossum"),
    ("In what year was Python first released?", "1991"),
    ("What is the philosophy behind Python?", "There should be one-- and preferably only one --obvious way to do it"),
    ("What is the name of Python's official style guide?", "PEP 8"),
    ("What is the name of the Python library for scientific computing?", "NumPy"),
]

# Initialize the score
score = 0

# Loop through the questions
for question, answer in questions:
  # Ask the question and get the user's response
  response = input(f"{question}\n> ")

  # Check if the response is correct
  if response.lower() == answer.lower():
    print("Correct!\n")
    score += 1
  else:
    print(f"Incorrect. The correct answer is: {answer}\n")

# Print the final score
print(f"You got {score} out of {len(questions)} correct.")
