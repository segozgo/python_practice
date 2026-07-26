import time as t
import keyboard as key
import pydirectinput as pyinput

is_exe = False

def toggle():
        global is_exe

        if is_exe == True:
            is_exe = False

        else:
            is_exe = True


key.add_hotkey("f10", toggle)

def hold(key_name, sec):
    st_sec = t.time()
    while t.time() - st_sec < sec:
        pyinput.keyDown(key_name)
        if is_exe == False:
            break

    pyinput.keyUp(key_name)


try:
    while True:
        if is_exe == True:
            print(f"\rrunning...", end="")
            hold("w", 4)
            hold("a", 1)
            hold("w", 1)
            pyinput.press("ctrl")
            t.sleep(10)
            if is_exe == False:
                continue
            pyinput.press("m")
            t.sleep(0.7)
            if is_exe == False:
                continue
            pyinput.press("s")
            t.sleep(0.7)
            if is_exe == False:
                continue
            pyinput.press("e")
            t.sleep(0.7)
            if is_exe == False:
                continue
            pyinput.press("e")
            t.sleep(10)    

        else:
            print(f"\rwaiting...", end="")
            t.sleep(0.1)

except KeyboardInterrupt:
    None