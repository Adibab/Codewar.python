import random

# print ( "Welcome to the Band name generator")
# a = input("whats's the name of the city you grew up in?\n")
# print(a)
# b = input("whats your pet name? \n")
# print (b)
# print (f"Your band name could be {a} {b}")

# a = input( "whats your name \n")
# b=len(a)
# print (type(b))
# print(f"number of letters :{b}")

# a = int("5") / int(2.7)
# print(type(a))

# total_bill =input("what was the total bill? \n")
# # print(type(total_bill))
# tip = input ( " what percentage tip you like to give? 10, 12 or 15 \n")
# tip_cal= int(tip)/100
# print(tip_cal)
# num_ppl = input("how many ppl to split? \n")
# # print(type(num_ppl))
# # print (int(total_bill))
# # print(int(num_ppl))

# per_person_bill = ( round((int(total_bill) * tip_cal) + int(total_bill) / int(num_ppl)))

# # print(type(per_person_bill))

# print(f"each person should pay: {per_person_bill}")


# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi 

# for number in range(1, 101):
#   # First check if the number is divisible by both 3 and 5.
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
 
#   # Then check if the number is only divisible by 3
#   elif number % 3 == 0:
#     print("Fizz")
 
#   # Finally check if the number is only divisible by 5
#   elif number % 5 == 0:
#     print("Buzz")
 
#   # If it's not divisible by either of those numbers, just print the number
#   else:
#     print(number)



# wordlist=  ["hippo", "baboon", "camel"]

# random_word= random.choice(wordlist)
# print(random_word)


# user_word= input("Guess a word \n").lower()
# print (user_word)
# for word in wordlist:
#     if word == user_word:
#         print ( "Right")
#     else:
#         print("Wrong")
        
 # creating placeholder
 
# placeholder= ""
# length_of_random_word = len(random_word)

# for word in range(length_of_random_word):
#     placeholder += "_"
# print (placeholder)
    


#task 3 
# display = ""

# user_word= input("Guess a word \n").lower()
# # print (user_word)
# for word in random_word:
#     if word == user_word:
#         display += word
#     else:
#         display += "_"
# print(display)




























   
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print(chosen_word)


# lives = len(chosen_word)
# correct_letter = []

# game_over = False
# while not game_over:
#     placeholder = ""
#     display = "_"
   

#     guess = input("Guess a letter \n").lower()

#     for letter in chosen_word:
#        if letter == guess:
#         # print (letter)
#           placeholder += letter
#         # print(placeholder)
#           correct_letter.append(guess)
#         # print(correct_letter)
#        elif letter in correct_letter:
#            placeholder += letter

#        else:
#         placeholder+= display
#     print(placeholder)
    
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("you lose)")
            
    
#     if display not in placeholder:
#          game_over = True
#          print("you win")
        
        
        
# def life_in_weeks(current):

#  age_left = (52 * 90) - (current * 52)

#  print(f"You have {age_left} weeks left")
    
            


# print(life_in_weeks(36))

# def calculate_love_score(name1, name2):
#     name1_lower = name1.lower()
#     name2_lower =  name2.lower()
    
#     true_letter= "true"
#     love_letters = "love"
    
#     true_count = 0
#     love_count = 0
    
#     for letter in true_letter:
#         true_count+= name1_lower.count(letter)
#         true_count+= name2_lower.count(letter)
#     # print(true_count)
#     # print(type(true_count))
    
#     for letter in love_letters:
#         love_count+= name1_lower.count(letter)
#         love_count+= name2_lower.count(letter)
#     # print(love_count)
#     love_score = int(str(true_count) +str(love_count))
    
#     print(love_score)
 
    
 
# print(calculate_love_score("Kanye West", "Kim Kardashian"))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt( original_text,  shift_amount):
#      list = []
#      encrypted_text =""
   
#      for letter in original_text:
#           # list.append(alphabet.index(letter)+shift_amount)
#           shifted_position=alphabet.index(letter)+shift_amount
#           print(shifted_position)
#           shifted_position %= len(alphabet)
#           print(shifted_position)
#           encrypted_text+=alphabet[shifted_position]
#      print(encrypted_text)
     
     
# def decrypt(original_text, shift_amount ):
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)-shift_amount
#         print(alphabet[shifted_position])
        

          
# print(decrypt("h", 2)) 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades ={}
#
# for key in student_scores:
#           if student_scores[key] > 91:
#              student_grades.update({key : "Outstanding"})
#           # print(student_grades)
#           elif student_scores[key] > 81:
#                student_grades.update({key : "Exceeds Expectations"})
#           elif student_scores[key] > 71:
#                student_grades.update({key : "Acceptable"})
#           else:
#                student_grades.update({key : "Fail"})
# print(student_grades)



def is_even(n):
    if n % 2 == 0 :
        return "True"
    else:
        return "False"
    # your code here

is_even(4)
is_even(-3)
is_even(2.5)
is_even(-3.5)
is_even(0)
is_even(0.5)
               
          
          


     