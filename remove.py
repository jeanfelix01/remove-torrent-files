import os

def save_file_txt(folder_path, txt_file_name):
    with open(txt_file_name, 'w') as txt_file:
        for filename in os.listdir(folder_path):
            txt_file.write(filename + '\n')
    print('File name Txt: ' + txt_file_name)

def delete_torrents(delete_path, txt_file_name):
    with open(os.path.join(txt_file_name), 'r') as txt_file:
        file_names = [line.strip() for line in txt_file.readlines()]

    for filename in os.listdir(delete_path):
        if filename.endswith('.torrent'):
           # Remove .torrent extension from file name
            name_without_ext = os.path.splitext(filename)[0]
            if name_without_ext not in file_names:
                file_path = os.path.join(delete_path, filename)
                os.remove(file_path)
                print(f'File {filename} removed.')


folder_path = 'path downloaded torrents'
txt_file_name = 'files.txt'
delete_path = 'path .torrents files'

save_file_txt(folder_path, txt_file_name)
delete_torrents(delete_path, txt_file_name)

