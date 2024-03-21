stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
# Type your code below

x = stdform.find('x')
mantissa = stdform[:x]
exponent = stdform[x+4:]
error = "Error converting to scientific E notation."
#validation 
validity = 1
valid_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'x', '.', '-', '^']

if stdform.count('.') > 1:
  validity *= 0
elif stdform.count('^') > 1:
  validity *= 0
elif stdform.count('x') > 1:
  validity *= 0
elif any(chr not in valid_char for chr in stdform):
  validity *= 0


if validity == 0:
  print(error)
else:
  print(f'This number in E notation is {mantissa}E{exponent}.')
  