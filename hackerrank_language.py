# Enter your code here. Read input from STDIN. Print output to STDOUT
import re;

# Language list
language_list = list("C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(':'));

# Input the number of tests and test cases
tests = int(raw_input(''));
input_strings = [];
# Split each input to retan only the language part
for i in range(tests):
    input_strings.append(raw_input('')[::-1].rsplit()[0][::-1]);

# Compare RegEx and print result
for i in range(tests):
    if input_strings[i] in language_list:
        print("VALID");
    else:
        print("INVALID");
