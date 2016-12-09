'''
Created on Dec 9, 2016

@author: Linh-PC
'''

from jira import JIRA

class con_jira(object):
    '''
    classdocs
    '''


    def __init__(self, username, password):
        '''
        Constructor
        '''
        self.username = username
        self.password = password
        print 'Username is: ', self.username
        print 'Password is: ', self.password
        