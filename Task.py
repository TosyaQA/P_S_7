#Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
#расширение
#минимальная длина случайно сгенерированного имени, по умолчанию 6
#максимальная длина случайно сгенерированного имени, по умолчанию 30
#минимальное число случайных байт, записанных в файл, по умолчанию 256
#максимальное число случайных байт, записанных в файл, по умолчанию 4096
#количество файлов, по умолчанию 42
#Имя файла и его размер должны быть в рамках переданного диапазона.
#Чтобы записать байты можно использовать список с числами и функцию bytes

import random
import pathlib

def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096, num_files=42):
    for _ in range(num_files):
        file_name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(min_name_length, max_name_length)))
        file_path = pathlib.Path(file_name + extension)

        file_size = random.randint(min_bytes, max_bytes)
        file_content = bytes([random.randint(0, 255) for _ in range(file_size)])

        with file_path.open('wb') as file:
            file.write(file_content)

create_files_with_extension('.txt')