import os
import collections


def get_all_files(path):
    files = {}
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            files.update(get_all_files(file_path))
        else:
            files[file_path] = (file, os.path.getsize(file_path))
    return files


def get_duplicates(path):
    all_files = get_all_files(path)
    duplicates = collections.defaultdict(list)
    for path, file in all_files.items():
        if list(all_files.values()).count(file) > 1:
            duplicates[file].append(path)
    return duplicates


def print_duplicates(duplicates):
    for file, paths in sorted(duplicates.items(), key=lambda x: x[0][1], reverse=True):
        print('file {} ({} bytes) occurs {} times:'.format(file[0], file[1], len(paths)))
        print('\n'.join(paths))


if __name__ == '__main__':
    path = input('input path: ')
    duplicates = get_duplicates(path)
    print_duplicates(duplicates)
