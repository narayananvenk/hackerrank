# Enter your code here. Read input from STDIN. Print output to STDOUT
import re;

# Input the number of tests and test cases
tests = int(raw_input(''));
input_strings = [];
for i in range(tests):
    input_strings.append(raw_input(''));

# Use filter and regular expression pattern to check the email
result = list(filter(lambda x: re.match('^[-\w]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$',x),input_strings));

# print the result in lexicographic order
print(sorted(result));
