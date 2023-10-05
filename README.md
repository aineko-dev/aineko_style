# aineko_style

## A pylint checker for misc style conventions

We adopt the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) with some modifications. This pylint checker is intended to enforce those conventions.


### Installation
1. Install with pip:
`pip install aineko_style`
2. Once installed you can either run it directly from the command line:
`pylint --load-plugins=aineko_style.checker your_module.py`
or add it to the pylint configuration file. Example:
   * pyproject.toml:
        ```toml
        [tool.pylint.main]
        load-plugins = ["aineko_style.checker"]
        ```
   * pylintrc:
       ```ini
       [MAIN]
       load-plugins=aineko_style.checker
       ```


### Features
Warning Messages


| Message ID | Description                                                                | Message symbol           |
| ---------- | -------------------------------------------------------------------------- | ------------------------ |
| C0001      | Docstring contains types. Types should be part of the function definition. | docstring-contains-types |

### Style Conventions
#### C0001 docstring-contains-types
Yes:
```python
def message(index:int, content:str):
    """short description

    Args:
        index: The index of the message.
        content: The content of the message.
    """
    ...
```

No:
```python
def message(index:int, content:str):
    """short description

    Args:
        index (int): The index of the message.
        content (str): The content of the message.
    """
    ...
```
