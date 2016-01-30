import csv
import json

from util.Utils import Utils
from util.Constantes import Constantes

class CSVUtils:

    utilidades = Utils()

    def parseCsvToJson(self):
        file = open(Constantes.FILE_INPUT_CSV, 'r')
        jsonfile = open(Constantes.FILE_OUTPUT_JSON, 'w')

        cabeceras = ( self.utilidades.extractHeadersCsv(file.readline()).split(';'))

        reader = csv.DictReader(file, delimiter=';', fieldnames=cabeceras)
        for row in reader:
            jsonfile.write(json.dumps(row) + "\n")

        file.close()
        jsonfile.close()
