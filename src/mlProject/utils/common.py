import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject.logging import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Read a YAML file and convert it into a ConfigBox.
    Args: path_to_yaml(str):path like input

    Raises: 
        ValueError: if the yaml is empty
        e:empty yaml
    Returns:
    ConfigBox: a ConfigBox object with the yaml content
    """
    try:
        with open(path_to_yaml, 'r') as file:
            yaml_content = yaml.safe_load(file)
            logger.info(f" yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(yaml_content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """
    Create directories based on the list of paths.
    Args:
        path_to_json(list): list of paths like input
        verbose(bool): if True, print the created directories

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory: {path} created successfully")

@ensure_annotations
def load_json(path:Path):
    """
    load json files data

    Args: 
    path(Path): path to Json file

    returns:
    ConfigBox: data as class attributes instead of dict
    
    """

    with open(path, 'r') as file:
        json_data = json.load(file) # return python dictionary format
        logger.info(f"Json file: {path} loaded successfully")

        return ConfigBox(json_data)
    
@ensure_annotations
def get_size(path:Path):
    """
    get size in KB

    Args:
    path(Path): path of the file

    Returns:
      str: size in KB
    """

    size_in_kb=round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} KB"