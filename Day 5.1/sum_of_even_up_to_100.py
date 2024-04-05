sum_even = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers from 1 to 100 is: ", sum_even)


sum_even_2 = 0

for i in range(2, 101, 2):
    sum_even_2 += i
    
print(sum_even_2)