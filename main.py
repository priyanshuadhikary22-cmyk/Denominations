def notes(a):
    Q=[2000, 1000, 500, 200, 100, 50, 10]
    X=0

    for i in range (6):
        q=Q[i]
        x=a//q
        print("Notes of {} = {}".format(q,x))
        a=a%q


amount = int(input("Enter your number:"))
notes(amount)

