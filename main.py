import pygame
from colors import Colors

def main() -> None:
	pygame.init()
	WIDTH = 800
	HEIGHT = 800
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
	CIRCLE_RADIUS = 150
	BALL_RADIUS = 5
	ball_pos = [WIDTH/2, HEIGHT/2 - 120]
	ball_vel = [0.0, 0.0]
	GRAVITY = 0.2
	
	running = True
	
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				
		ball_vel[1] += GRAVITY
		ball_pos[0] += ball_vel[0]
		ball_pos[1] += ball_vel[1]
		
		window.fill(Colors.BLACK.value)
		pygame.draw.circle(window, Colors.WHITE.value, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
		pygame.draw.circle(window, Colors.MAGENTA.value, ball_pos, BALL_RADIUS)
		
		pygame.display.flip()
		clock.tick(60)
	
	pygame.quit()
	
if __name__ == '__main__':
	main()
	
