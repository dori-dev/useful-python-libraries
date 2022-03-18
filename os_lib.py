"""os library
"""
import os

# os name
print(os.name)
print(os.uname())

# os environ
print(os.environ)
os.environ['TEST_VAR'] = 'python programming'
print(os.environ['TEST_VAR'])
print('TEST_VAR' in os.environ)
if 'ENV_VAR' not in os.environ:
    os.environ['ENV_VAR'] = 'value'
    print('add env var')
else:
    print("env var exist")

# directory
print(os.listdir())
print(os.listdir('/tmp'))
print(os.listdir('..'))
os.mkdir('test')  # make directory
os.rmdir('test')  # remove directory
print(os.getcwd())  # current directory
os.chdir('/tmp')  # change directory
print(os.getcwd())
os.makedirs('dir/test')
os.makedirs('dir/test2')
os.rename('dir', 'directory')  # for file and dir

# mini project for sort videos
PATH = '.'
os.chdir(PATH)
file_number = 1
for file_ in os.listdir():
    if file_.endswith('.mp4'):
        os.rename(file_, f'{str(file_number)}.mp4')
        file_number += 1

# permitions
os.system('touch test.txt')
FILE_NAME = 'test.txt'
if not os.access(FILE_NAME, os.W_OK):
    print(f"We can't write text in {FILE_NAME}")
else:
    with open(FILE_NAME, "w") as txt_file:
        txt_file.write('Hello, World!')

# run system commands
os.system('clear')
os.system('ls $HOME')
os.system('echo $HOME')
os.system('ping 8.8.8.8')
