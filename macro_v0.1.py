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

def nsleep(sec):
     st_sec = t.time()
     while t.time() - st_sec <sec:
        if is_exe == False:
            return False
        
        t.sleep(0.1)

def hold(key_name, sec):
        pyinput.keyDown(key_name)
        nsleep(sec)
        pyinput.keyUp(key_name)

def exe_macro():
        print(f"\rrunning...", end="")
        hold("w", 4)
        if is_exe == False:
             return False
        hold("a", 1)
        if is_exe == False:
            return False
        hold("w", 1)
        if is_exe == False:
            return False
        pyinput.press("ctrl")
        nsleep(10)
        if is_exe == False:
            return False
        pyinput.press("m")
        nsleep(0.7)
        if is_exe == False:
            return False
        pyinput.press("s")
        nsleep(0.7)
        if is_exe == False:
            return False
        pyinput.press("e")
        nsleep(0.7)
        if is_exe == False:
            return False
        pyinput.press("e")
        nsleep(10)
        if is_exe == False:
            return False 
        
try:
    while True:
        if is_exe:
             exe_macro() 

        else:
            print(f"\rwaiting...", end="")
            t.sleep(0.1)

except KeyboardInterrupt:
    None
