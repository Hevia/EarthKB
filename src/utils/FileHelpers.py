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

def loadFileAsLines(file_path: str) -> list[str]:
    """
    Loads a \n separated text file at a specificed path, returns an error otherwise
    
    :param file_path (str): The path to the file you want to load
    :return _file a list[str] separated by \n
    """
    try:
        _file = ""
        with open(file_path, "r") as fp:
            _file = fp.readlines()
        return _file
    except Exception:
        raise Exception(f"Error reading file at: {file_path}")

def saveFile(data, save_path) -> None:
    try:
        with open(save_path, "w+", encoding="utf-8") as fp:
            fp.write(data)
    except Exception:
        raise Exception(f"Error with trying to save file at: {save_path}")