'''
Regular Expression(RegEx)
------------------------
-->This RegEx is used from a search pattern to find out the string
contain squence char or not
-->To use this RegEx,we need to import re module

Functions
---------
Findall:
-->The search pattern is found than it will gives the o/p in the
        list[]
eg:
--
'''
import re
some='python is a programming languge'
print(re.findall('[a]',some))
#o/p:['a', 'a', 'a']

'''
Search:
-->This is also used to form a search pattern,but it will give
only the first matched object.
-->where it will gives with the index position,where the matched
object is found by the pattern.
eg:
--
'''
import re
do='i have 1000 rupees with me'
print(re.search('e',do))#o/p:<re.Match object; span=(5, 6), match='e'>

'''
Meta Characters
---------------
-->Meta characters are the symbols used in the search pattern.
1.[]
2..
3.+
4.^
5.$
6.?
7.*
8.{}

1.[]:
-->This [] symbol is used find a group char that present in the
string,where we can also specify the range.
syntax:
re.findall('[range]',variable_name)
-->By using this symbol we can search cap(A-Z),small(a-z),and digits(0-9).
eg:
--
'''
import re
some='We are in the class5'
print(re.findall('[aeiou]',some))
print(re.findall('[a-z]',some))
print(re.findall('[A-Z]',some))
print(re.findall('[0-9]',some))
print(re.search('[a-z]',some))
#o/p:
'''
['e', 'a', 'e', 'i', 'e', 'a']
['e', 'a', 'r', 'e', 'i', 'n', 't', 'h', 'e', 'c', 'l', 'a', 's', 's']
['W']
['5']
<re.Match object; span=(1, 2), match='e'>

2). char:
-->This symbol will refer only one means can match only a single char
in the pattern.
syntax:re.search('C...',variable_name)
eg:
--
'''
import re
some='Hello! World'
print(re.findall('H...o',some))
print(re.search('H...o',some))
#o/p:
'''
['Hello']
<re.Match object; span=(0, 5), match='Hello'>

3.+:
-->The symbol max number of sequence from the string from atleast one character.
syntax:re.findall('.+',variabl_name)
'''
import re
some='The symbol is used to find a group char that present'
print(re.findall('T.+r',some))#o/p:['The symbol is used to find a group char that pr']
'''
4.^:
-->The symbol is used to find pattern where string starting match or not
syntax:re.findall('^',variable_name)
'''
import re
some='Hello! Woeld'
print(re.findall('^He',some))
print(re.search('^Hello',some))
print(re.findall('^World',some))
print(re.search('^World',some))
#o/p:
'''
['He']
<re.Match object; span=(0, 5), match='Hello'>
[]
None


5.$:
--> This symbol will find out if the starting is ending with pattern or not.
syntax:re.findall('sequence$',variable_name)
eg:
--
'''
import re
any_='I am planning for a trip'
print(re.findall('for a trip$',any_))
print(re.search('for a trip$',any_))
#o/p:
'''
['for a trip']
<re.Match object; span=(14, 24), match='for a trip'>


6.?:
-->The symbol will find max upto 1 match in the string
syntax:re.findall('.?',variable_name)
eg:
--
'''
import re
some='Hello! World Hello! World Hello! World'
print(re.findall('Hel.?o',some))#o/p:['Hello', 'Hello', 'Hello']
'''
7.*:
-->The symbol max number of sequence from the string
syntax:re.findall('.*',variable_name)
eg:
--
'''
import re
some='The symbol is used to find a group char that present'
print(re.findall('T.*r',some))#o/p:['The symbol is used to find a group char that pr']
'''
8.{}:
-->The symbol is used to find a group char that present in string
syntax:re.findall('E.{size}',variable_name)
'''
import re
all_='I have 1000 rupees with me'
print(re.findall('I.{2,6}',all_))
print(re.findall('I.{2}',all_))
#o/p:
'''
['I have ']
['I have 1000 rupees with me']'''
#name start with capital letter
import re
user_name=input('Please enter your name:')
pattern=re.search('^[A-Z,a-z]{3,}$',user_name)
if pattern:
    print('correct')
else:
    print('incorrect')

#indian number
import re
num=input('please enter a number:')
find=re.findall('^[6-9][0-9]{9}$',num)
if find:
    print('Indian')
else:
    print('not Indian')
#o/p:
'''
please enter a number:9876543210
Indian
'''














    










