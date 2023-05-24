import pip
def install(package):
    pip.main(['install', PyInstaller])

try:
    import PyInstaller
    import os
    print('Module installed')
    import PyInstaller.__main__
    PyInstaller.__main__.run([
        '--onefile',
        '--distpath=dist/mac',
        os.path.join('deleteEmails.py'),
    ])
except:
    print('Module not installed')
    install('your_module')
