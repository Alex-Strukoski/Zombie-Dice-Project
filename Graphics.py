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

    sonic = """
                                                                         KKKKKKKKKKKKKKKKKKKKKKKKKKK
                                                                    KKKKK                           KKKKK 
                                                                KKKK          KKKKKKKKKK                  KKK 
                                                   KKKKKKKK  KKK            KK  KKKKKK K               KKKKKK 
                                                  K        KKK        KKKKKKK KKK    K KK          KKKK 
                                                  KK     KK         KK      KK   KKK K KK       KKK 
                                                   K    KK        KK KKKKKKKKK     KKK K      KK 
                                                   KKKKK         K KK         K        K     KKKK 
                                                    K   K         K            K       K         KKK 
                                                   KKKKK         KK     KK     KK                   KKK 
                                                   KKK KK       KK      KKK     K       KK             KK 
                                                    K   KK      K      KKKK     K        K               KK 
                                                    K    KK    K       KKKKK   KK        KK               KK 
                                                    K    KKKKKK         KKKK   K         KK                KK 
                                                     K   KKK            KKK   KK  K      KK    KKKK         KK 
                                                   KKKKKKKKK                 KKKK  KK    K          KK       KK 
                                                   KKKKKKKK  KKKK       KKKKK KK    KK   K  KKK        KK    KK 
                                                      KKKKK       KKKKK        KKK  K   KK   KK          KK  KK 
                                                        KK                   KKKKK KK  KK      KK          kkkk 
                                                          KK          KKKKKKK     KK  KK        KK           kk 
                                                            KKK                 KK KKK           K 
                                                            KKKKKKKKK KKK KKKKKKKKKKKK           KK 
                                                         KKK     KKKK  KKKKKK  KK    KK           K 
                                                       KKK  KK KKKK  KK        KKK  KK  KKKK      K 
                                                      K KKK K    KK K             KKKK      KKK  KK 
                                                      K KKKKKKK    KKK    KK KK K  KK KK       KKK 
                                                      KKKK    KKKK   KKKK  K  K  K KK  KK       KK 
                                                    KKK  KK        KK KK   K  K  KKK    K 
                                                    KK KKKKK          KK   K KKKK       K 
                                                            KK          KKK K KKKKKKKKK KK 
                                                             KKKK    KKK      K        KKK 
                                                               KK KK       KK  KK 
                                                                K   K KK   K KKKKKK 
                                                                K   K  KK  K 
                                                                K   K   K  KK 
                                                          KKKK  K   KKKKKK  KKK 
                                                          K   KKKKKKKKKKKK   K KKKK 
                                                           KK      KK    K KKKK   KK 
                                                          K        K              K 
                                                        KKKK        KK           KKKK 
                                                     KKKKK  KKKKKKKKK K             KK 
                                                  KKK     KK  KK    KK             KK 
                                                KKK        K   K     KKKKKKKKKKKKKKKKK 
                                               KK           K  K    KK    KKK       KKK 
                                             KK             K  KK   KK   KK  KKKKKKKK K 
                                            KK              K  KKKKKKK  KK  KK      KKKK 
                                            KKKKKKKKKKKKKKKKKKKKK    KK K  K          KK 
                                                                      KKK KK           K 
                                                                        KKK           KK 
                                                                          KKK         K 
                                                                             KKK     KK         
                                                                                 KKKKK
     /KK     /KK                                                                                  /KK     /KK             /KK     /KK          
    |  KK   /KK/                                                                                 | KK    |__/            | KK    |__/          
     \  KK /KK//KKKKKK  /KK   /KK        /KKKKKK   /KKKKKK   /KKKKKK         /KKKKKK  /KK   /KK /KKKKKK   /KK  /KKKKKKK /KKKKKK   /KK  /KKKKKKK
      \  KKKK//KK__  KK| KK  | KK       |____  KK /KK__  KK /KK__  KK       |____  KK| KK  | KK|_  KK_/  | KK /KK_____/|_  KK_/  | KK /KK_____/
       \  KK/| KK  \ KK| KK  | KK        /KKKKKKK| KK  \__/| KKKKKKKK        /KKKKKKK| KK  | KK  | KK    | KK|  KKKKKK   | KK    | KK| KK      
        | KK | KK  | KK| KK  | KK       /KK__  KK| KK      | KK_____/       /KK__  KK| KK  | KK  | KK /KK| KK \____  KK  | KK /KK| KK| KK      
        | KK |  KKKKKK/|  KKKKKK/      |  KKKKKKK| KK      |  KKKKKKK      |  KKKKKKK|  KKKKKK/  |  KKKK/| KK /KKKKKKK/  |  KKKK/| KK|  KKKKKKK
        |__/  \______/  \______/        \_______/|__/       \_______/       \_______/ \______/    \___/  |__/|_______/    \___/  |__/\_______/
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

def limit(t=0):
  ZombieDice.clearScreen()
  print(f"{ZombieDice.colors.red}L")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LI")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIM")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMI")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMIT")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE D")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE T")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TE")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TEN")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENT")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTA")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTAT")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATI")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIV")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVA")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS ")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS E")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EX")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXC")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXCE")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXCED")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXCEDI")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXCEDID")
  sleep(t)
  ZombieDice.clearScreen()
  print(f"LIMITE DE TENTATIVAS EXCEDIDO", ZombieDice.colors.reset)
  sleep(t)
  ZombieDice.clearScreen()
  for pulse in range(5):
    print(f"LIMITE DE TENTATIVAS EXCEDIDO", ZombieDice.colors.red)
    sleep(1)
    ZombieDice.clearScreen()
    print(f"LIMITE DE TENTATIVAS EXCEDIDO", ZombieDice.colors.reset)
    sleep(1)
    ZombieDice.clearScreen()
  print(f"{ZombieDice.colors.red}LIMITE DE TENTATIVAS EXCEDIDO", ZombieDice.colors.reset)
  
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


    

