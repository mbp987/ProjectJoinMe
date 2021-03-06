CREATE DATABASE joinme DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE joinme;
#drop database joinme;


CREATE TABLE Users (
    id_user INT(10) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(25) UNIQUE,
    user_pass VARCHAR(30),
    email VARCHAR(30),
    gender VARCHAR(1),
    birthdate YEAR,
    photo MEDIUMBLOB
);
#drop table Users;


CREATE TABLE VarEvents (
    id_event VARCHAR(5) Primary key,
    event_name VARCHAR(15)
);
#drop table VarEvents;


CREATE TABLE Cinemas (
    id_cinema INT(10) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_event VARCHAR(5),
    cname VARCHAR(35),
    street VARCHAR(50),
    snumber INT(4),
    city VARCHAR(20),
    FOREIGN KEY (id_event)
        REFERENCES VarEvents (id_event)
);
#drop table Cinemas;


CREATE TABLE Theatres (
    id_theatre INT(10) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_event VARCHAR(5),
    tname VARCHAR(40),
    street VARCHAR(50),
    snumber INT(4),
    city VARCHAR(20),
    FOREIGN KEY (id_event)
        REFERENCES VarEvents (id_event)
);
#drop table Theatres;


CREATE TABLE Form_offer (
    id_offer INT(15) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_user INT(10) ZEROFILL,
    id_event VARCHAR(5),
    date_o DATE,
    time_o TIME,
    art VARCHAR(30),
    payment VARCHAR(15),
    pref_gender VARCHAR(1),
    pref_age VARCHAR(10),
    FOREIGN KEY (id_event)
        REFERENCES VarEvents (id_event),
    FOREIGN KEY (id_user)
        REFERENCES Users (id_user)
);
#drop table Form_offer;


CREATE TABLE Form_cand (
    id_answer INT(20) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_offer INT(15) ZEROFILL,
    id_user_o INT(10) ZEROFILL,
    id_user_c INT(10) ZEROFILL,
    date_limit DATE,
    time_limit TIME,
    approval_c BOOLEAN,
    approval_o BOOLEAN,
    FOREIGN KEY (id_offer)
        REFERENCES Form_offer (id_offer),
    FOREIGN KEY (id_user_o)
        REFERENCES Users (id_user),
    FOREIGN KEY (id_user_c)
        REFERENCES Users (id_user)
);
#drop table Form_cand;


CREATE TABLE User_log (
    id_log INT(10) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_user INT(10) ZEROFILL,
    user_pass VARCHAR(30),
    date_login DATE,
    time_login TIME,
    user_language VARCHAR(10),
    FOREIGN KEY (id_user)
        REFERENCES Users (id_user)
);
#drop table User_log;


CREATE TABLE Form_contact (
	id_contact INT(10) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    id_user INT(10) ZEROFILL,
    message TEXT(200),
    sending BOOLEAN,
    date_contact DATE,
    time_contact TIME,
    FOREIGN KEY (id_user)
        REFERENCES users (id_user)
);
#drop table Form_contact;



############################################
-- adding example data to tables manually (small table)

insert into VarEvents(id_event, event_name) values ('c', 'cinema');
insert into VarEvents(id_event, event_name) values ('t', 'theatre');


-- adding example data to tables from *.txt files


load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Users.txt' into table Users fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_user, login, user_pass, email, gender, birthdate);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe//User_log.txt' into table User_log fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_user, user_pass, date_login, time_login, user_language);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Cinemas.txt' into table Cinemas fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_cinema, id_event, cname, street, snumber, city);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Theatres.txt' into table Theatres fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_theatre, id_event, tname, street, snumber, city);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Form_offer.txt' into table Form_offer fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_offer, id_user, date_o, time_o, art, payment, pref_gender, pref_age, id_event);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Form_cand.txt' into table Form_cand fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_answer, id_offer, id_user_o, id_user_c, date_limit, time_limit, approval_c, approval_o);

load data local infile 'Users/mbp/Desktop/ProjectJoinMe/Form_contact.txt' into table Form_contact fields terminated by '\t' lines terminated by '\n' ignore 1 lines (id_contact, id_user, message, sending, date_contact, time_contact);



############################################
-- helpful for checking

#SELECT * FROM Users;
#SELECT * FROM User_log;
#SELECT * FROM Form_offer;
#SELECT * FROM Form_cand;
#SELECT * FROM Form_contact;
#SELECT * FROM VarEvents;
#SELECT * FROM Theatres;
#SELECT * FROM Cinemas;