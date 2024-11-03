import os
import shutil
import pdf_convector

# Удаление файла
def delete_file(patch):
    try:
        os.remove(patch)
        return True
    except:
        print('Error delete')
        return False

# Получение списка директорий
def dataset_listdir(patch):
    return os.listdir(patch)

# набор ф-ций для получения списка файлов типа docx, doc, pdf
def list_docx_file(patch):
    return list(
        filter(
            lambda item:
            item[-5:] == '.docx',
            dataset_listdir(patch)
        )
    )

def list_doc_file(patch):
    return list(
        filter(
            lambda item:
            item[-4:] == '.doc',
            dataset_listdir(patch)
        )
    )

def list_pdf_file(patch):
    return list(
        filter(
            lambda item:
            item[-4:] == '.pdf',
            dataset_listdir(patch)
        )
    )

# ф-ция копирывания
def copy(path, out_path):
    try:
        shutil.copy(path, out_path)
        return True
    except:
        print('Error: copy file')
        return 'Error: copy file'

# Переводить все в pdf
def to_all_pdf(path, out_path):
    try:
        all = dataset_listdir(path)
        print(list(map(lambda item: pdf_convector.doc_to_pdf(item, out_path), list(map(lambda item: path+'/'+item, list_doc_file(path))))))
        print(list(map(lambda item: pdf_convector.docx_to_pdf(item, out_path), list(map(lambda item: path+'/'+item, list_docx_file(path))))))
        print(list(map(
            lambda item:
            copy(item[0], item[1]),
            list(
                zip(
                    list(map(lambda item: path+'/'+item, list_pdf_file(path))),
                    list(map(lambda item: out_path+'/'+item, list_pdf_file(path)))
                )
            )
            )))
        data_list = dataset_listdir(path)
        for link in data_list:
            delete_file(path+'/'+link)
        return True
    except:
        print('Error: all to pdf')
        return 'Error: all to pdf'    