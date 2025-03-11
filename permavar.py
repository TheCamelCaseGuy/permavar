import os
import  json
import time


def readFile(filePath):

    try:

        with open(filePath, 'r') as file:
            content = file.read()

        return content

    except FileNotFoundError:

        return "File not found."

    except Exception as e:

        return f"An error occurred: {e}"

def writeFile(filePath, content):

    try:

        with open(filePath, 'w') as file:
            file.write(content)

        return "File written successfully."

    except Exception as e:

        return f"An error occurred: {e}"

def readJSON(filepath):

    return  json.loads(readFile(filepath))

def writeJSON(filepath, content):

    writeFile(filepath, json.dumps(content))

def createDir(path):
    try:
        os.makedirs(path, exist_ok=True)
        return f"Directory '{path}' created successfully."
    except Exception as e:
        return f"An error occurred: {e}"



class PermaVar:

    def __init__(self, path, id):

        self.path: str = path
        self.id: str = id
        self.folder: str = os.path.join(path, id)
        self.mainfile: str = os.path.join(self.folder, "main")


        if not os.path.isfile(self.mainfile):

            writeJSON(self.mainfile, {})

        createDir(os.path.join(self.folder, "objects"))

    def getdata(self):

        data: dict = readJSON(self.mainfile)
        return data

    def set(self, variable, content):

        data: dict = self.getdata()
        data[variable] = content

        writeJSON(self.mainfile, data)

    def get(self, variable):

        data: dict = self.getdata()
        return data[variable]

    def list(self):

        data: dict = self.getdata()
        keys = list(data.keys())

        return keys

def editor(permavar: PermaVar):

    print("PERMAVAR DEFAULT EDITOR\n")

    def loop():

        cmd = input("   >>> ")
        if cmd == "list":
            data = permavar.list()

            for i in data:
                print(f"{i}: {permavar.get(i)}")

        elif cmd == "get":

            var = input("VAR   >>> ")

            try:
                print(permavar.get(var))

            except:
                print("INVALID VARIABLE")

        elif cmd == "set":

            var = input("VAR   >>> ")
            txt = input("CON   >>> ")

            try:
                permavar.set(var, txt)

            except:
                print("INVALID VARIABLE")

        loop()

    loop()


if __name__ == "__main__":

    print("TEST")
    pv = PermaVar("", "test")
    time.sleep(3)
    editor(pv)
