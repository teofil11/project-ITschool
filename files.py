import csv


class File():
    def __init__(self,name,path):
        self.path = path
        self.name = name
        self.rows = []
    def read_file(self):
        pass


class File_csv(File):
    def __init__(self,path,name):
        super().__init__(name,path)
    def read_file(self):
        with open(self.path + self.name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.rows.append(row)
        return self.rows
    

class File_txt(File):
    def __init__(self,path,name):
        super().__init__(name,path)
        
    def read_file(self):
        with open(self.path + self.name, 'r') as file:
            content = (file.readlines())
            for row in content:
                self.rows.append(row)
        return self.rows

