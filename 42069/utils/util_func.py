import os
import json
import dotenv


def env(variable: str, to_int: bool = False):
    result: str = os.environ.get(variable, "")
    if to_int and isinstance(result, str):
        return int(result)
    assert result is not None, f"Environment variable '{variable}' not exist"
    return result


def load_env(path="./", name=""):
    dotenv.load_dotenv(os.path.join(os.path.dirname(path), f'{name}.env'))


def load_conf(dir="./", name="", type="json"):
    if type == "json":
        with open(os.path.join(os.path.dirname(dir), f'{name}'), 'r') as f:
            return json.load(f)
