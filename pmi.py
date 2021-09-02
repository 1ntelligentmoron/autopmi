# Import required libraries
import webbrowser as web
import pyautogui as gui
import time
from datetime import datetime
dt = datetime.now()


# Read config.txt
with open('config.txt', 'r') as file:
    configs = file.readlines()

option = []
pmi = []
sched = []
line_no = 0  # temp index for assigning key-value pairs to lists

for config in configs:
    
    line_no += 1

    if config[0] == '#' or config == '\n':
        continue
    
    kv_pair = config[:-1].split('=')
    
    if 7 <= line_no <= 7:
        option.append(kv_pair)
    elif 15 <= line_no <= 34:
        pmi.append(kv_pair)
    elif 45 <= line_no <= 83:
        sched.append(kv_pair)

    
# QoL functions
def get_val(Nx2_2d_list, key):
    for kv_pair in Nx2_2d_list:
        if kv_pair[0] == key:
            return kv_pair[1]
    return

def join_zoom(subject: str):
    url = f'https://zoom.us/j/{get_val(pmi, subject)}'
    web.open(url)
    time.sleep(int(get_val(option, 'wait')))  # wait for browser to load page
    gui.press('left')
    gui.press('enter')


# Script
def main():
    
    while True:
        
        week = input('Week A or B? ').upper()  # Week ident
        if week not in ('A', 'B'):  # Week validation
            print('Invalid week, try again.\n')
            continue
        day = dt.strftime('%w')  # Day of week
        hhmm = int(dt.strftime('%H') + dt.strftime('%M'))  # Time in str(HHMM)
        
        if day in ('0', '6') or not 1540 <= hhmm <= 1745:  # Exit if weekend or no Zoom lesson coming up
            print('No upcoming lesson.')
            break
        
        if 1540 <= hhmm < 1620:  # Get lesson number
            lesson_no = '8'
        elif 1620 <= hhmm < 1655:
            lesson_no = '9'
        else:
            lesson_no = '10'
            
        lesson_ident = f'{week}{day}_lesson_{lesson_no}'  # Construct key for 'sched'
        upcoming_subj = get_val(sched, lesson_ident)  # Get subject name
        join_zoom(upcoming_subj)  # Join Zoom
        break
    
    
if __name__ == "__main__":
    main()
