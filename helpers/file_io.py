from os import path
from typing import Union, Any

from ruamel import yaml

from helpers.paths import EXPECTED


def read_yaml_file(file_path: str) -> dict:
    """Read the contents of a yaml file.

    Args:
        file_path: The full path to the file to read.

    Returns:
        A dictionary of values from the yaml file.

    """
    with open(file_path, 'r', encoding='utf-8') as yaml_file:
        return yaml.safe_load(yaml_file)


def get_the_expected_text(
        file_name: str, language: str, main_node: str = None,
        second_node: str = None) -> Union[str, dict, None]:
    """Get the expected text from the expected text yaml file.

        Args:
            file_name: File name of the yaml file.
            language: Localised Language.
            main_node: The main node of the yaml file.
            second_node: Second node that returns the expected value
                required (a string).

        Example:
            yaml_file_name = 'expected_text.yaml'
            file.get_expected_text(file_name=yaml_file_name ,
                                   main_node='plan_a_journey',
                                   language='en-uk',
                                   second_node='to_text_alert')

        Return:
            The expected text of the given nodes as a string or dict
            containing the keys ad values.

    """
    expected_nodes_dict = read_yaml_file(path.join(EXPECTED, file_name))
    if second_node is not None:
        return expected_nodes_dict[language][main_node][second_node]
    else:
        return expected_nodes_dict[language][main_node]
