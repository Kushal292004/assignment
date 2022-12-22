#1
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
average = a+b+c/3
print("average is", average)

#2
a = int(input("gross income = "))

if(a>10000):
    b = int(input("number of dependants = "))

    taxable = a-(b*3000)-10000

    print("taxable income = ", taxable)
    tax = taxable*0.2
    print("tax = ", tax)

else:
    print("no tax")


#3
time = int(input("no. of seconds = "))
minute = int(time/60)
sec = time%60

print("time is equal to", minute,"minutes and", sec, "seconds")

#4
a = 25+int('25')+25.0
b = str(a)

print(b)
#5
import math

for i in range(0,350,+5):

    a = round(math.sin(i),4)
    b = round(math.cos(i),4)
    print(i,"=>",a," ",b)
