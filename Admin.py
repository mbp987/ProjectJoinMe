class Admin():
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
        
        #super().start()
        #self.member = Member
        print('What kind of events are you interested in?')
        
        rs = self.cursor.execute("SELECT * FROM cinemas")
        results = cursor.fetchall()
        print('%40s | %20s' % ('xxx', 'Street'))
        for row in results:
            cname = row[2]
            street = row[3]
            print('%40s | %20s' % (cname, street))