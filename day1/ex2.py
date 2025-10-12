score = float(input("Enter your score: "))

if score >= 8.00:
    print("Excellent")
elif 6.5 <= score < 8.00:
    print("Good")
elif 5.0 <= score < 6.5:
    print("Average")
else:
    print("Weak")
