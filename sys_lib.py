import sys
# sys.path.append('/home')
# print(sys.path)

# print(sys.maxsize) # max of int the my system can sopport theme :)
# print(2**63)
# print(sys.executable)
# print(sys.platform)
# print(sys.version)

# if sys.platform == 'linux':
#     sys.exit()
# else:
#     print('windows')



print(sys.argv)

if sys.argv[1] == 'admin':
    print('hi admin')
else:
    sys.exit()
    
#### ===> python sys_library.py <name>
