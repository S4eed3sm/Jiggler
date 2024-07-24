import random
import time
from datetime import datetime

import numpy as np
import pyautogui
from screeninfo import get_monitors

m = get_monitors()[0]
print(m.x, m.y, m.width, m.height)

pyautogui.FAILSAFE = False

choices = ["esc", "1", "2", "3", "shift", "space", "\\"]


def human_like_pause():
    pause_duration = random.uniform(0.1, 0.5)
    time.sleep(pause_duration)


def get_bezier_curve_points(start_x, start_y, end_x, end_y, num_points=100):
    cp1_x = (
        start_x
        + (end_x - start_x) * random.uniform(0.1, 0.3)
        + random.uniform(-200, 200)
    )
    cp1_y = (
        start_y
        + (end_y - start_y) * random.uniform(0.1, 0.3)
        + random.uniform(-200, 200)
    )
    cp2_x = (
        start_x
        + (end_x - start_x) * random.uniform(0.3, 0.5)
        + random.uniform(-200, 200)
    )
    cp2_y = (
        start_y
        + (end_y - start_y) * random.uniform(0.3, 0.5)
        + random.uniform(-200, 200)
    )
    cp3_x = (
        start_x
        + (end_x - start_x) * random.uniform(0.5, 0.7)
        + random.uniform(-200, 200)
    )
    cp3_y = (
        start_y
        + (end_y - start_y) * random.uniform(0.5, 0.7)
        + random.uniform(-200, 200)
    )
    cp4_x = (
        start_x
        + (end_x - start_x) * random.uniform(0.7, 0.9)
        + random.uniform(-200, 200)
    )
    cp4_y = (
        start_y
        + (end_y - start_y) * random.uniform(0.7, 0.9)
        + random.uniform(-200, 200)
    )

    t_values = np.linspace(0, 1, num_points)
    points = []
    for t in t_values:
        x = (
            (1 - t) ** 4 * start_x
            + 4 * (1 - t) ** 3 * t * cp1_x
            + 6 * (1 - t) ** 2 * t**2 * cp2_x
            + 4 * (1 - t) * t**3 * cp3_x
            + t**4 * end_x
        )
        y = (
            (1 - t) ** 4 * start_y
            + 4 * (1 - t) ** 3 * t * cp1_y
            + 6 * (1 - t) ** 2 * t**2 * cp2_y
            + 4 * (1 - t) * t**3 * cp3_y
            + t**4 * end_y
        )
        points.append((x, y))
    return points


def human_like_mouse_move(x, y):
    """Move the mouse to a target position with human-like movements."""
    start_x, start_y = pyautogui.position()
    points = get_bezier_curve_points(start_x, start_y, x, y)

    for point in points:
        pyautogui.moveTo(point[0], point[1], duration=0.001)
        time.sleep(random.uniform(0.01, 0.03))


last_pause_time = time.time()
next_pause_interval = random.randint(60, 300)

while True:
    for i in range(10):
        time.sleep(random.uniform(0.5, 2))

        x = random.randint(m.x, m.width - 1)
        y = random.randint(m.y, m.height - 1)
        print(f"Moving to ({x}, {y})")

        human_like_mouse_move(x, y)

        choice = random.choice(choices)
        pyautogui.press(choice)
        print("Movement made at {}".format(datetime.now().time()))

        human_like_pause()

        if time.time() - last_pause_time > next_pause_interval:
            pause_duration = random.randint(30, 60)
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            last_pause_time = time.time()
            next_pause_interval = random.randint(60, 300)

    cycle_pause = random.randint(0, 60)
    print(f"Pausing for {cycle_pause} seconds.")
    time.sleep(cycle_pause)
