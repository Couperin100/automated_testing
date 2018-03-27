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


def dictionary_lookup(
        dictionary: dict, main_node: str,
        *secondary_nodes: Union[str, list, None]) -> Any:
    """Recursive dictionary node lookup function.

    Function can go as many nested nodes into the given dictionary as the given
    number of secondary node arguments you specified. If the node you've
    supplied doesnt exist then will return ``None``.

    """
    if secondary_nodes:
        return dictionary_lookup(dictionary.get(main_node), *secondary_nodes)
    return dictionary.get(main_node)


def get_the_expected_text(
        file_name: str, main_node: str,
        secondary_nodes: Union[str, list, None]) -> Union[str, dict, None]:
    """Get the expected text from the expected text yaml file.

    If your given yaml file has more than 2 nested nodes then you will need to
    use a list containing the nodes as strings to the secondary_nodes parameter
    (see example 2 below)

        Args:
            file_name: File name of the yaml file.
            main_node: The main node of the yaml file.
            secondary_nodes: Additional nodes that return the expected value
                required (can be a string or a list).

        Example:
            yaml_file_name = 'tfl_expected_text.yaml'
            file.get_expected_text(file_name=yaml_file_name ,
                                   node='plan_a_journey',
                                   nodes='to_text_alert')

        Example 2:
            yaml_file_name = 'tfl_expected_text.yaml'
            file.get_expected_text(
                file_name=yaml_file_name, node='plan_a_journey',
                nodes=['to_text_alert','another_nested_node'])

        Return:
            The expected text of the given nodes as a string.

    """
    expected_nodes_dict = read_yaml_file(path.join(EXPECTED, file_name))
    if isinstance(secondary_nodes, str):
        secondary_nodes = [secondary_nodes]  # make string into a list.
    return dictionary_lookup(expected_nodes_dict, main_node, *secondary_nodes)
