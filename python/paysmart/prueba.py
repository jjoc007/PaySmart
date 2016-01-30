import time

from cargue.CSVUtils import CSVUtils
from util.Constantes import Constantes
from util.File import File

from mongodb.LoadDataAnalitic import LoadDataAnalitic

if __name__ == "__main__":

    t0 = time.clock()

    mongoDB = LoadDataAnalitic()
    utilFile = CSVUtils()

    utilFile.parseCsvToJson()
    mongoDB.insertMasive("empleados")

    file = File()
    file.deleteFile(Constantes.FILE_OUTPUT_JSON)

    print (" tiempo que paso " + str((time.clock() - t0)))