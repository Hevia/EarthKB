def loadFile(file_path: str) -> str:
    """
    Loads the file at a specificed path, returns an error otherwise
    
    :param file_path (str): The path to the file you want to load
    :return _file a str of the contents of the file
    """
    try:
        _file = ""
        with open(file_path, "r") as fp:
            _file = fp.read()
        return _file
    except Exception:
        raise Exception(f"Error reading file at: {file_path}")