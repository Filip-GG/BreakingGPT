#Функция для конвертирования docx в pdf
def docx_to_pdf(location_file : str, out_location = './dataset/'):
    from docx2pdf import convert
    try:
        name_file = location_file.split('/')[-1:][0].split('.')[0] + '.pdf'
        convert(location_file, out_location+name_file)
        return True
    except:
        return 'Error convect'

#Функция для конвертирования doc в dox
def doc_to_docx(location_file : str, out_location = './dataset_input/'):
    from doc2docx import convert
    try:
        name_file = location_file.split('/')[-1:][0].split('.')[0] + '.docx'
        convert(location_file, out_location+name_file)
        return True
    except:
        return 'Error convect'
    
#Функция для конвертирования doc в pdf    
def doc_to_pdf(location_file : str, out_location = './dataset/'):
    try:
        if doc_to_docx(location_file) != True:
            return 'Error convect doc_to_docx'
        patch_file = './dataset_input/'+location_file.split('/')[-1:][0].split('.')[0] + '.docx'
        if docx_to_pdf(patch_file, out_location) != True:
            return 'Error convect docx_to_pdf'
        return  True
    except:
        return 'Error convect'
#без водяных знаков но медленее

'''
#Функция для конвертирования doc в pdf
def doc_to_pdf(location_file : str, out_location = './dataset/'):
    import aspose.words as aw
    try:
        name_file = location_file.split('/')[-1:][0].split('.')[0] + '.pdf'
        doc = aw.Document(location_file)
        doc.save(out_location+name_file)
        return True
    except:
        return 'Error convect'
#имеет водяные знакит из библиотеки
'''