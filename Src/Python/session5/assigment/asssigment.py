import os
import random

def thanos_project(folder_name="thanos_folder", file_count=10):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


    for i in range(file_count):
        file_path = os.path.join(folder_name, f"file_{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"This is file {i}")


    files = os.listdir(folder_name)
    print(f"Files before deletion: {len(files)}")


    files_to_delete = random.sample(files, len(files) // 2)
    for file in files_to_delete:
        os.remove(os.path.join(folder_name, file))


    remaining_files = os.listdir(folder_name)
    print(f"Files after deletion: {len(remaining_files)}")

# Example usage
thanos_project("thanos_folder", 10)
