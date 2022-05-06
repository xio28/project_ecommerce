import os

abs_path = os.getcwd()

print(os.path.relpath("git_commands.txt", abs_path))
