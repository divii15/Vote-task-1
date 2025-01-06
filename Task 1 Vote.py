#TASK 1
#5)Vote Eligible?
#input:12
#output:not eligible for vote
#input:19
#output:eligible for vote


age = int(input("Enter the number: "))
if age>=18 :
    print("Eligible for vote")
else :
    print("Not Eligible for vote")