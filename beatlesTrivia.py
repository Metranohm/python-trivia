def play_trivia_game():
  score = 0
  print("Welcome to the Beatles Python Trivia Game!\n")
  print("You will be asked 15 questions about the Beatles. Get as many correct as you can.\n")

  # Question 1
  q1 = "In what year did the Beatles form?\n"
  a1 = "1960"
  answer = input(q1)
  if answer == a1:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a1 + "\n")
  
  # Question 2
  q2 = "Who was the lead singer of the Beatles?\n"
  a2 = "John Lennon"
  answer = input(q2)
  if answer == a2:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a2 + "\n")

  # Question 3
  q3 = "What was the name of the Beatles' first album?\n"
  a3 = "Please Please Me"
  answer = input(q3)
  if answer == a3:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a3 + "\n")
  
  # Question 4
  q4 = "What was the name of the Beatles' last album?\n"
  a4 = "Let It Be"
  answer = input(q4)
  if answer == a4:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a4 + "\n")
  
  # Question 5
  q5 = "What was the name of the Beatles' first single?\n"
  a5 = "Love Me Do"
  answer = input(q5)
  if answer == a5:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a5 + "\n")
  
  # Question 6
  q6 = "What was the name of the Beatles' fourth single?\n"
  a6 = "I Want To Hold Your Hand"
  answer = input(q6)
  if answer == a6:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a6 + "\n")
  
  # Question 7
  q7 = "Who was the annoying lady who broke up the Beatles?\n"
  a7 = "Yoko Ono"
  answer = input(q7)
  if answer == a7:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a7 + "\n")
    
  # Question 8
  q8 = "What was the name of the Beatles' first movie?\n"
  a8 = "A Hard Day's Night"
  answer = input(q8)
  if answer == a8:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a8 + "\n")
  
  # Question 9
  q9 = "Who was the creepiest beatle?\n"
  a9 = "George Harrison"
  answer = input(q9)
  if answer == a9:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a9 + "\n")
  
  
  # Question 10
  q10 = "Which beatle had the hottest wife?\n"
  a10 = "Paul McCartney" 
  answer = input(q10)
  if answer == a10:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a10 + "\n")
  
  # Question 11
  q11 = "Which beatle was absuive to his wife?\n"
  a11 = "John Lennon"
  answer = input(q11)
  if answer == a11:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a11 + "\n")
  
  # Question 12
  q12 = "Which beatle had the worst hygiene?\n"
  a12 = "Ringo Starr"
  answer = input(q12)
  if answer == a12:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a12 + "\n")
    
  # Question 13
  q13 = "Which beatle's child had the most legal problems?\n"
  a13 = "Dhani Harrison"
  answer = input(q13)
  if answer == a13:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a13 + "\n")
    
  # Question 14
  q14 = "Which beatles was the biggest jerk?\n"
  a14 = "Paul McCartney"
  answer = input(q14)
  if answer == a14:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a14 + "\n")
    
  # Question 15
  q15 = "Which beatle should've died first?\n"
  a15 = "John Lennon"
  answer = input(q15)
  if answer == a15:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a15 + "\n")
  
  # Question 16
  q16 = "Which beatle was the most talented?\n"
  a16 = "George Harrison"
  answer = input(q16)
  if answer == a16:
    score += 1
    print("Correct!\n")
  else:
    print("Incorrect. The correct answer is " + a16 + "\n")

  # Final score
  print("You got " + str(score) + " out of 20 questions correct.")

# Start the game
play_trivia_game()