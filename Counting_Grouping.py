#Write a function called item_order that takes as input a string named order. 
#The string contains only words for the items the customer can order separated by one space. 
#The function returns a string that counts the number of each item and consolidates them in the following order: 
#    salad:[# salad] hamburger:[# hambruger] water:[# water]
def item_order(order):
    s=0
    h=0
    w=0
    n=0
    while n<len(order):
        if order[n]=='s':
            s+=1
            n+=6
        elif order[n]=='h':
            h+=1
            n+=10
        elif order[n]=='w':
            w+=1
            n+=6
        else:
            return 'Invalid order'
    return 'salad:'+str(s)+' hamburger:'+str(h)+' water:'+str(w)