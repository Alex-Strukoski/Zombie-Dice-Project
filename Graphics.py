from os import system, name
from time import sleep
import pygame
import ZombieDice
  

class gameGraphics:#Graficos estaticos
    menuStatic = """
  ╔══════════════════════•Z̴̨̲̟̘̘̟̹̩̤̘̤͖͕͍͚͑̐̂̒Ö̶̥̦̯̼̦̼̮̲͝M̷̡̢̨̛̛͚͚̪̫͖͆̊͑͂̐̒́̉͗̇̂́͠B̸̨̞̘̝̜͙̞̝̪͕̦̓͂̄́̐̿́͊̃̿̓̊̅̚͠Į̶̺̤͎͙̞̈́̓̅̔̊̀̂́͝͠Ę̶͖̭̪̱̟͚͍͚͕̂̾̾̏́̅̃̀̿̅͋̓͛͒̔̍̈͝•════════════════════╗ 
    ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ☰ ☱ ☲ ☶ ☲
	
          Para ver as regras digite [regras]
        para ver os créditos digite [creditos] 
    para sortear quem vai por primeiro digite [first]
          para iniciar o jogo digite [start] 
	        E para sair digite [exit]

    ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ☰ ☱ ☶ ☶
  ╚═══════════════════════•Ḑ̸̢̡̛̛̤͔̳̙̺͙̙̳́͑̌́̀̈́̒̄̀̉̕͜ͅǏ̷̘͗̑͜C̸̰̪̞͙̼̼̭̙̣̮̩̬̤̾͜ͅE̶̛͍̒͋͐̉̔̈́̆̑̑͌•═════════════════════╝  
    """
    severedHand = """
                                                                    ▒▒░░░░              ░░░░░░                        
                                                      ░░░░        ░░░░░░  ░░          ░░░░░░  ░░                      
                                                    ▓▓░░░░▓▓      ░░░░    ░░          ░░░░    ░░                      
                                                  ▒▒░░    ░░      ░░░░    ░░          ░░░░    ░░                      
                                                  ░░░░    ░░      ░░░░░░░░░░          ░░░░    ░░                      
                                                ▓▓░░░░  ░░▓▓      ░░░░░░░░░░        ░░░░  ░░  ░░                      
                                                ░░░░░░░░░░      ▓▓░░░░░░░░░░        ░░░░  ░░░░▒▒                      
                                    ▒▒░░        ░░░░░░░░░░      ░░░░░░░░░░░░        ░░░░    ░░                        
                                  ░░░░  ░░      ░░░░░░░░░░      ░░░░░░░░░░░░      ░░░░░░░░  ░░                        
                                  ░░░░  ░░      ░░░░░░░░░░      ░░░░░░░░░░░░      ░░░░░░░░  ░░                        
                                  ░░░░  ░░      ░░░░░░░░░░      ░░░░░░░░░░░░      ░░░░░░░░  ░░                        
                                  ░░░░  ░░      ░░░░░░░░░░      ░░░░░░░░░░░░    ▓▓▒▒░░░░░░  ░░                        
                                  ░░░░░░░░▒▒    ░░░░░░░░░░      ░░░░░░░░░░░░    ░░░░░░░░░░  ░░                        
                                  ░░░░░░░░░░    ░░░░░░░░░░░░    ░░░░░░░░░░      ░░░░░░░░░░░░                          
                                  ░░░░░░░░░░      ░░░░░░░░░░    ░░░░░░░░░░      ░░░░░░░░░░░░                          
                                  ░░░░░░░░░░      ░░░░░░░░░░  ░░░░░░░░░░░░    ░░░░░░░░░░░░░░                          
                                  ░░░░░░░░░░      ░░░░░░░░░░  ░░░░░░░░░░░░    ░░░░░░░░░░░░░░                          
                                  ░░░░░░░░░░▒▒    ░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▓▓                          
                                  ░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░  ░░                    ░░░░    
                                    ░░░░░░░░░░░░░░  ░░░░░░  ░░░░      ░░░░░░░░░░░░░░░░  ░░                ░░░░      ▒▒
                                    ░░░░░░░░░░    ░░░░    ░░░░░░░░░░░░░░░░░░░░░░        ░░              ░░          ░░
                                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░              ░░          ░░
                                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░            ░░░░░░░░    ░░░░
                                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░          ░░  ░░░░░░░░░░░░▓▓
                                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░░░░░░░  
                                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░  ▒▒▓▓  
                                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░  ░░▒▒    
                                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ▒▒░░░░░░░░░░  ░░░░      
                                      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░  ░░░░░░░░  ░░░░        
                                       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░  ▒▒░░        
                                       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░          
                                       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
                                       ░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░▒▒▓▓            
                                       ░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                
                                       ░  ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                  
                                       ▒   ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                   
                                       ▒    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                    
                                             ▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                      
                                       ▒      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                        
                                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                          
                                              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓                          
                                              ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░                            
                                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                
                                                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                
                                                  ░▒░░░ ░▒░░▒░░▒░░▒░░░▒░░▒░░░░░▒░ ░▒░░▒
                                                  ▒░░▒▒▀▒░░▒░░░▒▓░▒▒▀▒░▓▒▓░░▒░░▒▒▀▒░░▒░
                                                  ▒ ░ ░ ░  ░ ░▒ ░ ░ ░  ░ ░▒ ░ ░ ░  ░ ░▒ 
                                                  ░   ░    ░  ░░   ░    ░  ░░   ░    ░  
                                                  ░     ░ ░     ░░░     ░ ░     ░ ░     
                                                                 ░
                                                  ░
"""
    hand = """
                                           ▒▒██                                        
                                      ▒▒██    ▒▒██                                      
                                        ▒▒██  ▒▒██  ▒▒██                                
                                ▒▒▒▒    ▒▒██  ▒▒██  ▒▒██                                
                                ██▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                                
                                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ▒▒██                            
                                  ████▒▒▒▒▒▒████▒▒██  ▒▒▒▒██                            
                                      ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒██                              
                                        ▒▒██▒▒▒▒▒▒▒▒████                                
                                        ▒▒▒▒▒▒▒▒████                                    
                                        ▒▒▒▒████                                        
                              ▒▒        ▒▒▒▒▒▒██                                        
                                  ▒▒    ▒▒▒▒▒▒██        ▒▒                              
                                      ██▒▒▒▒▒▒██▒▒██                                    
                              ██████▒▒▒▒▒▒▒▒▒▒██▒▒██                                    
                                        ██▒▒  ██  ██▒▒██                                
                                  ████                  ██ 
    """
    winner = """
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝                                                    
    """
    loser = """
    ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄ 
     ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌
      ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌
      ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌
      ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ 
       ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ 
     ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ 
     ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ 
     ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    
     ░ ░                           ░                  ░      
    """
    rollingDices = """                   
                  ________
                 /\       \ 
                /  \       \ 
               /    \       \ 
              /      \_______\ 
              \      /       /
            ___\    /   ____/___
           /\   \  /   /\       \ 
          /  \   \/___/  \       \ 
         /    \       \   \       \ 
        /      \_______\   \_______\ 
        \      /       /   /       /
         \    /       /   /       /
          \  /       /\  /       /
           \/_______/  \/_______/ """
    rolling = f"▒█▀▀█ ▒█▀▀▀█ ▒█░░░ ▒█░░░ ▀█▀ ▒█▄░▒█ ▒█▀▀█\n▒█▄▄▀ ▒█░░▒█ ▒█░░░ ▒█░░░ ▒█░ ▒█▒█▒█ ▒█░▄▄ \n▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄█ ▄█▄ ▒█░░▀█ ▒█▄▄█"
    dino = """      
                    ████████████████                                        
              ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████                                  
            ▓▓██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░██▓▓                                
            ██  ██░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░██  ██                                
            ██▒▒██░░░░░░░░▒▒▒▒░░░░░░░░██▒▒██                                
              ████░░░░░░░░░░░░░░░░░░░░████                                  
            ██░░██░░░░░░░░░░░░░░░░░░░░██░░██                                
            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                                
          ██░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░██                              
          ██░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░██                              
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
        ██░░████░░░░░░░░░░░░░░░░░░░░░░░░████░░██                            
        ██░░██▒▒██████░░░░░░░░░░░░██████▒▒██░░██                            
        ██░░██░░▒▒  ▒▒████████████▒▒  ▒▒░░██░░██                            
        ██░░██░░▒▒▒▒▒▒░░▒▒░░░░▓▓░░▒▒▒▒▒▒░░██░░██                            
          ██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██                              
          ██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██                              
            ██░░██  ▒▒  ▒▒    ▒▒  ▒▒  ██░░██                                
            ████▒▒████▓▓██▓▓████▓▓██▓▓░░████                                
            ██▒▒██░░░░░░░░░░░░░░░░░░░░██▒▒██                                
            ██▒▒░░████████████████████░░▒▒██                                
          ██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██                              
          ██▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██                              
          ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██                        ██████
          ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██                    ▓▓██▒▒░░██
        ██▒▒▒▒░░██░░██░░░░░░░░░░░░██░░██░░▒▒▒▒██              ████▒▒░░░░██  
        ██▒▒░░░░██░░██░░░░░░░░░░░░██░░██░░░░▒▒██            ██▒▒▒▒░░░░██    
        ██▒▒░░██░░██░░░░░░░░░░░░░░░░██░░██░░▒▒██          ██▒▒▒▒░░░░██      
        ██▒▒░░██░░██░░░░░░░░░░░░░░░░██░░██░░▒▒██        ██▒▒▒▒░░░░░░██      
      ██▒▒░░░░░░████░░░░░░░░░░░░░░░░████░░░░░░▒▒██    ██▒▒▒▒░░░░░░██        
      ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██████▒▒▒▒░░░░░░░░██        
      ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒▒▒▒▒░░░░░░░░██          
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██▒▒░░░░░░░░░░██          
    ██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██░░░░░░░░░░██            
    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░██            
    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░██              
    ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░██                
      ▓▓░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░░░██░░░░▓▓██                  
      ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██████                      
        ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██                            
          ██░░░░██░░░░░░░░░░░░░░░░░░░░██░░░░██                              
            ██░░░░████████████████████░░░░██                                
            ██░░░░██                ██░░░░██                                
            ██░░░░██                ██░░░░██                                
            ██░░░░██                ██░░░░██                                
            ██▓▓░░██                ██░░▓▓██                                
          ██▒▒▒▒░░██                ██░░▒▒░░██                              
          ██████████                ██▓▓██▓▓██   
     ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄            ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░░░░░░░░░░░▌
    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌
    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀                            
    """
    sus = "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
    gameTitle = """
    ▒███████▒ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓▓█████    ▓█████▄  ██▓ ▄████▄  ▓█████ 
    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▓█   ▀    ▒██▀ ██▌▓██▒▒██▀ ▀█  ▓█   ▀ 
    ░ ▒ ▄▀▒░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▒███      ░██   █▌▒██▒▒▓█    ▄ ▒███   
      ▄▀▒   ░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▒▓█  ▄    ░▓█▄   ▌░██░▒▓▓▄ ▄██▒▒▓█  ▄ 
    ▒███████▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░░▒████▒   ░▒████▓ ░██░▒ ▓███▀ ░░▒████▒
    ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░░ ▒░ ░    ▒▒▓  ▒ ░▓  ░ ░▒ ▒  ░░░ ▒░ ░
    ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░ ░ ░  ░    ░ ▒  ▒  ▒ ░  ░  ▒    ░ ░  ░
    ░ ░ ░ ░ ░░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░       ░ ░  ░  ▒ ░░           ░   
      ░ ░        ░ ░         ░    ░       ░     ░  ░      ░     ░  ░ ░         ░  ░
    ░                                  ░                ░          ░               
    """
    finaltext = "▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ █░█ █▀▀ \n░▒█░░ █▀▀█ █▄▄█ █░░█ █▀▄ ▀▀█ \n░▒█░░ ▀░░▀ ▀░░▀ ▀░░▀ ▀░▀ ▀▀▀ "


def skull(a=10): #Aqui começa as animações
    '''
    :param a: it's an integer, if none is given then the param is 10.
    :return: none
    '''
    for skull in range(a):
        print("""
                ██████████████                
            ██████████████████████            
        ██████████████████████████████        
      ██████████████████████████████████      
    ██████████████████████████████████████    
  ██████████████████████████████████████████  
  ██████████████████████████████████████████  
████████████████████████████████████████████
████████████████████████████████████████████
████████████████████████████████████████████
████████████████████████████████████████████
  ██████████████████████████████████  ████
  ████████      ██████      ████████  ████
████  ████████████  ██  ████████████  ██████
████  ██████████████████████████████  ██████
  ████  ██        ████  ████        ██  ████  
  ██  ██              ██              ██  ██  
    ██              ██████              ██    
    ██              ██████              ██    
  ████            ████  ████            ████  
  ██████      ██████      ██████      ██████  
  ████  ██████    ██      ██    ██████  ████  
  ██████      ██████      ██████      ██████  
    ████████  ██████  ██  ██████  ████████    
      ████  ██████████████████████  ████      
              ██████████████████              
        ██    ██  ████  ████  ██    ██        
        ██    ██  ████  ████  ██    ██        
        ██                          ██        
        ██    ██  ████  ████  ██    ██        
          ██  ██  ████  ████  ██  ██          
            ██████████████████████            
            ██████████████████████            
                ██████████████    
                
 
     ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █ 
    █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ 
    ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  
      █   █   █   █   █   █   █   █   █   █ 
    ▄▀   █  ▄▀   █  ▄▀   █  ▄▀   █  ▄▀   █  
    █    ▐  █    ▐  █    ▐  █    ▐  █    ▐  
    ▐       ▐       ▐       ▐       ▐       
                
""")    
        pygame.mixer.init()
        pygame.mixer.music.load('hehehe.wav')
        pygame.mixer.music.play()
        sleep(1)
        ZombieDice.clearScreen()
        print("""
                ██████████████                
            ██████████████████████            
        ██████████████████████████████        
      ██████████████████████████████████      
    ██████████████████████████████████████    
  ██████████████████████████████████████████  
  ██████████████████████████████████████████  
████████████████████████████████████████████
████████████████████████████████████████████
████████████████████████████████████████████
████████████████████████████████████████████
  ██████████████████████████████████  ████
  ████████      ██████      ████████  ████
████  ████████████  ██  ████████████  ██████
████  ██████████████████████████████  ██████
  ████  ██        ████  ████        ██  ████  
  ██  ██              ██              ██  ██  
    ██              ██████              ██    
    ██              ██████              ██    
  ████            ████  ████            ████  
  ██████      ██████      ██████      ██████  
  ████  ██████    ██      ██    ██████  ████  
  ██████      ██████      ██████      ██████  
    ████████  ██████  ██  ██████  ████████    
      ████  ██████████████████████  ████      
        ██    ██  ████  ████  ██    ██        
        ██    ██  ████  ████  ██    ██        
        ██    ██  ████  ████  ██    ██        
          ██  ██  ████  ████  ██  ██          
            ██████████████████████            
            ██████████████████████            
                ██████████████    
                
        
     ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █  ▄▀▀▄ █ 
    █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ █  █ ▄▀ 
    ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  ▐  █▀▄  
      █   █   █   █   █   █   █   █   █   █ 
    ▄▀   █  ▄▀   █  ▄▀   █  ▄▀   █  ▄▀   █  
    █    ▐  █    ▐  █    ▐  █    ▐  █    ▐  
    ▐       ▐       ▐       ▐       ▐       
                
""")
        sleep(1)
        ZombieDice.clearScreen()
	
	
def limit(t=0):
  ZombieDice.clearScreen()
  loadingText = []
  text = "LIMITE DE TENTATIVAS EXCEDIDO"
  for letter in text:
    loadingText.append(letter)
    print(f"{ZombieDice.colors.red}{''.join(loadingText)}")
    sleep(t)
    ZombieDice.clearScreen()
  for pulse in range(5):
    print(text, ZombieDice.colors.reset)
    sleep(1)
    ZombieDice.clearScreen()
    print(text, ZombieDice.colors.red)
    sleep(1)
    ZombieDice.clearScreen()
	

def loading(a=2, t=0.5):
    '''
    :param a: it's an integer, if none is given then the param is 2.
    :param t: it's an integer, the time for it to loop, if none is given then the param is 0.5
    :return: none
    '''
    sleep(0.5)
    space = " " * (a * (a*2))
    downSpace =  "\n" * ((a - 1) * 2)
    if a > 7: 
      space = " " * a
      downSpace =  "\n" * a
    sleep(t)
    print(downSpace)
    print(space, f"{ZombieDice.colors.red}░▒████ ████▒░")
    sleep(t)
    print(space, "░▒███   ███▒░")
    sleep(t)
    print(space, "░▒██     ██▒░")
    sleep(t)
    print(space, "░▒█       █▒░")
    sleep(t)
    print(space, "░▒    ຶ༎    ▒░")
    sleep(t)
    print(space, "▒  L̸̢̨̹͓̗͍̹̞̺̳͚̬̻͖͈̫̟̝̻̮̩̤̱̹̝̗̲̮̎̾̅̓͑́̓̈́̐̍̎̀͂́̓̆͛̌͐͒̓͒̄̾̐͛̓͌̚̕̚͜͜͠ͅͅͅO̶͎̭̪̦̺̗̙̯͉̮̱̪̲͕̮̹̩̾̈̂̉͘A̵̧̨̢̧͍͙̲̦͚͉̲̭̤̟͖̫̖͙̪̗̟̳̼̪͍̦̠̍͌͌̓̍̓͌̑̓͋͒̄̆̌̓̔͗̊̒͂͗͒͛̈͒̉̕͜͜͝͝͠D̷̢̨̡̡̨͕̱͔̜͚̬̬̪̟̭̺̟̭̰͙͓̘̗̟̖̫͖̻͔͎̈́̈̎̈́̒̒̿͗́̅͛̇̔̓̀̂̎̔́͐̐͋͗̏̓̊̆̊̈́̊̕͜͜͝ͅI̴̢͖͔̼̦͍͇̻͙̲͓̦͇͖̩̜̖̥͈̒̄Ṉ̵̡̢̢̼̼͕̪̪͕̘̙̠͚̝̘̤͙̯̩̝̬͚̟̩̻͇͎̝̇͛͒̀̓͊͋̀͌̀͌̊͊̂̈͌̀̾̒̄̚͜͜͠ͅͅĢ̴̧̡̛̗͔̮̦͖͙̱̝̩̠͖͔̥̘̏̽̈́̑̓̒̆͐̿̓̾̃̿̈́͘  ▒")
    sleep(t)
    print(space, "░▒  Ģ̵̢̢̡̩̮̦̻̯͍͈̰̱̳̦͎̻͎̲͍̫̩̦̜̹͔̩̫̥̣̥̆͆̒̈̏̈́̊̾̾̈́̾̍̊̑͂͜͜͝͠Ǎ̴̢̨̡̞̥̺̜̟̲̮̦͚̦̬̠̠͈̤̘͚̥̺̣̥̻͇̰̙͙̩͙̋̊͊̈̍͛̿͌͌̀̚͜͝͝ͅM̵̘̬̥̭̗̼͖̳̣̫͔̰̻͉̮͌̿̽̽̔̌͆̎̐̀̔͋͒̿͂̋̅͋͌͗͂̓̀͐͗̃͘̕̚̚͜͝E̵̝͙̩͔͓̳͆̈́̃͂̑̃́͐̏̒̾͘   ▒░")
    sleep(t)
    print(space,f"░▒█       █▒░")
    sleep(t)
    print(space, "░▒██     ██▒░")
    sleep(t)
    print(space, "░▒███   ███▒░")
    sleep(t)
    print(space, "░▒██▒█ █▒██▒░")
    print(space, "▒▓█▒▒▀▒░▓▒▓█░")
    print(space, "▒ ░ ░ ░  ░ ░ ")
    print(space, "░   ░    ░  ░")
    print(space, "░     ░  \n", ZombieDice.colors.reset)
    sleep(t)
    ZombieDice.clearScreen()
            
def loadingDice(t=0.2):
    ZombieDice.clearScreen()
    sleep(t)
    print("⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚅ ⚂")
    print("⚄ ⚃")
    print("⚂ ⚁ ⚀")
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚅ ⚂")
    print("⚄ ⚃")
    print("⚂")
    print("  ⚁ ⚀")
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n\n⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚅ ⚂")
    print("⚄ ⚃")
    print("⚂")
    print("     ")
    print("  ⚁ ⚀")
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n\n\n⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚅ ⚂")
    print("⚄ ⚃")
    print(" ")
    print("⚂    ")
    print("     ")
    print("  ⚁ ⚀")
    sleep(t)
    pygame.mixer.init()
    pygame.mixer.music.load('Rolling-Dice.wav')
    pygame.mixer.music.play()
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚅ ⚂")
    print("          ⚀")
    print("⚄⚃ ⚂ ⚁ ⚀")
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n\n\n⚄")
    print("⚄ ⚃ ⚅")
    print("⚄ ⚃ ⚄ ⚃ ⚅ ⚂⚂ ⚁    ⚀")
    sleep(t)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n\n\n\n\n⚄⚃ ⚅ ⚄ ⚃  ⚅ ⚄ ⚃   ⚂ ⚄ ⚃ ⚂ ⚁ ⚀")
    sleep(0.4)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀")
    sleep(1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀", ZombieDice.colors.reset)
    sleep(1)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀")
    sleep(1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀", ZombieDice.colors.reset)
    sleep(1)
    ZombieDice.clearScreen()
    print("\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀")
    sleep(1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.green}\n\n\n\n\n\n\n\n\n\n⚄ ⚃ ⚅ ⚄ ⚃ ⚅ ⚄ ⚃ ⚂ ⚄ ⚃ ⚂ ⚁ ⚀", ZombieDice.colors.reset)
    sleep(3)
    ZombieDice.clearScreen()
    

def newTurn():
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}I{ZombieDice.colors.reset}niciando mais uma rodada do turno atual.")
    print(f"{ZombieDice.colors.red}▒", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░", ZombieDice.colors.reset)
    sleep(0.5)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}Inic{ZombieDice.colors.reset}iando mais uma rodada do turno atual.")
    print(f"{ZombieDice.colors.red}▒▓██", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒ ▒ ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░   ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░   ", ZombieDice.colors.reset)
    sleep(0.5)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}Iniciando{ZombieDice.colors.reset} mais uma rodada do turno atual.")
    print(f"{ZombieDice.colors.red}▒▓███▀▒░▓", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒ ▒ ░ ░ ░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░     ░  ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░   ░   ", ZombieDice.colors.reset)
    sleep(0.5)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}Iniciando mais uma{ZombieDice.colors.reset} rodada do turno atual.")
    print(f"{ZombieDice.colors.red}▒▓███▀▒░▓▒▓███▀▒░▓", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒   ░ ░ ░▒▒▒ ░ ░ ░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░     ░  ░░▒  ░    ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░ ░        ░    ░   ", ZombieDice.colors.reset)
    sleep(0.5)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}Iniciando mais uma rodada do turno a{ZombieDice.colors.reset}tual.")
    print(f"{ZombieDice.colors.red}▒▓███▀▒░▓▒▓███▀▒░▓▒▓█░▒▀▒░▓▒▓█▒█▀▒░▓", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒ ▒ ░ ░ ░▒▒▒ ░ ░ ░▒ ▒ ░ ░ ░▒ ░ ░ ░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░     ░   ░▒  ░    ░     ░ ░  ░    ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░   ░    ░ ░    ░     ░  ░          ", ZombieDice.colors.reset)
    sleep(0.5)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.red}Iniciando mais uma rodada do turno atual.")
    print(f"{ZombieDice.colors.red}▒▓███▀▒░▓▒▓███▀▒░▓▒▓█░▒▀▒░▓▒▓█▒█▀▒░▓▀▒█▒░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}▒ ▒ ░ ░ ░▒▒▒ ░ ░ ░▒ ▒ ░ ░ ░▒ ░ ░ ░▒ ░ ░ ░", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░     ░   ░▒  ░    ░     ░ ░  ░    ░    ", ZombieDice.colors.reset)
    print(f"{ZombieDice.colors.red}░ ░        ░        ░             ", ZombieDice.colors.reset)
    sleep(1)
	
  
def spinningBar(t=5):
  for i in range(t):
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.reset}{ZombieDice.colors.blue}({ZombieDice.colors.reset} | {ZombieDice.colors.blue}){ZombieDice.colors.reset}")
    sleep(0.1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.blue}({ZombieDice.colors.reset} / {ZombieDice.colors.blue}){ZombieDice.colors.reset}")
    sleep(0.1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.blue}({ZombieDice.colors.reset} ―― {ZombieDice.colors.blue}){ZombieDice.colors.reset}")
    sleep(0.1)
    ZombieDice.clearScreen()
    print(f"{ZombieDice.colors.blue}({ZombieDice.colors.reset} \\ {ZombieDice.colors.blue}){ZombieDice.colors.reset}")
    sleep(0.1)

def loadingBar(n=10, t=1):
    """_A loading Bar animation_
    
    Args:
       n (_int_): set's the number of times to load if none is given. Default is 10.
       t (_float_): set's the speed of the animation if none is given. Default is 1.
    """
    contador = 0
    for i in range(n):
        contador += 1
        bar = "█" * contador
        print(f"{ZombieDice.colors.red}{bar}")
        print(f"{int(contador/n*100)}%", ZombieDice.colors.reset)
        sleep(t)
        ZombieDice.clearScreen()
    

