import pyautogui

print("Press ctrl-c to quit.")
try:
    previous_x = -1
    previous_y = -1
    while True:
        x, y = pyautogui.position()
        positionString = "x:" + str(x).rjust(4) + " y:" + str(y).rjust(4)

        # updates the output if the position changes.
        if previous_x != x or previous_y != y:
            print("\b" * len(positionString), end="", flush=True)
            print(positionString, end="")
            previous_x = x
            previous_y = y
except KeyboardInterrupt:
    print("\nProgram terminated.")
