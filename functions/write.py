def wUpper(name):
    """
    Convert the first letter of a name to uppercase and the remaining letters to lowercase.

    Args:
        name (str): The name to be processed.
    Returns:
        str: The processed name with the first letter uppercase and the remaining letters lowercase.
    """
    output=name[0].upper()
    output+=name[1:len(name)].lower()
    return output