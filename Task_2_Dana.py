import sqlite3

def read_cake():
    f = open("CAKE.txt", "r")
    con = sqlite3.connect("bakery.db")
    line = f.readline()
    while line:
        num, name, date, typ, price, source, country = line.split(',')
        comm = "INSERT INTO 'BakeryItem' VALUES ({}, '{}', '{}', '{}', {}, '{}')".format(num, name, date, typ, price, source)
        comm2 = "INSERT INTO 'Cake' VALUES ({}, '{}')".format(num, country)
        con.execute(comm)
        con.execute(comm2)
        line = f.readline()
    f.close()
    con.commit()
    con.close()

#read_cake()

def read_bread():
    f = open("BREAD.txt", "r")
    con = sqlite3.connect("bakery.db")
    line = f.readline()
    while line:
        num, name, date, typ, price, source, subtype = line.split(',')
        comm = "INSERT INTO 'BakeryItem' VALUES ({}, '{}', '{}', '{}', {}, '{}')".format(num, name, date, typ, price, source)
        comm2 = "INSERT INTO 'Bread' VALUES ({}, '{}')".format(num, subtype)
        con.execute(comm)
        con.execute(comm2)
        line = f.readline()
    f.close()
    con.commit()
    con.close()

#read_bread()

def read_moon():
    f = open("MOONCAKE.txt", "r")
    con = sqlite3.connect("bakery.db")
    line = f.readline()
    while line:
        num, name, date, typ, price, source, lard = line.split(',')
        comm = "INSERT INTO 'BakeryItem' VALUES ({}, '{}', '{}', '{}', {}, '{}')".format(num, name, date, typ, price, source)
        comm2 = "INSERT INTO 'Mooncake' VALUES ({}, '{}')".format(num, lard)
        con.execute(comm)
        con.execute(comm2)
        line = f.readline()
    f.close()
    con.commit()
    con.close()

read_moon()