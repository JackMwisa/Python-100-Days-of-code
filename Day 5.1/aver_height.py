student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    
    student_heights[n] = int(student_heights[n])

print(student_heights)



summing = 0

for summs in student_heights:
    summing += summs #student_heights.index(summs)+1*summs
    
number = 0

for students in student_heights:
    number += 1
    
print(f"the total height is {summing}")
print(f" the number of students is {number}")

print(f" the average height of student is {summing // number}")
