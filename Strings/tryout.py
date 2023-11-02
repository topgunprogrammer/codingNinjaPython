
a = "abc"
'''
| Method       | Description                                                 | Example                                               |
|--------------|-------------------------------------------------------------|-------------------------------------------------------|
| capitalize() | Converts the first character to upper case                   | `"hello".capitalize()` => `"Hello"`                   |
| casefold()   | Converts string into lower case                              | `"HELLO".casefold()` => `"hello"`                      |
| center()     | Returns a centered string                                    | `"hello".center(10)` => ` "  hello  "`                 |
| count()      | Returns the number of times a specified value occurs        | `"hello".count('l')` => `2`                            |
| encode()     | Returns an encoded version of the string                     | `"hello".encode()` => `b'hello'`                       |
| endswith()   | Returns true if the string ends with the specified value     | `"hello".endswith('lo')` => `True`                     |
| expandtabs() | Sets the tab size of the string                              | `"hello\tworld".expandtabs(4)` => `'hello   world'`     |
| find()       | Searches the string for a specified value and returns position | `"hello".find('e')` => `1`                           |
| format()     | Formats specified values in a string                         | `"My name is {name}".format(name="John")` => `"My name is John"` |
| format_map() | Formats specified values in a string                         | `"My name is {name}".format_map({'name': 'Alice'})` => `"My name is Alice"` |
| index()      | Searches the string for a specified value and returns position | `"hello".index('e')` => `1`                         |
| isalnum()    | Returns True if all characters in the string are alphanumeric | `"hello123".isalnum()` => `True`                     |
| isalpha()    | Returns True if all characters in the string are in the alphabet | `"hello".isalpha()` => `True`                       |
| isascii()    | Returns True if all characters in the string are ASCII characters | `"hello".isascii()` => `True`                       |
| isdecimal()  | Returns True if all characters in the string are decimals    | `"123".isdecimal()` => `True`                        |
| isdigit()    | Returns True if all characters in the string are digits      | `"123".isdigit()` => `True`                          |
| isidentifier() | Returns True if the string is an identifier                | `"hello".isidentifier()` => `True`                    |
| islower()    | Returns True if all characters in the string are lowercase   | `"hello".islower()` => `True`                        |
| isnumeric()  | Returns True if all characters in the string are numeric     | `"123".isnumeric()` => `True`                        |
| isprintable()| Returns True if all characters in the string are printable   | `"hello\n".isprintable()` => `False`                  |
| isspace()    | Returns True if all characters in the string are whitespaces  | `"  \t\n".isspace()` => `True`                       |
| istitle()    | Returns True if the string follows the rules of a title       | `"Hello World".istitle()` => `True`                   |
| isupper()    | Returns True if all characters in the string are uppercase   | `"HELLO".isupper()` => `True`                        |
| join()       | Converts the elements of an iterable into a string           | `"-".join(['a', 'b', 'c'])` => `"a-b-c"`              |
| ljust()      | Returns a left-justified version of the string               | `"hello".ljust(10)` => `"hello     "`                 |
| lower()      | Converts a string into lowercase                             | `"Hello".lower()` => `"hello"`                        |
| lstrip()     | Returns a left-trimmed version of the string                 | `"   hello   ".lstrip()` => `"hello   "`              |
| maketrans()  | Returns a translation table to be used in translations       | `str.maketrans('aeiou', '12345')`                     |
| partition()  | Returns a tuple where the string is parted into three parts  | `"hello world".partition(' ')` => `('hello', ' ', 'world')` |
| replace()    | Returns a string where a specified value is replaced with another specified value | `"hello".replace('l', 'p')` => `"heppo"`  |
| rfind()      | Searches the string for a specified value and returns the last position of where it was found | `"hello".rfind('l')` => `3`                    |
| rindex()     | Searches the string for a specified value and returns the last position of where it was found | `"hello".rindex('l')` => `3`                   |
| rjust()      | Returns a right-justified version of the string               | `"hello".rjust(10)` => `"     hello"`                 |
| rpartition() | Returns a tuple where the string is parted into three parts starting from the right | `"hello world".rpartition(' ')` => `('hello', ' ', 'world')` |
| rsplit()     | Splits the string at the specified separator from the right, and returns a list | `"apple,orange,banana".rsplit(',')` => `['apple', 'orange', 'banana']` |
| rstrip()     | Returns a right-trimmed version of the string                | `"   hello   ".rstrip()` => `"   hello"`              |
| split()      | Splits the string at the specified separator, and returns a list | `"apple,orange,banana".split(',')` => `['apple', 'orange', 'banana']` |
| splitlines() | Splits the string at line breaks and returns a list           | `"Hello\nWorld".splitlines()` => `['Hello', 'World']` |
| startswith() | Returns true if the string starts with the specified value    | `"hello".startswith('he')` => `True`                  |
| strip()      | Returns a trimmed version of the string                       | `"   hello   ".strip()` => `"hello"`                  |
| swapcase()   | Swaps cases, lower case becomes upper case and vice versa     | `"Hello World".swapcase()` => `"hELLO wORLD"`          |
| title()      | Converts the first character of each word to upper case       | `"hello world".title()` => `"Hello World"`            |
| translate()  | Returns a translated string using a translation table        | `"hello".translate(str.maketrans('aeiou', '12345'))` => `"h2ll4"` |
| upper()      | Converts a string into uppercase                              | `"hello".upper()` => `"HELLO"`                        |
| zfill()      | Fills the string with a specified number of 0 values at the beginning | `"42".zfill(5)` => `"00042"`                          |
'''