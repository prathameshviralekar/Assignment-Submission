# -*- coding: utf-8 -*-
"""Data Science - Batch 1 - Assignment 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15C4sjo_qI2-MbmptuAkmFB-_taP49mg0
"""

# Questions 1: 
# Given the following jumbled word, OBANWRI guess the correct English word. 
# A. RANIBOW B. RAINBOW C. BOWRANI D. ROBWANI

word_list = ["RANIBOW","RAINBOW","BOWRANI","ROBWANI"]
guess_word = "RAINBOW"
guess = " "

while guess_word!= guess.upper() and guess_word!= word_list:
    guess = input("Enter Guess Word : ")

print("You guess correct word",guess)

# Questions 2:
# Write a program which prints “LETS UPGRADE”. (Please note that you have to print in ALL CAPS as given)

String = input("Please enter string : ")
print(String.upper())

# Questions 3:
# Write a program that takes cost price and selling price as input and displays whether the transaction is a Profit or a Loss or Neither. 
# INPUT FORMAT The first line contains the cost price. The second line contains the selling price. 
# OUTPUT FORMAT Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither profit nor loss, print "Neither". 
# (You must not have quotes in your output)

CP = float(input(" Please Enter the Cost Price of the product: "))

SP = float(input(" Please Enter the Sale Price of the product: "))

if(CP > SP):

   amount = CP - SP

   print("Total Loss Amount : ",amount)

elif(SP > CP):

   amount = SP - CP

   print("Total Profit : ",amount)

else:

   print("There is no Profit no Loss....")

# Questions 4:
# Write a program that takes an amount in Indian Rupees as input. You need to find its equivalent in Euro and display it. 
# Assume 1 Euro equals Rs. 80. Please note that you are expected to stick to the given input and output format as in sample test cases. 
# Please don't add any extra lines such as 'Enter a number', etc.
# Your program should take only one number as input and display the output.

euro = float(input("Please Enter Euro:"))
rupees = euro * 80
print(rupees, " Rupees")