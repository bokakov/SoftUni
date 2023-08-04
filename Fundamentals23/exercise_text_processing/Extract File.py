file_path = input()
file_path_args = file_path.split("\\")
file_name_type = file_path_args[-1]

file_name = file_name_type.split(".")
file_type = file_name.pop()

print(f"File name: {'.'.join(file_name)}")
print(f'File extension: {file_type}')
