import os
import pickle
from scikg_types.DocumentTypes import TextFile


def loadTextFilesBulk(dir_path: str) -> list[TextFile]:
    textFiles: list[TextFile] = []
    try:
        for _, _, file_names in os.walk(dir_path):
            for file_name in file_names:
                textFiles.append(
                    {
                        "file_id": file_name,
                        "file_content": loadFile(f"{dir_path}/{file_name}"),
                    }
                )
    except Exception as e:
        # TODO logging
        print(e)

    return textFiles


def loadFile(file_path: str) -> str:
    """
    Loads the file at a specificed path, returns an error otherwise

    :param file_path (str): The path to the file you want to load
    :return _file a str of the contents of the file
    """
    try:
        _file = ""
        with open(file_path, "r", encoding="utf-8") as fp:
            _file = fp.read()
        return _file
    except Exception as e:
        raise Exception(f"Error: {e} file at: {file_path}")


def loadFileAsLines(file_path: str) -> list[str]:
    """
    Loads a \n separated text file at a specificed path, returns an error otherwise

    :param file_path (str): The path to the file you want to load
    :return _file a list[str] separated by \n
    """
    try:
        _file = ""
        with open(file_path, "r", encoding="utf-8") as fp:
            _file = fp.readlines()
        return _file
    except Exception as e:
        raise Exception(f"Error: {e} reading file at: {file_path}")


def saveTextFile(data, save_path) -> None:
    try:
        with open(save_path, "w+", encoding="utf-8") as fp:
            fp.write(data)
    except Exception:
        raise Exception(f"Error with trying to save file at: {save_path}")


def savePickle(data, save_path) -> None:
    try:
        with open(save_path, "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        raise Exception(f"Error: {e} with trying to save pickle at: {save_path}")


def loadPickle(load_path) -> None:
    try:
        with open(load_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise Exception(f"Error: {e} with trying to load pickle at: {load_path}")
