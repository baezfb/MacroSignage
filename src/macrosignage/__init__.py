from os import getcwd
from os.path import abspath, dirname, join

from flask import Flask, redirect, url_for

from .utils import create_instance_config
from .blueprints import blueprints
from .extensions import extensions

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

    app = Flask(__name__,
                template_folder='ui/templates',
                static_folder='ui/static',
                instance_relative_config=True,
                instance_path=instance_path)

    # Load default config
    app.config.from_pyfile(application_default_config_file)
    # Load instance config overriding default config
    app.config.from_pyfile(application_instance_config_file, silent=True)

    @app.before_first_request
    def before_first_request():
        """
        Execute before first request.
        """
        from .extensions import db
        db.create_all()

    @app.get('/')
    def index():
        return redirect(url_for('display.index'))

    # Register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Register extensions
    for extension in extensions:
        extension.init_app(app)

    return app
