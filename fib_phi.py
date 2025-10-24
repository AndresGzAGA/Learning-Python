# En la serie de Fibonachi. El cociente f(i+1)/f(i) se aproxima a phi conforme i se aproxima a infinito.
def f(i):
    '''
    Aproxima phi con el cociente f(i+1)/f(i) en la serie fibonacci.
    '''
    last=0.0
    now=1.0
    next=1.0
    n=0
    while n!=i:
        last=now
        now=next
        next=now+last
        n+=1
    return 'phi es aproximadamente: ' + str(next/now)