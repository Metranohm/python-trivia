# import the necessary modules
import random

# define the main function
def main():
  # list of tuples containing the questions and answers
  questions = [
      ( "What is the name of the band's leader and main songwriter?", "Anton Newcombe" ),
      ( "What year was the band formed?", "1990" ),
      ( "What genre of music does the band primarily play?", "Psychedelic rock" ),
      ( "What is the title of the band's debut album?", "Methodrone" ),
      ( "Which album features the song 'Straight Up and Down'?", "Revelation" ),
      ( "Which album features the song 'Anemone'?", "Tepid Peppermint Wonderland: A Retrospective" ),
      ( "What was the title of the band's first EP?", "Spacegirl and Other Favorites" ),
      ( "What was the original lineup of the band?", "Anton Newcombe, Dean Taylor, Matt Hollywood, and Collin Hegna" ),
      ( "What is the title of the band's eighth studio album?", "Who Killed Sgt. Pepper?" ),
      ( "Which album features the song 'Not If You Were the Last Dandy on Earth'?", "Their Satanic Majesties' Second Request" ),
      ( "Which album features the song 'The Devil May Care (Mom & Dad Don't)'?", "Thank God for Mental Illness" ),
      ( "Which album features the song 'Vacuum Boots'?", "Bravery, Repetition and Noise" ),
      ( "Which album features the song 'Wish I Could Fly'?", "Give It Back!" ),
      ( "Which album features the song 'The Clouds Are Lies'?", "Aufheben" ),
      ( "Which album features the song 'The One'?", "Musique de film imaginé" ),
      ( "What is the name of the band's leader and main songwriter?", "Anton Newcombe" ),
      ( "What year was the band formed?", "1990" ),
      ( "What genre of music does the band primarily play?", "Psychedelic rock" ),
      ( "What is the title of the band's debut album?", "Methodrone" ),
      ( "Which album features the song 'Straight Up and Down'?", "Revelation" ),
      ( "Which album features the song 'Anemone'?", "Tepid Peppermint Wonderland: A Retrospective" ),
      ( "What was the title of the band's first EP?", "Spacegirl and Other Favorites" ),
      ( "What was the original lineup of the band?", "Anton Newcombe, Dean Taylor, Matt Hollywood, and Collin Hegna" ),
      ( "What is the title of the band's eighth studio album?", "Who Killed Sgt. Pepper?" ),
      ( "Which album features the song 'Not If You Were the Last Dandy on Earth'?", "Their Satanic Majesties' Second Request" ),
      ( "Which album features the song 'The Devil May Care (Mom & Dad Don't)'?", "Thank God for Mental Illness" ),
      ( "Which album features the song 'Vacuum Boots'?", "Bravery, Repetition and Noise" ),
      ( "Which album features the song 'Wish I Could Fly'?", "Give It Back!" ),
      ( "Which album features the song 'The Clouds Are Lies'?", "Aufheben" ),
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

# run the main function
if __name__ == "__main__":
  main()
