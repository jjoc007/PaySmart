import os


class File:

    def deleteFile(self, file):
        os.remove(file)
        print("el archivo "+ file+ " fue eliminado.")