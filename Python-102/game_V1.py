import random

# Updated version 

'''
options = ('rock', 'paper', 'scissors')

Before we used the option variable as a global one, but since we are doing the function I'm going to make it a variable just for the contest of the funtion 
'''

# Choose options

def choose_options():
  options = ('rock', 'paper', 'scissors')
  user1 = input("rock, paper, scissors ")
  user1 = user1.lower()
  
  if not user1 in options:
    print('that element is not available in the game')
    # continue
    return None, None
  
  comp1 = random.choice(options)
  
  print('user option: ', user1)
  print('computer option: ', comp1)

  return user1, comp1 

'''
import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('esa opcion no es valida')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

'''

# Game rules

def game_rules(user1, comp1, user_wins, computer_wins):
  if user1 == comp1:
    print("tie")
  elif user1 == "rock":
    if comp1 == "scissors":
      print("rock wins against scissors")
      print("user wins")
      user_wins += 1
    else:
      print("paper wins against rock")
      print("computer wins")
      computer_wins += 1
  elif user1 == "paper":
    if comp1 == "rock":
      print("paper wins againts rock")
      print("user wins")
      user_wins += 1
    else:
      print("scissors wins againts paper")
      print("computer wins")
      computer_wins += 1
  elif user1 == "scissors":
    if comp1 == "paper":
      print("scissors wins againts paper")
      print("user wins")
      user_wins += 1
    else:
      print("rock wins against scissors")
      print("computer wins")
      computer_wins += 1
      
  return user_wins, computer_wins

'''
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins

'''
  
# Main code of the game

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
    print('')
    print('')
    print('ROUND ', rounds)
    
    print('user wins', user_wins)
    print('computer wins', computer_wins)
    
    rounds += 1 

    user1, comp1 = choose_options()
    #I need to verify what option has each player
    user_wins, computer_wins = game_rules(user1, comp1, user_wins, computer_wins)
 
    if user_wins == 2:
      print('')
      print('THE USER WINS!')
      print('GAME OVER')
      break
  
    if computer_wins == 2:
      print('')
      print('THE USER WINS!')
      print('GAME OVER')
      break

run_game()

'''
def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break

run_game()

def result():
    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break
      user_wins, computer_wins = run_game(user_wins, computer_wins)

result()

'''


# Previous version

'''
options = ('rock', 'paper', 'scissors')

user_wins = 0
computer_wins = 0
rounds = 1

while True:

  print('')
  print('')
  print('ROUND ', rounds)
  
  user1 = input("rock, paper, scissors ")
  user1 = user1.lower()
  
  if not user1 in options:
    print('that element is not available in the game')
    continue
  
  comp1 = random.choice(options)
  
  print('user option: ', user1)
  print('computer option: ', comp1)
  
  if user1 == comp1:
    print("tie")
  elif user1 == "rock":
    if comp1 == "scissors":
      print("rock wins against scissors")
      print("user wins")
      user_wins += 1
    else:
      print("paper wins against rock")
      print("computer wins")
      computer_wins += 1
  elif user1 == "paper":
    if comp1 == "rock":
      print("paper wins againts rock")
      print("user wins")
      user_wins += 1
    else:
      print("scissors wins againts paper")
      print("computer wins")
      computer_wins += 1
  elif user1 == "scissors":
    if comp1 == "paper":
      print("scissors wins againts paper")
      print("user wins")
      user_wins += 1
    else:
      print("rock wins against scissors")
      print("computer wins")
      computer_wins += 1
  print('user wins', user_wins)
  print('computer wins', computer_wins)

  if user_wins == 2:
    print('')
    print('THE USER WINS!')
    print('GAME OVER')
    break

  if computer_wins == 2:
    print('')
    print('THE USER WINS!')
    print('GAME OVER')
    break
    
  rounds += 1 

'''