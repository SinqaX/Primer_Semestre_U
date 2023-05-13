import os.path
import shutil

home_folder = os.path.expanduser('~')

def formatRuta(ruta):
    newHome = ''
    for a in ruta:
        if a == '\\':
            newHome = newHome + '/'
        else:
            newHome = newHome + a

    return newHome


newHome = formatRuta(home_folder)+'/'
rutaActual = os.path.abspath(os.getcwd())
rutaActual = formatRuta(rutaActual)

print(newHome)
print(rutaActual)

if _name_ == "__main__":
    for filename in os.listdir(newHome):
        name, extension = os.path.splitext(newHome + filename + '/')
        if filename == 'Pictures':
            shutil.copytree(name, rutaActual+'/recovery_data')