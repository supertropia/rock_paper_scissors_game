import random
rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice=int(input("What do tou choose? "
                      "type:\n 0 for rock, "
                     "1 for paper , "
                      "2 for scissors :  "))

computer_choice = random.randint (0,2)

print(f"********** User choice : {user_choice} **********\n")

print(f"********** Computer choice : {computer_choice} **********\n")

if user_choice == 0 and computer_choice == 0: #rock and rock
    print(f"user choice{rock}\n and computer choice {rock} The match ended in a draw. Game over")
if user_choice ==0 and computer_choice == 1: # rock and paper
    print(f"user choice{rock}\n and computer choice {paper}. Computer win!, you lose!!!.")
if user_choice ==0 and computer_choice == 2 : #rock and scissors
    print(f"user choice{rock}\n and computer choice {scissors}. You win! computer lose!!!.")


if user_choice ==1 and computer_choice == 0 :#paper and rock
        print(f"user choice{paper}\n and computer choice {rock}. You win!!! Computer lose!!.")
if user_choice == 1 and computer_choice == 1:# paper and paper
    print(f"user choice{paper}\n and computer choice {paper}. The match ended in a draw. Game over.")
elif user_choice == 1 and computer_choice == 2: #paper and scissors
    print(f"user choice{paper}\n and computer choice {scissors}. Computer win!!!, You lose!!.")


if user_choice == 2 and computer_choice == 0: #scissors and rock
        print(f"user choice{scissors}\n and computer choice {rock}. Computer lose!!!, You win!!.")
if user_choice == 2 and computer_choice == 1: #scissors and paper
        print(f"user choice{scissors}\n and computer choice {paper}.You win!! Computer lose, .")
if user_choice == 2 and computer_choice == 2:  # scissors and scissors
    print(f"user choice{scissors}\n and computer choice {scissors}. The match ended in a draw. Game over!!.")
