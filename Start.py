import pymysql
import sys
from Member import Member
#from .admin import Admin

class Start:
    def __init__(self):
        print('Welcome in JoinMe!')
        choice = input('Who are you?\n(M) - Member\n(V) - Visitor\n(A) - Admin\n(Q) - Quit\n').upper()
        if(choice == 'M'):
            self.member()
        elif(choice == 'V'):
            self.visitor()
        elif(choice == 'A'):    
            self.admin()
        elif(choice == 'Q'):    
            print('See you soon. Bye!')
        elif(choice != 'M' or 'V' or 'A' or 'Q'):
            print()
            print('Please try to choose again...')
            i = 0
            while(i < 2):
                i += 1
                choice = input('Who are you?\n(M) - Member\n(V) - Visitor\n(A) - Admin\n(Q) - Quit\n').upper()
            else:
                print('same errory')
        else:
            print('Something went wrongmmmmm...')
            
            
start = Start()
