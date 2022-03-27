import re

content = "Hello 123 4567 World_This is a Regex Demo"
result = re.match("Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$",content)
print(result)


infor = "My name is Kinoz tel:19823420823"
result2 = re.match("My\s.*\w{5}\s\w{3}.\d{11}",infor)
print(result2)