from os import getcwd
from os.path import abspath, dirname, join

from flask import Flask

from .utils import create_instance_config

# Current working directory
cwd = getcwd()
# Current application directory
cad = abspath(dirname(__file__))


def macro_signage_app(instance_path=None):
    """
    Create a new instance of the Macro Signage application.

    Args:
        instance_path: Path to instance.

    Returns:
        Flask application.
    """

    # set the instance path
    if instance_path is None:
        instance_path = join(cwd, 'instance')

    # Create instance config file if it doesn't exist
    create_instance_config(instance_path)

    # Default config file
    application_default_config_file = join(cad, 'config.py')
    # Instance config file
    application_instance_config_file = join(cwd, 'instance', 'config.py')

    app = Flask(__name__, instance_relative_config=True, instance_path=instance_path)

    # Load default config
    app.config.from_pyfile(application_default_config_file)
    # Load instance config overriding default config
    app.config.from_pyfile(application_instance_config_file, silent=True)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
