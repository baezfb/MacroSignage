def generate_token(length: int = 32):
    """
    Generate a random token.

    Args:
        length (int): Length of token.

    Returns:
        str: Random token.
    """
    from secrets import token_urlsafe
    return token_urlsafe(length)


def create_dir(path: str):
    """
    Create a directory if it doesn't exist.

    Args:
        path(str): Path to directory.

    Returns:
        None
    """
    from os import makedirs
    from os.path import exists
    try:
        if not exists(path):
            makedirs(path)
    except FileExistsError:
        pass


def create_file(path: str):
    """
    Create a file if it doesn't exist.

    Args:
        path (str): Path to file.

    Returns:
        None
    """
    from os.path import exists
    try:
        if not exists(path):
            open(path, 'a').close()
    except FileExistsError:
        pass


def create_instance_config(instance_path: str):
    """
    Create instance config file if it doesn't exist.

    Args:
        instance_path (str): Path to instance.

    Returns:
        None
    """
    from os.path import join, exists
    instance_config_file = join(instance_path, 'config.py')
    instance_init_file = join(instance_path, '__init__.py')
    try:
        if not exists(instance_config_file):
            create_dir(instance_path)
            create_file(instance_config_file)
            create_file(instance_init_file)
    except FileExistsError:
        pass
