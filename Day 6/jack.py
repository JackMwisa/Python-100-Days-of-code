def invert_dictionary(original_dict):
    inverted_dict = {}
    
    # Iterate through each student in the original dictionary
    for student, courses in original_dict.items():
        # Iterate through each course for the student
        for course in courses:
            # Check if the course is already a key in the inverted dictionary
            if course in inverted_dict:
                # If the course is already a key, append the student to the existing list of values
                inverted_dict[course].append(student)
            else:
                # If the course is not a key, create a new key with the student as the first value
                inverted_dict[course] = [student]
    
    return inverted_dict

# Sample input
original_dict = {
    'Stud1': ['CS1191', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Print the original dictionary
print("Original Dictionary:")
print(original_dict)

# Generate and print the inverted dictionary
inverted_dict = invert_dictionary(original_dict)
print("\nInverted Dictionary:")
print(inverted_dict)
