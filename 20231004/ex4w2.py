#Write a program to print n natural number
#in descending order using for loop

x=int(input("Enter a range:"))
y=[]

counter=x

while counter!=0:
    y.append(str(counter))
    counter-=1

#a=map(str,y)
z=' '.join(y)
print(z)


