import os
import shutil

# 1. List of tasks
tasks = ["Study Python", "Do sport", "Read a book", "Sleep early"]

# 2. Create and write tasks into a file
file_name = "tasks.txt"
with open(file_name, "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("File tasks.txt has been created and tasks have been written successfully.")

# 3. Read and display file content
print("\nFile content:")
with open(file_name, "r") as file:
    content = file.read()
    print(content)

# 4. Rename the file
new_file_name = "my_tasks.list"
os.rename(file_name, new_file_name)
print(f"File has been renamed to {new_file_name}")

# 5. Create a folder if it doesn't exist
folder_name = "tasks_files"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' has been created.")

# 6. Move the file into the folder
shutil.move(new_file_name, folder_name)
print(f"File {new_file_name} has been moved into the folder '{folder_name}'.")

print("\nTasks have been organized successfully!")
