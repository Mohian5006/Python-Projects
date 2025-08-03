student_scores = [12,45,123,45,63,785,123,45,768,987,1]

highest = 0

for max in student_scores:
    if max > highest:
        highest = max

print(f"Highest Number is: {highest}")