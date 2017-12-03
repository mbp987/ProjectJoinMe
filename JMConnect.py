import pymysql
import sys
from start import Start

class JMConnect:
    
    def __init__(self):
        
        self.conn = pymysql.connect("localhost", "rooot", "mbp987", "joinme", charset='utf8')
        self.cursor = self.conn.cursor()
        try:
            self.start()
        except:
            print('Something went wrong... Sorry...')
            
JMConnect()
        
