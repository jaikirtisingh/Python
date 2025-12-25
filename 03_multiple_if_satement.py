a=int(input("Enter your age:"))
#if statement no:1
if(a%2==0):
    print("a is even")
# End of if statement no:1
#if statement no:2
if(a>18):
    print("you are above age of  consent")
    print("good for you")
elif(a<0):
    print("you are entering an invalid age ")
elif(a==0):
    print("you are entering 0 which is not a valid age  ")
else:
    print("you wre below the age consent ")

#end of if statement no:2
print("End of program ")