import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Malawian Tetris")

# Define colors based on the Malawian flag
black = (0, 0, 0)
red = (206, 17, 38)
green = (0, 102, 0)
white = (255, 255, 255)

# Define Malawian rivers' names for levels
rivers = [
    "Shire",
    "Lilongwe",
    "Ruo",
    "Bua",
    "Dwangwa",
    "Linthipe",
    # ... Add more river names for the remaining levels
]

# Tetris block class
class Block:
    def __init__(self, color):
        self.color = color
        self.shape = random.choice(["I", "J", "L", "O", "S", "T", "Z"])
        self.rotation = 0
        self.x = width // 2
        self.y = 0

# Function to draw the Tetris board
def draw_board():
    screen.fill(black)

# Function to draw a block
def draw_block(block):
    shape_template = SHAPES[block.shape][block.rotation]
    for i in range(len(shape_template)):
        for j in range(len(shape_template[i])):
            if shape_template[i][j] == "1":
                pygame.draw.rect(screen, block.color, (block.x + j * 30, block.y + i * 30, 30, 30))

# Define Tetris block shapes and rotations
SHAPES = {
    "I": ["0100", "0100", "0100", "0100"],
    "J": ["100", "111"],
    "L": ["001", "111"],
    "O": ["11", "11"],
    "S": ["011", "110"],
    "T": ["010", "111"],
    "Z": ["110", "011"],
}

# Main game loop
def main():
    clock = pygame.time.Clock()
    block = Block(green)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        handle_input(keys, block)

        update_game_logic(block)

        draw_board()
        draw_block(block)

        pygame.display.flip()
        clock.tick(10)  # Adjust the frame rate as needed

    pygame.quit()

# Function to handle user input for block movement and rotation
def handle_input(keys, block):
    if keys[pygame.K_LEFT] and not check_collision(block, -1, 0):
        block.x -= 30
    if keys[pygame.K_RIGHT] and not check_collision(block, 1, 0):
        block.x += 30
    if keys[pygame.K_DOWN] and not check_collision(block, 0, 1):
        block.y += 30
    if keys[pygame.K_UP]:
        rotate_block(block)

# Function to check collision with the borders and other blocks
def check_collision(block, offset_x, offset_y):
    shape_template = SHAPES[block.shape][block.rotation]
    for i in range(len(shape_template)):
        for j in range(len(shape_template[i])):
            if shape_template[i][j] == "1":
                x_pos = block.x + j * 30 + offset_x * 30
                y_pos = block.y + i * 30 + offset_y * 30
                if (
                    x_pos < 0
                    or x_pos >= width
                    or y_pos >= height
                    or (x_pos, y_pos) in get_occupied_positions()
                ):
                    return True
    return False

# Function to get the positions of all occupied blocks on the board
def get_occupied_positions():
    occupied_positions = []
    # Implement logic to get positions of occupied blocks
    return occupied_positions

# Function to update game logic (e.g., handle block placement, line clearing)
def update_game_logic(block):
    if not check_collision(block, 0, 1):
        block.y += 30
    else:
        # Block has landed, update occupied positions and check for line clearing
        update_occupied_positions(block)
        clear_lines()
        # Spawn a new block
        block = Block(green)

# Function to update the positions of occupied blocks on the board
def update_occupied_positions(block):
    # Implement logic to update occupied positions
    pass

# Function to clear completed lines
def clear_lines():
    # Implement logic to clear completed lines
    pass

# Function to rotate the current block
def rotate_block(block):
    rotated_shape = SHAPES[block.shape][(block.rotation + 1) % len(SHAPES[block.shape])]
    if not check_collision(block, 0, 0, rotated_shape):
        block.rotation = (block.rotation + 1) % len(SHAPES[block.shape])

if __name__ == "__main__":
    main()
