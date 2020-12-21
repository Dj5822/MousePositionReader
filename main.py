import pyautogui

print("Press ctrl-c to quit.")
try:
    previous_x = -1
    previous_y = -1
    while True:
        x, y = pyautogui.position()
        position_string = "x:" + str(x).rjust(4) + " y:" + str(y).rjust(4)

        # updates the output if the position changes.
        if previous_x != x or previous_y != y:
            pixel_color = pyautogui.screenshot().getpixel((x, y))
            position_string += " RGB: (" + str(pixel_color[0]).rjust(3) + ", " + \
                               str(pixel_color[1]).rjust(3) + ", " + str(pixel_color[2]).rjust(3) + ")"
            print("\b" * len(position_string), end="", flush=True)
            print(position_string, end="")
            previous_x = x
            previous_y = y
except KeyboardInterrupt:
    print("\nProgram terminated.")
