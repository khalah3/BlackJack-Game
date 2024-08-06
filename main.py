import random
import clear
from art import logo
print(logo)

continue_game = True

while continue_game:



  list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  player_cards=[]
  computer_cards=[]
  for i in range(2):
    player_cards.append(random.choice(list))
  for i in range(1):
    computer_cards.append(random.choice(list))
  print(f'Player cards are : {player_cards}\n')
  print(f'Player_score:{sum(player_cards)}\n')
  print(f'First_computer_card:{sum(computer_cards)}\n')
  
  if sum(player_cards)==21 and len(player_cards)==2:
    print('Player has a blackjack')
    

  
  def more_cards():
    choice=input("Type y to get another card, type n to pass\n\n")
    if choice=='y':
      for i in range(1):
         player_cards.append(random.choice(list))
         print(player_cards)
         if sum(player_cards) >21 and 11 in player_cards:
           player_cards.remove(11)
           player_cards.append(1)
         if sum(player_cards)>21:
           print("You lose. Game Over\n")
         else:
           more_cards()
    elif choice=="n":
      print("No more draws\n")
    sum_of_player_cards=sum(player_cards)
    return sum_of_player_cards
   
  
  player_score=more_cards()
  
  print(f'Player Score is {player_score}\n')
  
  
  def computer_draw():
    if player_score <=21:
      computer_cards.append(random.choice(list))
      while sum(computer_cards) <17:
        computer_cards.append(random.choice(list))
      print(f'The computer cards are {computer_cards}\n')
      if sum(computer_cards) > 21:
        print (f"Computer score is {sum(computer_cards)}\n")
        print("Player wins\n")
      elif sum(computer_cards) > player_score:
        print (f"Computer score is {sum(computer_cards)}\n")
        print("Dealer wins\n")
      elif sum(computer_cards) == player_score:
        print (f"Computer score is {sum(computer_cards)}\n")
        print("It's a draw\n")
      elif sum(computer_cards) < player_score:
        print (f"Computer score is {sum(computer_cards)}\n")
        print("Player wins\n")
      
  
  computer_draw()
  
  another_game=input('Do you want to play another game? Type y or n\n')
  
  if another_game== 'y':
    clear.clear()
    print(logo)
  else:
    continue_game=False


  
  
                   
                   
                   
  
    
    
    

    
    
  
  
  




