import pymysql
import sys

class Visitor():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
        print(100*'_'+100*' '+'\n'+'\nHere you may:   (R) - Register   (L) - Login   (W) - Write to us   (Q) - Quit')
        print(100*' ')
        print('Or just see the events:   (C) - Cinema   (T) - Theatre\n'+100*'_')
        
        choice = input().upper()
        
        if (choice == 'R'):
            self.register()
        elif (choice == 'L'):
            self.login()
        elif (choice == 'W'):
            self.write()
        elif (choice == 'Q'):
            self.quit()
        elif (choice == 'C'):
            rs = self.cursor.execute("SELECT * FROM Form_offer WHERE id_event = 'c'")
            results = cursor.fetchall()
            print(106*'-')
            print('| %12s | %10s | %20s | %10s | %15s | %20s |' % ('Date', 'Time', 'Movie', 'Payment', 'Looking for...', 'around the age...'))
            print('|'+104*'-'+'|')
            for row in results:
                date_o = row[3]
                time_o = row[4]
                art = row[5]
                payment = row[6]
                pref_gender = row[7]
                pref_age = row[8]
                print('| %12s | %10s | %20s | %10s | %15s | %20s |' % (date_o, time_o, art, payment, pref_gender, pref_age))
            print(106*'-')
            v = Visitor(self.conn, self.cursor)
        elif (choice == 'T'):
            rs = self.cursor.execute("SELECT * FROM Form_offer WHERE id_event = 't'")
            results = cursor.fetchall()
            print(106*'-')
            print('| %12s | %10s | %20s | %10s | %15s | %20s |' % ('Date', 'Time', 'Performance', 'Payment', 'Looking for...', 'around the age...'))
            print('|'+104*'-'+'|')
            for row in results:
                date_o = row[3]
                time_o = row[4]
                art = row[5]
                payment = row[6]
                pref_gender = row[7]
                pref_age = row[8]
                print('| %12s | %10s | %20s | %10s | %15s | %20s |' % (date_o, time_o, art, payment, pref_gender, pref_age))
            print(106*'-')
            v = Visitor(self.conn, self.cursor)
        else:
            print('Bye anyway')
        
        
    def register(self):
        print('Not available - building in progess...')
        v = Visitor(self.conn, self.cursor)
        
        
    def login(self):
        print('Not available - building in progess...')
        v = Visitor(self.conn, self.cursor)
        
        
    def write(self):
        #self.conn = conn
        #self.cursor = cursor        
        print(100*'_'+'\n'+100*' '+'\nIf you have any query, problem or sugestion, \nplease leave a short message including your email below and press Enter.\nTo back to the previous screen just press Enter.\n'+100*'_')    
        message = input()
        
        while not message:
            print(100*'_'+'\nNo message - redirecting to Visitor profile')
            v = Visitor(self.conn, self.cursor)
            break
        
        else:
            self.cursor.execute("INSERT INTO Form_contact(id_user, message, sending) VALUES (NULL, 'wiadomosc testowa1zwinga', True)")
            self.conn.commit()
            print( )
            print(46*'@'+'\n@'+9*' '+'Thank you for the message!'+9*' '+'@\n@ We will reply at our earliest convenience. @\n'+46*'@')
            v = Visitor(self.conn, self.cursor)
        
        
    def quit(self):
        print('See you soon. Bye!')
        