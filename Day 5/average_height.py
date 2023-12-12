
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    
    student_heights[n] = int(student_heights[n])

print(student_heights)


summing = 0

for summs in student_heights:
    summing += student_heights
    
print(summing)