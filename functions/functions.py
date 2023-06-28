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

def format_file(file_name,content):
    lines = []
    if IsCsv(file_name) is True:
        for line in content:
            cleaned_row = [item.replace("T", " ").replace("Z", "") for item in line]
            lines.append(cleaned_row)
        return lines
    if IsTxt(file_name) is True:
        for line in content:
            cleaned_row = line.rstrip(";\n ").replace('T', " ").replace('Z', '')
            lines.append(cleaned_row)
        return lines