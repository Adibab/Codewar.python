def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        
        smallest = numbers[0]
        
        for num in numbers:
            if num < smallest:
                smallest = num
            smallest_index = numbers.index(smallest)
            return smallest_index
        # min_value = min(numbers)
        # min_value_index = numbers.index(min_value)
        # return numbers[: min_value_index] + numbers[ min_value_index+1:]
        
        print(remove_smallest([2,2,1,2,1]))