import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Obstacle Avoidance Simulator")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for frame rate control
clock = pygame.time.Clock()

# Robot properties
robot_radius = 20
robot_x, robot_y = WIDTH // 4, HEIGHT // 2
robot_speed = 5
robot_direction = [1, 0]  # Initial direction (x, y)

# Obstacle properties
obstacle_width, obstacle_height = 50, 50
num_obstacles = 5
obstacles = [
    pygame.Rect(
        random.randint(200, WIDTH - 100), random.randint(50, HEIGHT - 50), obstacle_width, obstacle_height
    )
    for _ in range(num_obstacles)
]

# Function to detect collisions
def detect_collision(robot_x, robot_y, obstacles):
    for obstacle in obstacles:
        if obstacle.collidepoint(robot_x, robot_y):
            return True
    return False

# Main simulation loop
def run_simulation():
    global robot_x, robot_y, robot_direction
    running = True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Draw the robot and obstacles
        pygame.draw.circle(screen, BLUE, (robot_x, robot_y), robot_radius)
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)

        # Update robot position
        new_x = robot_x + robot_speed * robot_direction[0]
        new_y = robot_y + robot_speed * robot_direction[1]

        # Handle collisions
        if detect_collision(new_x, new_y, obstacles) or not (0 < new_x < WIDTH and 0 < new_y < HEIGHT):
            robot_direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        else:
            robot_x, robot_y = new_x, new_y

        # Update the display
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Run the simulation
run_simulation()
