#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def div(p,q):
    '''
    Tests to see if p is divisible by all of the numbers from 1 to q.
    Returns 'True' if that is the case. 'False' if not.
    ''' 
    n=q
    q=1
    while q!=n:
        if p%q==0:
            q+=1
        else:
            return False
    return True


n=20
while div(n,20)!=True:
    n+=20
print(n)