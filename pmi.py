import webbrowser
import pyautogui as gui
import time


# QoL functions
def get_val(Nx2_2d_list, key):
    for kv_pair in Nx2_2d_list:
        if kv_pair[0] == key:
            return kv_pair[1]


# Read config
with open('config.txt', 'r') as file:
    configs = file.readlines()

option = []
pmi = []
sched = []
line_no = 0

for config in configs:
    
    line_no += 1
    
    if config[0] == '#' or config == '\n':
        continue
    
    kv_pair = config[:-1].split('=')
    
    if 7 <= line_no <= 7:
        option.append(kv_pair)
    elif 15 <= line_no <= 34:
        pmi.append(kv_pair)
    elif 43 <= line_no <= 82:
        sched.append(kv_pair)
        
# print("option", option)
# print("pmi", pmi)
# print("sched", sched)


# Main
def join_zoom(subject):
    webbrowser.open('https://zoom.us/j/')
    time.sleep(3)
    gui.press('left')
    gui.press('enter')
