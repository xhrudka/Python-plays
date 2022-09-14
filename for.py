expenses=[10.5,8,5,15,20,5,3]
sum=0

for x in expenses:
    sum = sum + x

print("You spend $",sum, sep="")

# The Empty string sep does not allow a space, the resulr would look like: You spend $66.5