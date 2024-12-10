import pygame
from dealer import Dealer
from player import Player


class Controller:
  
  def __init__(self):
    pygame.init()
    pygame.event.pump
    self.screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Blackjack')
    
  def mainloop(self):
    game_over = False
    Dealer1 = Dealer()
    Player1 = Player()
    hbutton = pygame.Rect(100, 500, 200, 50)
    sbutton = pygame.Rect(500, 500, 200, 50)
    
    while game_over == False:
      green = (0,255,0)
      (self.screen).fill(green)
      font = pygame.font.SysFont('Arial', 30)
      white = (255,255,255)
      red = (255,0,0)
      playercards = "Player: " + "".join(Player1.hand())
      dealercards = "Dealer: " + "".join(Dealer1.hand1()) + " ?"
      playerscore = "Player score: " + str(Player1.score())
      dealerscore = "Player score: " + str(Dealer1.score())
      playercardstext = font.render(playercards, True, (255,255,255))
      playerscoretext = font.render(playerscore, True, (255,255,255))
      dealercardstext = font.render(dealercards, True, (255,255,255))
      dealerscoretext = font.render(dealerscore, True, (255,255,255))
      self.screen.blit(playercardstext, (50, 100))
      self.screen.blit(playerscoretext, (50, 150))
      self.screen.blit(dealercardstext, (50, 200))
      self.screen.blit(dealerscoretext, (50, 250))
      pygame.draw.rect(self.screen, red, hbutton)
      pygame.draw.rect(self.screen, red, sbutton)
      hittext = font.render("Hit", True, (255,255,255))
      self.screen.blit(hittext, (hbutton.x + 75, hbutton.y + 10))
      standtext = font.render("Stand", True, (255,255,255))
      self.screen.blit(standtext, (sbutton.x + 75, sbutton.y + 10))
      
      for event in pygame.event.get():
        if event.type == pygame.quit:
          game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
                if hbutton.collidepoint(event.pos):
                    Player1.hit()
                    if Player1.score > 21:
                        game_over = True
                if sbutton.collidepoint(event.pos):
                    if Dealer1.score < 17:
                        Dealer1.hit()
                    game_over = True
                    
      if game_over == True:
        dealercardstext = "Dealer: " + ", ".join(Dealer1.hand)
        dealerscoretext = f"Dealer Score: {Dealer1.score}"
        dealer_label = font.render(dealercardstext, True, (255,255,255))
        dealer_score_label = font.render(dealerscoretext, True, (255,255,255))
        self.screen.blit(dealer_label, (50, 200))
        self.screen.blit(dealer_score_label, (50, 250))
        result_text = ""
        if Player1.score > 21:
            result_text = "Player Bust! Dealer Wins!"
        elif Dealer1.score > 21:
            result_text = "Dealer Bust! Player Wins!"
        elif Player1.score > Dealer1.score:
            result_text = "Player Wins!"
        elif Player1.score < Dealer1.score:
            result_text = "Dealer Wins!"
        else:
            result_text = "It's a Tie!"

        result_label = font.render(result_text, True, (255,255,255))
        self.screen.blit(result_label, (800 // 2 - result_label.get_width() // 2, 600 // 2))
        pygame.time.wait(5000)
        pygame.display.update()
        
    
    
      
    
  
  ### below are some sample loop states ###

   #def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  #def gameloop(self):
      #event loop

      #update data

      #redraw
    
  #def gameoverloop(self):
      #event loop

      #update data

      #redraw
