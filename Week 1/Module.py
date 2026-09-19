
  # importing the module
import calculator

  # initializing variables
num_1 = 16
num_2 = 7

  # calling functions from the module
total = calculator.add(num_1, num_2)
diff = calculator.subtract(num_1, num_2)
prod = calculator.multiply(num_1, num_2)
quot = calculator.divide(num_1, num_2)

  # printing results
print(num_1, '+', num_2, '=', total)
print(num_1, '-', num_2, '=', diff)
print(num_1, '*', num_2, '=', prod)
print(num_1, '/', num_2, '=', quot)