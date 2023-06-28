def isCsv(file):
    f = file.split('.')
    if f[1] == 'csv':
        return True

def isTxt(file):
    f = file.split('.')
    if f[1] == 'txt':
        return True