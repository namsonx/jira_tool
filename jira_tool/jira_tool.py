'''
Created on Dec 9, 2016

@author: Linh-PC
'''

from connected_jira import con_jira

def main():
    username = raw_input('Enter your username: ')
    password = raw_input('Enter your password: ')
    connected = con_jira(username, password)
    raw_input('Press Enter to exit')

if __name__ == '__main__':
    main()
    pass