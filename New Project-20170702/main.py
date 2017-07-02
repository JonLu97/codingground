def factorial(n): 
    if n ==1:
        return 1
    else: 
        return n*factorial(n-1)
        
print factorial(7)


import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom
    

print ncr(5, 2)






