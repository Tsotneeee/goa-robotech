def volt1():
    R = float(input("resistance (ohm): "))
    I = float(input("current (A): "))
    U = R * I
    print(U ,"V")

def current1():
    R = float(input("resistance (ohm): "))
    U = float(input("voltage (V): "))
    I = U / R
    print(I ,"A")

def resistance1():
    U = float(input("voltage (V): "))
    I = float(input("current (A): "))
    R = U / I
    print(R ,"Ω")

def current2():
    q = float(input("charge (C): "))
    t = float(input("time (s): "))
    I = q / t
    print(I ,"A")

def charge1():
    I = float(input("current (A): "))
    t = float(input("time (s): "))
    q = I * t
    print(q ,"C")
    
def time1():
    q = float(input("charge (C): "))
    I = float(input("current (A): "))
    t = q / I
    print(t ,"s")

inp = input("category of calculation: ")
if inp == "resistance":
    resistance1()
elif inp == "current":
    c = input("charge and time or resistance and voltage? ")
    if c == "charge and time":
        current2()
    elif c == "resistance and voltage":
        current1()
    else:
        print("not found")
elif inp == "charge":
    charge1()
elif inp == "time":
    time1()
elif inp == "volt":
    volt1()