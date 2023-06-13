def wUpper(name):
    output=name[0].upper()
    output+=name[1:len(name)].lower()
    return output

def IsCsv(file):
    f = file.split('.')
    if f[1] == 'csv':
        return True

def IsTxt(file):
    f = file.split('.')
    if f[1] == 'txt':
        return True
