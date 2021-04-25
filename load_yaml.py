import sys
import logging
import yaml

def load_yaml(yml_file):
    """ Load content of a yaml file
    Args:
        yml_file(str): Name of the yaml file
    Returns:
        dict: content of the yaml file
    """

    with open(yml_file,'r') as yamlfile:
        try:
            data = yaml.safe_load(yamlfile)
        except yaml.YAMLERROR as exc:
            loggigng.error(exc)
            sys.exit(0)
        except fileNotFoundError as exc:
            logging.error(exc)
            sys.exit(0)
    return data 