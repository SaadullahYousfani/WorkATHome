# -*- coding: utf-8 -*-
"""GuessingGame2.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_f9lyRuPurcIYFRP-ZmZyDCp2t-OmMPL
"""

print("Hello World 14'May'2023")

answer = 4

print(answer)

print("Enter the Number between 1 and 10: ")
guess = int(input())

if guess != answer:
  if guess > answer:
    print("Please Guess lower")
    guess = int(input())
    if guess == answer:
      print("You guessed it! ")
    else:
      print("Invalid Guess! Refresh the Program")
  
  if guess < answer:
      print("Please Guess Higher")
      guess = int(input())
      if guess == answer:
        print("You guessed it! ")
      else:
        print("Invalid Guess! Refresh the Program")

else:
  print("You got it you guessed it first Try Congratulations: :)")