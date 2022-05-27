#!/usr/bin/python3

from collections import OrderedDict
from yaml import SafeLoader as YamlSafeLoader


KEY_MAPPING = {
    "applications": "app",
    "database": "db",
    "virtualization": "vt"
}

DEFAULT_MAPPING_TAG = 'tag:yaml.org,2002:map'

def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))


YamlSafeLoader.add_constructor(DEFAULT_MAPPING_TAG, dict_constructor)


def load_yaml(stream):
    loader = YamlSafeLoader(stream)
    try:
        return loader.get_single_data()
    finally:
        loader.dispose()


def load_config(file_name):
    with open(file_name, 'r') as stream:
        return load_yaml(stream)


from collections.abc import MutableMapping

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        k = k.lower()
        k = KEY_MAPPING.get(k, k)
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def __main__():
    menu = load_config('ctx.yml')
    for k, v in flatten_dict(menu).items():
        print("-",k)


if __name__ == "__main__":
    __main__()
