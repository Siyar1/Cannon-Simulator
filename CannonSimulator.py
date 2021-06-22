import os, math, pygame
pygame.font.init()

## Window dimensions
width, height = 1280, 720
window = pygame.display.set_mode((width, height))

## Window name
pygame.display.set_caption("Cannon Simulator")

## Game framerate
FPS = 144

## Font for text
general_font = pygame.font.SysFont('Ariel', 40)

## Initial conditions and constants
x_initial = 85
y_initial = 615

## Creating the images
cannon_image = pygame.image.load(os.path.join('Assets', 'cannon.png'))
cannonbase_image = pygame.image.load(os.path.join('Assets', 'cannon_base.png'))
cannonball_image = pygame.image.load(os.path.join('Assets', 'cannonball.png'))
background_image = pygame.image.load(os.path.join('Assets', 'background.png'))
grass_image = pygame.image.load(os.path.join('Assets', 'grass_field.png'))
road_image = pygame.image.load(os.path.join('Assets', 'road.png'))

## Cannoball, cannon, and cannon base dimensions
cannon_width, cannon_height = 100, 100
cannonball_width, cannonball_height = 50, 50
cannonbase_width, cannonbase_height = 120, 120

## Scaling/rotating the images so that they fit
cannon_image = pygame.transform.scale(cannon_image, (cannon_width, cannon_height))
cannon_image = pygame.transform.rotate(cannon_image, -45)
cannonbase_image = pygame.transform.scale(cannonbase_image, (cannonbase_width, cannonbase_height))
cannonball_image = pygame.transform.scale(cannonball_image, (cannonball_width, cannonball_height))
grass_image = pygame.transform.scale(grass_image, (1280, 720))

## Function for what to display on the window
def display_window(cannonball, cannon_moving, initial_angle, initial_velocity, time):
    angle_text = general_font.render('The angle is: ' + str(initial_angle), 1, (0, 0, 0))
    initial_velocity_text = general_font.render('The initial velocity is: ' + str(initial_velocity), 1, (0, 0, 0))
    x_position_text = general_font.render('The X position is: ' + str(cannonball.x - x_initial), 1, (0, 0, 0))
    y_position_text = general_font.render('The Y position is: ' + str((y_initial - cannonball.y)), 1, (0, 0, 0))
    time_text = general_font.render('Time in seconds: ' + str(time), 1, (0, 0, 0))
    

    window.blit(background_image, (0, -200))
    window.blit(grass_image, (0, 500))
    window.blit(road_image, (0, 650))

    window.blit(cannonball_image, (cannonball.x, cannonball.y))

    window.blit(cannon_moving, (40, 570))
    window.blit(cannonbase_image, (50, 560))

    window.blit(angle_text, (50, 50))
    window.blit(x_position_text, (50, 100))
    window.blit(y_position_text, (50, 150))
    window.blit(initial_velocity_text, (50, 200))
    window.blit(time_text, (50, 250))

    pygame.display.update()

## Rotating image
def rotate_image(image, angle):
    initial_rect = image.get_rect()
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rectangle = initial_rect.copy()
    rotate_rectangle.center = rotate_image.get_rect().center
    rotate_image = rotate_image.subsurface(rotate_rectangle).copy()
    return rotate_image

## The game loop which is responsible for the refreshing of the page
def game_loop():
    initial_angle = 0
    initial_velocity = 0
    cannon_moving = cannon_image
    cannonball = pygame.Rect(85, 615, cannonball_width, cannonball_height)
    time = 0
    gravity = 9.81

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        total_time = (2*initial_velocity*math.sin(math.radians(initial_angle)))/gravity

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE] and time <= total_time:
            time += 1/35
            cannonball.x = x_initial + initial_velocity * math.cos(math.radians(initial_angle)) * time
            cannonball.y = y_initial - (initial_velocity * math.sin(math.radians(initial_angle)) * time - gravity/2 * time ** 2)

        if keys_pressed[pygame.K_a]:
            initial_angle += 1
            if initial_angle > 90:
                initial_angle = 90
            cannon_moving = rotate_image(cannon_image, initial_angle)
        
        if keys_pressed[pygame.K_d]:
            initial_angle -= 1
            if initial_angle < 0:
                initial_angle = 0
            cannon_moving = rotate_image(cannon_image, initial_angle)

        if keys_pressed[pygame.K_w]:
            initial_velocity += 1
            if initial_velocity > 105:
                initial_velocity = 105

        if keys_pressed[pygame.K_s]:
            initial_velocity -= 1
            if initial_velocity < 0:
                initial_velocity = 0
            

        display_window(cannonball, cannon_moving, initial_angle, initial_velocity, time)
    pygame.quit()

if __name__ == "__game_loop__":
    game_loop()

game_loop()