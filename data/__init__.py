import json
from os import path

_ROOT = path.abspath(path.join(__file__) + '/..')


def _load_file(name):
    """
    :param name: str - the name of loaded dataset
    :return: Dict[str, int]
    """
    with open(_ROOT + '/FUN-dataset/' + name + '.json') as f:
        return json.load(f)


def load_test():
    """
    :return: Dict[str, int]
    """
    return _load_file('test')


def load_train():
    """
    :return: Dict[str, int]
    """
    return _load_file('train')


def load_fun_dataset():
    """
    :return: Dict[str, int]
    """
    fun = load_test()
    fun.update(load_train())
    return fun


def load_gold():
    """
    :return: Dict[str, int]
    """
    return _load_file('assessed')
