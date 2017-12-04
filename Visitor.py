class Visitor():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
        print(100*'_'+'\n| Here you may:   (R) - Register   (L) - Login   (W) - Write to us   (Q) - Quit')
        print('| Or just see the events:   (C) - Cinema   (T) - Theatre\n'+100*'_')
        
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
            rs = self.cursor.execute("SELECT * FROM cinemas")
            results = cursor.fetchall()
            print('%40s | %20s' % ('xxx', 'Street'))
            for row in results:
                cname = row[2]
                street = row[3]
                print('%40s | %20s' % (cname, street))   
        elif (choice == 'T'):
            rs = self.cursor.execute("SELECT * FROM theatres")
            results = cursor.fetchall()
            print('%40s | %20s' % ('xxx', 'Street'))
            for row in results:
                tname = row[2]
                street = row[3]
                print('%40s | %20s' % (tname, street))           
        else:
            print('Bye anyway')
        
    def register(self):
        print('Not available - building in progess...')
        
    def login(self):
        print('Not available - building in progess...')
        
    def write(self):
        print(100*'_'+'\nIf you have any query, problem or sugestion, please leave your message below.\nPress (B) to back to the previous screen\n'+100*'_')    
        message = input()
        if(message == 'B'):
            v = Visitor(self.conn, self.cursor)       
        elif(message == NULL):
            print('Thank you for the message!\nWe will reply at our earliest convenience')
        else:
            print('No text')
        
    def quit(self):
        print('See you soon. Bye!')
        