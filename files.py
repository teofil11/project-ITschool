import csv
import subprocess


class File():
    """
    Represents a file.

    Attributes:
        path (str): The path to the file.
        name (str): The name of the file.
        rows (list): A list to store the rows of the file.

    """
    def __init__(self,name,path):
        """
        Initializes a File object.

        Args:
            name (str): The name of the file.
            path (str): The path to the file.

        """
        self.path = path
        self.name = name
        self.rows = []

    def read_file(self):
        subprocess.check_call(["attrib", "-H", self.path])


class File_csv(File):
    def __init__(self,path,name):
        super().__init__(name,path)

    def read_file(self):
        """
        Reads the contents of the CSV file.

        Returns:
            list: A list containing the rows of the CSV file.

        """
        super().read_file()
        with open(self.path + self.name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.rows.append(row)
        return self.rows
    

class File_txt(File):
    def __init__(self,path,name):
        super().__init__(name,path)
        
    def read_file(self):
        """
        Reads the contents of the text file.

        Returns:
            list: A list containing the lines of the text file.

        """
        super().read_file()
        with open(self.path + self.name, 'r') as file:
            content = (file.readlines())
            for row in content:
                self.rows.append(row)
        return self.rows

