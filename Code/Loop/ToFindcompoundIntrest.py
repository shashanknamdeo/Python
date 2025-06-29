def toFindCompoundIntrest(p,t,r):
    
    ##ci=p(1+r/100)**t
    a = r/100
    b = 1+a
    c = b**t
    d = c-1
    e = d*p
    return e

p = float(input("Enter Amount"))

r = float(input("Enter rate of intrest"))

t = float(input("Enter time"))


ci = toFindCompoundIntrest(p,t,r)
print(ci)