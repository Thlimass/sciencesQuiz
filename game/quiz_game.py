# import pygame
# from pygame.locals import QUIT
#
# pygame.init()
#
# class QuizGame:
#     def __init__(self):
#         self.screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption("Quiz Ciências")
#         self.clock = pygame.time.Clock()
#
#     def run(self):
#         running = True
#         while running:
#             for event in pygame.event.get():
#                 if event.type == QUIT:
#                     running = False
#
#             self.screen.fill((255, 255, 255))
#             pygame.display.flip()
#             self.clock.tick(60)
#
#         pygame.quit()
#
# if __name__ == "__main__":
#     game = QuizGame()
#     game.run()