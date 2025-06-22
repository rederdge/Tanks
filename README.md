# Tanks Game

A simple tank game built with Python and Pygame.

## How to Run

1. Install Python 3 and Pygame:
   ```
   pip install pygame
   ```

2. Make sure the following files are in the same folder:
   - `main.py`
   - `ptank.png` — player tank image
   - `etank.png` — enemy tank image
   - `bullet.png` — bullet image
   - `back.png` — background image

3. Run the game:
   ```
   python main.py
   ```

## Controls

- Arrow keys — move the player tank
- A / D — rotate the player tank's turret
- Space — shoot

## Game Objective

- Destroy the enemy tank while avoiding its shots.
- The game ends if either the player or the enemy is destroyed.

## Features

- The enemy shoots at the player and rotates its turret towards the shot.
- Both tanks have health bars.
- The game uses a background image (`back.png`).

---

Made with Python and Pygame.