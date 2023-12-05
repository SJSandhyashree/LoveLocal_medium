def majority_elements(nums):
    # Check if the input list is empty
    if not nums:
        return []

    # Initialize two candidates and their counts
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # Iterate through the input list
    for num in nums:
        # Check if the current number is the same as candidate1
        if num == candidate1:
            count1 += 1
        # Check if the current number is the same as candidate2
        elif num == candidate2:
            count2 += 1
        # If count1 is 0, update candidate1 and reset count1 to 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        # If count2 is 0, update candidate2 and reset count2 to 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        # If neither candidate is matched, decrease both counts
        else:
            count1 -= 1
            count2 -= 1

    # Second pass to check the actual counts of candidates
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if the candidates appear more than n/3 times and return the result
    result = [candidate for candidate in (candidate1, candidate2) if nums.count(candidate) > len(nums) // 3]
    return result

# Take user input for the integer array
nums_input = input("Enter the integer array (comma-separated): ")
nums = [int(num) for num in nums_input.split(',')]

# Call the function with user input and print the result
result = majority_elements(nums)
print(f"Input: {nums}\nOutput: {result}")

