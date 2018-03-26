from ruamel import yaml


def read_yaml_file(file_path: str) -> dict:
    """Read the contents of a yaml file.

    Args:
        file_path: The full path to the file to read.

    Returns:
        A dictionary of values from the yaml file.

    """
    with open(file_path, 'r', encoding='utf-8') as yaml_file:
        return yaml.safe_load(yaml_file)