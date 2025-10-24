#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2
s='bobrbobobthbob'
b=0
n=0
while n!=len(s):
    if s[n:n+3]=='bob':
        b+=1
    n+=1
print 'Number of times bob occurs is: '+str(b)