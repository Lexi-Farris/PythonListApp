def sum_of_n(n):
  """
  Calculates the sum of all integers from 1 to n.

  Args:
  n (int): A positive integer up to which the sum is calculated.

  Returns:
  int: The sum of all integers from 1 to n.
  """
    # Handle the edge case where n is 0
    

    # Calculate the sum of numbers from 1 to n
    
  i = 1
  sum = 0

  while i <= n:
    sum += 1
    i +=1
  return sum 
    
# Test cases
print(sum_of_n(10))  # Expected output: 55
print(sum_of_n(25))  # Expected output: 325
print(sum_of_n(0))   # Expected output: 0
print(sum_of_n(100)) # Expected output: 5050