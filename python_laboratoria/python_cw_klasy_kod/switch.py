def print1():
    print 1

def print2():
    print 2

def print3():
    print 3

switch = {}
switch['print 1'] = print1
switch['print 2'] = print2
switch['print 3'] = print3

switch['print 1']()
