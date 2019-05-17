from __future__ import print_function
import random
import time

allowed_notifications = [0, 1, 2, 3]

general_not = [['email', 'I am email'], 
['messenger', 'dad', 'I am your father.'], 
['instagram', 'I am instagram'], ['snapchat', 'I am snapchat'], 
['messenger', 'mom', 'I am not your father.'], 
['messenger', 'sister', 'I do not exist']]

#mess_list = []

def create_allowed_list():
    '''
    creates list of allowed apps to message person
    '''
    #allowed_notifications = [0, 1, 2, 3]
    for index in range(0, 4):
        print ('What would like like to allow? You have', str(4-index), 'to add')
        notification = raw_input('What application would you like to allow? ')
        if notification.lower() == 'messenger':
            who = raw_input('Messages from who? ')
            messenger_list = []
            messenger_list = [notification, who]
            notification = messenger_list
            
            #notification += ' : '
            #notification += who
        allowed_notifications[index] = notification
    


def check_if_allowed(allowed_list, general_list):
    '''
    allows specified messages to print to screen
    if sending a message though messenger list is given as ['messenger', 'from who', 'message']
    all other messages are given as ['app', 'message']
    '''
    mess_list = []
    for index in range(0,4):
        if type(allowed_list[index]) == list:
            mess_list += allowed_list[index]
            #print (mess_list)
    #allowed_list = allowed_notifications
    '''if 'email' in allowed_list:
        print ('HI, I am email.')
    if 'instagram' in allowed_list:
        print ('HI I am Instagram')
    if ''
    '''
    '''for app in general_list:
        if app == 'messenger':
            if 'messenger' in allowed_list:
                
        elif app in allowed_list:
            print ('HI I am ', app)'''
    if 'messenger' in mess_list:
        if general_list[1] in mess_list:
            print (general_list[1], ':', general_list[2])
        else:
            if general_list[0] in allowed_list:
                print (general_list[0], ':', general_list[1])
            else:
                print ('passed', ':', general_list[0])
    else:
        if general_list[0] in allowed_list:
            print (general_list[0], ':', general_list[1])
        else:
                print ('passed', ':', general_list[0])
            
def push_notification():
    var = random.choice(range(0,len(general_not)))
    notifi_list = general_not[var]
    check_if_allowed(allowed_notifications, notifi_list)
    
    
create_allowed_list()


count = 10

print ('Here are the notifications')

while count >= 0:
    push_notification()
    time.sleep(0.75)
    count -= 1