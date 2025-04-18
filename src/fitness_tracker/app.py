from importlib import import_module
from typing import Dict, Type, Any
import json
from fitness_tracker.settings.settings import Constants


def load_module_config(config_path) -> dict[Any, tuple]:
    """
    Load module configuration from JSON file.
    Configurations are mapped to (module_path, class_name)
    tuples.

    :param config_path: Path to JSON file.
    :return: Dictionary with module configuration.
    """
    try:
        with config_path.open("r") as file:
            data = json.load(file)
            for key, value in data.items():
                if not isinstance(value, list) or len(value) != 2:
                    raise ValueError(
                        f"Invalid config entry for {key}: expected "
                        "[module_path, class_name]"
                        )
        return {key: tuple(value) for key, value in data.items()}
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Module config file not found at {config_path}"
        )
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON config file at {config_path}: {e}")


def initialise() -> Dict[str, Type[Any]]:
    """
    Builds application module component dictionary.

    :return: Dictionary of module components.
    """
    module_config = load_module_config(Constants.CONFIG_PATH)
    components = {}
    for key, (module_path, class_name) in (module_config.items()):
        try:
            module = import_module(module_path)
            attr = getattr(module, class_name)
            if not isinstance(attr, type):
                raise ValueError(
                    f"{class_name} in {module_path} is not a class"
                )
            components[key] = attr
        except ImportError as e:
            raise ImportError(f"Failed to import {module_path}: {e}")
        except AttributeError as e:
            raise AttributeError(
                f"Attribute {class_name} not found in {module_path}: {e}"
            )
    return components
