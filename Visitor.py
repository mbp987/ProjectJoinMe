import pymysql
import sys

class Visitor():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
        print(106*'_'+106*' '+'\n'+'\nHere you may:   (R) - Register   (L) - Login   (W) - Write to us   (Q) - Quit')
        print(106*' ')
        print('Or just see the events:   (C) - Cinema   (T) - Theatre\n'+106*'_')
        
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
        
        login = input('Choose your login: ')
        user_pass = input('Insert your password: ')
        email = input('Email: ')
        gender = input('Gender (F/M): ').upper()
        birthdate = input('Year of your birth (YYYY): ')
        #tu jest problem
        self.cursor.execute("INSERT INTO users(login, user_pass, email, gender, birthdate) VALUES (%s, %s, %s, %s, %s)" % (login, user_pass, email, gender, birthdate))
        self.conn.commit()        
        
        print('Not available - building in progess...')
        v = Visitor(self.conn, self.cursor)        
        
        
    def login(self):
        login = input('Insert your login: ')
        user_pass = input('Password: ')
        #do dokonczenia
        print('Not available - building in progess...')
        v = Visitor(self.conn, self.cursor)
        
        
    def write(self):
        print(106*'_'+'\n'+106*' '+'\nIf you have any query, problem or sugestion,\n    please leave a short message including your email below and press Enter.\nTo back to the previous screen just press Enter.\n'+106*'_')    
        message = input()
        
        while not message:
            print(106*'_'+'\nNo message - redirecting to Visitor profile')
            v = Visitor(self.conn, self.cursor)
            break
        else:
            #tu jest problem
            self.cursor.execute("INSERT INTO form_contact (id_user, message, sending) VALUES (NULL, 'wiadomosc testowa1zwinga', True);")
            self.conn.commit()
            #self.conn.close()
            #self.cursor.execute("select * from form_contact;")
            #res = self.cursor.fetchall() 
            #print(res)
            print( )
            print(46*'@'+'\n@'+9*' '+'Thank you for the message!'+9*' '+'@\n@ We will reply at our earliest convenience. @\n'+46*'@')
            v = Visitor(self.conn, self.cursor)
            
        
    def quit(self):
        print('See you soon. Bye!')
        