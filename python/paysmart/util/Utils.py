

class Utils:
    
    def extractHeadersCsv(self, line):
        line = line.strip()
        line = line.replace('\n','')
        line = line.replace(' ','_')
        line = line.upper()
        return line