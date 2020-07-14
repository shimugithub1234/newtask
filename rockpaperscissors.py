import random

list_1=["rock","paper","scissor"]

print("------GAME------")
print("\nChoices: \n\n0-ROCK,\n1-PAPER,\n2-SCISSOR")



a_random_number = random.randint(0,2)

def play(user_input):
	if user_input>2 :
		print('ENTER VALID NUMBER FROM CHOICES')
	else:
		print("Your input is:",list_1[user_input].upper(),"and Computer input is:",list_1[a_random_number].upper())

		if list_1[user_input] == list_1[a_random_number]:
			print('ITS A TIE !!!')
		elif list_1[user_input] == "rock":
			if list_1[a_random_number] == "paper":
				print('YOU LOOSE !!!')
			else:
				print('YOU WIN !!!')
		elif list_1[user_input] == "paper":
			if list_1[a_random_number] == "rock":
				print('YOU WIN !!!')
			else:
				print('YOU LOOSE !!!')
		elif list_1[user_input] == "scissor":
			if list_1[a_random_number] == "rock":
				print('YOU LOOSE !!!')
			else:
				print('YOU WIN !!!')
		else:
			print('ERROR !!!')

user_input=int(input("\nEnter your Choice :"))
play(user_input)
while True:
  print("Do you want to play again? (Y/N)")
  ans = input()
  if ans == 'y' or ans == 'Y': 
    user_input=input("\nEnter your Choice :")
    play(int(user_input))
  else:
    exit()