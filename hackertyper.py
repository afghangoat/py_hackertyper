import pyperclip
import os
import time
import random
import pyautogui
from pyautogui import typewrite,hotkey
pyautogui.FAILSAFE = False

if __name__ == "__main__":
    stonks_mode=False
    time.sleep(10) #For start, wait some
    
    global_delay=0
    
    file_name="sandsim/main_demoduled.cpp"
    how_much_fragment=2 #How much to split lines

    #print(random.randint(3, 9)) #both included
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if len(line)<10:

                if stonks_mode==True:
                    typewrite(line+"\n")
                    if global_delay!=0:
                        time.sleep(global_delay)
                else:
                    pyperclip.copy(line+"\n")
                    if global_delay!=0:
                        time.sleep(global_delay)
                    hotkey('ctrl', 'v')
            else:

                if how_much_fragment==2:
                    idx1=random.randint(1, len(line)-2)
                    
                    if stonks_mode==True:
                        typewrite(line[0:idx1])
                        if global_delay!=0:
                            time.sleep(global_delay)
                    
                        typewrite(line[idx1:len(line)-1]+"\n")
                        if global_delay!=0:
                            time.sleep(global_delay)
                    else:
                        pyperclip.copy(line[0:idx1])
                        if global_delay!=0:
                            time.sleep(global_delay)
                        hotkey('ctrl', 'v')
                    
                        pyperclip.copy(line[idx1:len(line)-1]+"\n")
                        if global_delay!=0:
                            time.sleep(global_delay)
                        hotkey('ctrl', 'v')
                    
                else:
                    if stonks_mode==True:
                        typewrite(line+"\n")
                        if global_delay!=0:
                            time.sleep(global_delay)
                    else:
                        pyperclip.copy(line+"\n")
                        if global_delay!=0:
                            time.sleep(global_delay)
                        hotkey('ctrl', 'v')
                