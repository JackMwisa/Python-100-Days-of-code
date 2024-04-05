student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    
    student_scores[n] = int(student_scores[n])  # convert each element to integer from string

# calculate highest 

# for x in range(0, len(student_scores)):
#     if student_scores[x] > student_scores[x-1]:
#         highest = student_scores[x]
        
# print ("The highest score is: ", highest)

highest = 0

for score in student_scores:
    if score > highest:
        highest = score
print("Highest Score:", highest)