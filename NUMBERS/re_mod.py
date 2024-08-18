import re

print(type(re))

my_string = "My name is Valik."
my_string1 = "My name is Valik. Valik try find element."

res = re.search("Valik", my_string)
res1 = re.search("V...k", my_string)
res2 = re.search("V...k$", my_string)
res3 = re.search("^M.*name", my_string)
res4 = re.search("V...k.$", my_string)
res5 = re.search("\.$", my_string)
res6 = re.search("\n.$", my_string)

print(res)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print("Va..\n.$")
print(r"Va..\n.$")
print(res3.span())
print(res3.start())
print(res3.end())
print(type(res))

my_pattern = re.compile(r"Va..k\.$")
my_pattern1 = re.compile(r"^M.*\.$")
my_pattern2 = re.compile(r"V...k")

print(my_pattern)
print(my_pattern.search(my_string))
print(my_pattern1.match(my_string))
print(my_pattern2.findall(my_string1))
