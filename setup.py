from cx_Freeze import setup, Executable

includefiles = ['GoedeWoorden.txt', 'FouteWoorden.txt']

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("Spelling test E7 2",     # Shortcut
     "DesktopFolder",          # Directory_
     "Spelling test E7 2",     # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]WoordenTest.exe", # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

setup(name='CITO_Spelling_Trainer_E7_2',
      version='1.0',
      description='CITO Spelling oefening E7 2',
      author='PyEd',
      options = {'build_exe': {'include_files':includefiles},
                 'bdist_msi': bdist_msi_options},
      executables = [Executable(
                      "WoordenTest.py",
                      base=None)])
