import pymysql
import sys
from JMConnect import *
from Visitor import *
from Member import *
from Admin import *


class Start:
    def __init__(self):
        jm = JMConnect()
        self.conn = jm.getConn()[0]
        self.cursor = jm.getConn()[1]
        print('Welcome to JoinMe!')
        choice = input('Who are you?\n(M) - Member\n(V) - Visitor\n(A) - Admin\n(Q) - Quit\n').upper()
        if(choice == 'M'):
            m = Member(self.conn, self.cursor)
        elif(choice == 'V'):
            v = Visitor(self.conn, self.cursor)
        elif(choice == 'A'):    
            a = Admin(self.conn, self.cursor)
        elif(choice == 'Q'):    
            print('See you soon. Bye!')
        elif(choice != 'M' and 'V' and 'A' and 'Q'):
            print()
            i = 3
            while(i >= 1 ):
                print('Please try to choose again...')
                print('No. of probes: '+str(i))
                i -= 1
                choice = input('Who are you?\n(M) - Member\n(V) - Visitor\n(A) - Admin\n(Q) - Quit\n').upper()
            else:
                print('Something went wrong...')
            
s = Start()



