# Enter your code here. Read input from STDIN. Print output to STDOUT
import re;

# Input the number of tests and test cases
tests = int(raw_input(''));
input_strings = [];
for i in range(tests):
    input_strings.append(raw_input(''));
# Compare RegEx and print result
for i in range(tests):
    if len(input_strings[i]) <= 10 and re.match('^[A-Z]{5}[0-9]{4}[A-Z]$',input_strings[i]) is not None:
        print("YES");
    else:
        print("NO");
