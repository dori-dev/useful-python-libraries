"""sys library
"""
import sys

sys.path.append('/home')
print(sys.path)

# max of int the system can sopport
print(sys.maxsize)

print(sys.executable)  # python path
print(sys.platform)  # operating system
print(sys.version)  # python version


print(sys.argv)


try:
    name = sys.argv[1]
except IndexError:
    print('please enter your name')
    print('python sys_lib.py [name]')
else:
    print(f"Hello, {name}")
