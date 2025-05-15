import pygame
pygame.init()
width,height=1200,600
yellow=(255,255,0)
red=(255,0,0)
green=(255,255,0)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("brateinberg vechile")
clock=pygame.time.Clock()
fps=60
pygame.font.init()
font=pygame.font.SysFont("Arial",20)
class sun:
    def __init__(self,position,radius=50,color=yellow):
        self.position=pygame.math.Vector2(position)
        self.radius=radius
        self.color=color
   # def move(self):
    #    self.position.x=self.position.x + 1
     #   self.position.y=self.position.y + 1
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.position,self.radius)
sun=sun((600,300))

class vechile:
    def __init__(self,position,direction,radius=50,color=red):
        self.position=pygame.math.Vector2(position)
        self.direction=direction
        self.radius=radius
        self.color=color
        self.speeding_scaling=50

        self.sensor_radius=15
        self.sensor_offset=self.radius+self.sensor_radius
        self.sensor_position=self.position+pygame.math.Vector2(0,-self.sensor_offset).rotate(self.direction)
        self.sensor_color=green

    def draw(self,surface):
        pygame.draw.circle(surface,self.color,self.position,self.radius)
        
        pygame.draw.circle(surface,self.sensor_offset,self.sensor_position,self.sensor_radius)

    def calculate_distance_to_sun(self,sun_position):
        return self.sensor_position.distance_to(sun_position)
             

    def move(self,sun_position):
        direction=pygame.math.Vector2(0,-1).rotate(self.direction)
        distance=self.calculate_distance_to_sun(sun_position)
        speed=self.speeding_scaling*(1/distance)
        text=f"distance to sun:{distance}\nspeed to sun:{speed}"
        text_surface=font.render(text,True,(255,255,255))
        screen.blit(text_surface,(10,10))
        self.position +=direction*speed
        self.sensor_position=self.position+pygame.math.Vector2(0,-self.sensor_offset).rotate(self.direction)

vechile=vechile((300,500),45)


running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0))
   # circle.move()
    sun.draw(screen)
    vechile.move(sun.position)
    vechile.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()