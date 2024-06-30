import module_one
from module_one import print_name
# import module_one as m_one
import other

print_name("Val")

module_one.print_name("Valik")

print(type(module_one))
print(dir(module_one))

print(other)
print(type(other))
print(other.print_sum(3, 6))
print(other.my_name)
