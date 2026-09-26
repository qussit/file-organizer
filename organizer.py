import os
folder = input("Enter folder path: ")
list_files = os.listdir(folder)
for file in list_files:
    extension = os.path.splitext(file)[1].lower()
    if extension in [".jpg", ".png", ".gif"]:
        category = 'Images'
    elif extension in [".mp4", ".avi", ".mkv"]:
        category = "Videos"
    elif extension in [".doc", ".docx", ".pdf", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"]:
        category = "Documents"
    elif extension in [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".exe"]:
        category = "Archives"
    elif extension == ".torrent":
        category = "Torrents"
    elif extension in [".mp3", ".wav", ".aiff", ".flac", ".ape", ".m4a", ".aac", ".ogg"]:
        category = "Music"
    else:
        category = "Unknown"
    category_path = os.path.join(folder, category)
    os.makedirs(category_path, exist_ok=True)
    print(f'{file} >> {category}')
