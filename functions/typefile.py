def isCsv(file):
    """
    Check if a file has a CSV extension.

    Args:
        file (str): The name of the file.
    Returns:
        bool: True if the file has a CSV extension, False otherwise.
    """
    f = file.split('.')
    if f[1] == 'csv':
        return True

def isTxt(file):
    """
    Check if a file has a TXT extension.

    Args:
        file (str): The name of the file.
    Returns:
        bool: True if the file has a TXT extension, False otherwise.

    """
    f = file.split('.')
    if f[1] == 'txt':
        return True