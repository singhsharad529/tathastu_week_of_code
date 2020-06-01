p1 = int(input("Enter 1st player runs\n"))
p2 = int(input("Enter 1st player runs\n"))
p3 = int(input("Enter 1st player runs\n"))

st1=(p1*100)/60
st2=(p2*100)/60
st3=(p3*100)/60

print("Strike rate of 1st player:",st1)
print("Strike rate of 2nd player:",st2)
print("Strike rate of 3rd player:",st3)

print("\nIf they play 60 more balls then:\n")
print("\nStrike rate of 1st player:",st1*2)
print("Strike rate of 2nd player:",st2*2)
print("Strike rate of 3rd player:",st3*2)

print("Maximum number of sixes each player could hit:\n")
print("Player 1 :",p1//6)
print("Player 2 :",p2//6)
print("Player 3 :",p3//6)
