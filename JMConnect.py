import pymysql
import sys

class JMConnect:
    
    def __init__(self):
        self.getConn()
    def getConn(self):
        try:
            self.conn = pymysql.connect("localhost", "root", "mbp987", "joinme", charset='utf8')
            self.cursor = self.conn.cursor() 
            #self.err=false
        except:
            #self.err ='Something went wrong... Sorry...'
            print(self.err)             
        return self.conn, self.cursor