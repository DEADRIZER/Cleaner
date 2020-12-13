import os, getpass

User= getpass.getuser()                                     # Get current user name
Temp= f"C:/Users/{User}/AppData/Local/Temp/"                # Temp path depending on user name

for root, dirs, files in os.walk(Temp, topdown=False):
    for name in files:
        try:
            print(f'Removing file... "{name}" : "{Temp+name}"')            
            os.remove(os.path.join(root, name))
        except Exception as e:
            if e == "PermissionError":
                print(f'Access denied : "{Temp+name}"')

    for name in dirs:
        try:
            print(f'Removing directory... "{name}" : "{Temp+name}"')
            os.rmdir(os.path.join(root, name))
        except Exception as e:
            if e == "PermissionError":
                print(f'Access denied : "{Temp+name}"')

