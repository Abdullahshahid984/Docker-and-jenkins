import os
from time import strftime
from sys import platform, exc_info

def n_files(directory):
    total = 0
    for file in os.listdir(directory):
        if file.endswith(('.doc', '.docx', '.tmd')):
            total += 1
    return total

def doc2pdf_libreoffice(doc, ending, newdic):
    cmd = f"lowriter --convert-to pdf:writer_pdf_Export '{doc}'"
    os.system(cmd)
    new_file = doc.replace(ending, ".pdf")
    if platform == 'linux':
        cmdmove = f"mv '{new_file}' '{newdic}'"
    elif platform == 'win32':
        new_file = new_file.replace("/", "\\")
        cmdmove = f"move '{new_file}' '{newdic}'"
    os.system(cmdmove)
    print(new_file)

def is_tool(name):
    from shutil import which
    return which(name) is not None

if __name__ == "__main__":
    print('\nPlease note that this will overwrite any existing PDF files')
    print('For best results, close Microsoft Word before proceeding')
    
    directory = os.getcwd()
    
    if n_files(directory) == 0:
        print('There are no files to convert')
        exit()
    
    print('Starting conversion... \n')

    try:
        if not is_tool('libreoffice'):
            from win32com import client
            word = client.DispatchEx('Word.Application')
        
        for file in os.listdir(directory):
            if file.endswith(('.doc', '.docx', '.tmd')):
                ending = os.path.splitext(file)[1]
                
                if is_tool('libreoffice'):
                    in_file = os.path.abspath(os.path.join(directory, file))
                    new_file = os.path.abspath(os.path.join(directory, 'PDFs'))
                    doc2pdf_libreoffice(in_file, ending, new_file)
                else:
                    new_name = file.replace(ending, ".pdf")
                    in_file = os.path.abspath(os.path.join(directory, file))
                    new_file = os.path.abspath(os.path.join(directory, 'PDFs', new_name))
                    doc = word.Documents.Open(in_file)
                    print(new_name)
                    doc.SaveAs(new_file, FileFormat=17)
                    doc.Close()
    
    except Exception as e:
        print(e)

    print('\nConversion finished at ' + strftime("%H:%M:%S"))
