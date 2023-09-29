import subprocess

# Replace 'your_folder_path' with the actual path of the folder you want to navigate to
folder_path = 'C:\\Your\\Folder\\Path'

# Replace 'your_cpp_file.cpp' with the name of your C++ source file
cpp_file = 'your_cpp_file.cpp'

# Build the command to change directory, compile the C++ file, run it, and open a new Command Prompt window
cmd_command = f'cd /d {folder_path} && g++ {cpp_file} -o {cpp_file[:-4]}.exe && {cpp_file[:-4]}.exe && start cmd'

# Compile the C++ file, run the executable, and open a new Command Prompt window in the specified directory
subprocess.Popen(cmd_command, shell=True)
