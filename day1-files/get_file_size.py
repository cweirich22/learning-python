import os

def largest_file(directory):
    biggest_name = None
    biggest_size = -1

    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue
        size = os.path.getsize(path)
        if size > biggest_size:
            biggest_size = size
            biggest_name = name

    return biggest_name, biggest_size

print(largest_file("day1-files"))

