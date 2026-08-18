from pathlib import Path
import os

def createfile():


    try:
            
        name=input("pls enter ur file name:--")

        path= Path(name)

        if not path.exists():      # not turns true to false and vice versa
            with open(path, "w") as fs:
                data=input("what u want to write:--")

                fs.write(data)
                print("file created succesfully")

        else:
            print("Error file name already exists")


    except Exception as err:
        print(f"an error occuresd as {err}")






    
def readfile():  
    try:
            
        name=input("pls tell your file name:--")

        path=Path(name)
        if path.exists():
            with open(path,"r") as f:

                content=f.read()
                print(f" Your file content is \n {content}")

        else:
            print("error no such file exist")
    except Exception as err:
        print(f"  an error occured as {err}")



def updatefile():
    
    name=input(" Enter the file name:-")
    path=Path(name)

    if path.exists():
        print("operations")
        print("1 . Renaming the file")
        print("2. Appending the content")
        print("3. Overwritting the file")

        choice=int(input("Enter your responsse:-"))

        if choice==1:

            newname=input("Tell your new file name:-")

            new_path=Path(newname)

            if not new_path.exists():
               path.rename(new_path)
               print("Renamed successfully")
            else:
                print("File already exist")

        elif choice==2:

            with open(path,"a") as fs:
                data= input("What do you want to append:-")
                fs.write("\n" +data)

                print("sUCCESFULLY APPENDED")

        elif choice==3:
            with open(path, "w") as fs:
                data=input("What you want to overwrite:-- ")

                fs.write(data)
                print(" SUCCESFULLY OVERWRITTEN")








def deletefile():
    pass

print ("press 1 for creating a file")
print ("press 2 for reading a file")
print ("press 3 for updating a file")
print ("press 4 for deleting a file")

a=int(input("tell ur response:-"))

if a==1:
    createfile()

if a==2:
    readfile()

if a==3:
    updatefile()

if a==4:
    deletefile()
