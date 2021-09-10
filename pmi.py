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
a = []
b = []
line_no = 0  # temp index for assigning key-value pairs to lists

for config in configs:
    
    line_no += 1

    if config[0] == '#' or config == '\n':
        continue
    
    kv_pair = config[:-1].split('=')
    
    if 7 <= line_no <= 7:
        option.append(kv_pair)
    elif 15 <= line_no <= 33:
        pmi.append(kv_pair)
    elif 43 <= line_no <= 81:
        sched.append(kv_pair)
    elif 86 <= line_no <= 104:
        a.append(config[:-1])
    elif 106 <= 125:
        b.append(config[:-1])

    
# QoL functions
def get_val(Nx2_2d_list, key):
    for kv_pair in Nx2_2d_list:
        if kv_pair[0] == key:
            return kv_pair[1]
    return

def join_zoom(subject: str):
    if subject == 'refle':
        print('\nPlease choose the subject manually, this window will close in 30 seconds.')
        print('RE: https://zoom.us/j/4287727803')
        print('FLE: https://zoom.us/j/5168805269')
        time.sleep(30)
    elif subject == 'ee':
        print('\nPlease choose the teacher manually, this window will close in 30 seconds.')
        print('EE Lesson:')
        print('YPWP: https://zoom.us/j/7578549019')
        print('LGW: https://zoom.us/j/3651136599')
        time.sleep(30)
    else:
        halt = input(f'\nJoining {subject} lesson, confirm? (Press ENTER to continue, close this window if not.)')
        url = f'https://zoom.us/j/{get_val(pmi, subject)}'
        web.open(url)
        time.sleep(int(get_val(option, 'wait')))  # wait for browser to load page
        gui.press('left')
        gui.press('enter')


# Script
def main():
    
    while True:
        
        week_num = dt.strftime('%y') + dt.strftime('%U')
        
        if week_num in a:
            week = 'A'
            print('Week A')
        elif week_num in b:
            week = 'B'
            print('Week B')
        else:
            week = input('Week A or B? ').upper()
        
        if week not in ('A', 'B'):  # Week validation
            print('Invalid week, try again.\n')
            continue
        day = dt.strftime('%w')  # Day of week
        hhmm = int(dt.strftime('%H') + dt.strftime('%M'))  # Time in str(HHMM)
        
        if day in ('0', '6') or not 1530 <= hhmm <= 1745:  # Exit if weekend or no Zoom lesson coming up
            print('No upcoming lesson.')
            break
        
        if 1530 <= hhmm < 1620:  # Get lesson number
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
