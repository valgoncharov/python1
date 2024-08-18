import time

print(time)

time.time()
print(time.time())
print(time.ctime(1522))
start_time = time.time()
time.sleep(2.5)
print(time.time())


end_time = time.time()
print(start_time - end_time)


start_time = time.time()
my_range = range(10000000)
print(my_range[1000])
end_time = time.time()

print("Total duration of the operation: ", end_time - start_time)
