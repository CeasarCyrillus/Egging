import pygame
class Egg:
	def __init__(self, placement):
		self.placement = placement
		self.color = (255, 0, 0)
		self.type = "Egg"
	def draw(self):
		pl = self.placement
		pygame.draw.ellipse(screen, self.color, pl, 1)
		pygame.draw.ellipse(screen, (0, 255, 0), [pl[0], (pl[1]+pl[0]/2)-pl[3]/5, pl[2], pl[3]/5], 1)
		pygame.draw.ellipse(screen, (0, 255, 0), [pl[0], (pl[1]+pl[0]/2), pl[2], pl[3]/5], 1)
		pygame.draw.ellipse(screen, (0, 255, 0), [pl[0], (pl[1]+pl[0]/2), pl[2], pl[3]/5], 1)

class Hare:
	def __init__(self, pos):
		self.pos = pos
		self.color = (255, 255, 255)
		self.type = "Hare"
	def draw(self):
		x = self.pos[0]
		y = self.pos[1]
		p1 = [x-50, y]
		p2 = [x-50, y-80]
		p3 = [x, y-50]

		p4 = [x+50, y-80]
		p5 = [x+50, y]
		pygame.draw.lines(screen, self.color, False, [p1, p2, p3, p4, p5])
		pygame.draw.circle(screen, self.color, self.pos, 50, 1)

pygame.init()
screen = pygame.display.set_mode((400, 300))
exit = False
obj = Hare([100, 100])
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
        	if obj.type == "Hare":
        		obj = Egg([100, 100, 80, 100])
        	elif obj.type == "Egg":
        		obj = Hare([100, 100])
    obj.draw()
    pygame.display.flip()
    screen.fill((0, 0, 0))