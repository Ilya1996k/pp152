import re
numb = r'(?:(?:[1-9][0-9]*)|[0])'
reg = rf'(?:(?:{numb}[-*])*{numb})'
data = open(r'C:\Users\Еуфсрук\Downloads\24.txt').read()
print(max(re.findall(reg, data),key = len))
print(len(max(re.findall(reg, data),key = len)))

