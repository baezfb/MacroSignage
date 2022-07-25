from ...extensions import db
from ...utils.sql import SQLMixin
from ...utils import generate_token


class Display(db.Model, SQLMixin):
    """
    Display Model.

    Args:
        db.Model: SQLAlchemy model class.

    Returns:
        None
    """
    public_key = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=True)

    def get_default(self):
        """
        Get default display.

        Args:
            None

        Returns:
            Display object.
        """
        return self.query.filter_by(name='default').first()

    def get_by_public_key(self, public_key):
        """
        Get display by public key.

        Args:
            public_key: Public key of display.

        Returns:
            Display object.
        """
        return self.query.filter_by(public_key=public_key).first()

    @staticmethod
    def insert_default_displays():
        """
        Insert default displays.

        Args:
            None

        Returns:
            None
        """
        displays = [
            {
                'name': 'Default',
                'description': 'Default display.',
            },
            {
                'name': 'Default 2',
                'description': 'Default display 2.',
            },
        ]
        for display in displays:
            Display(**display).save()

    def is_empty(self):
        """
        Check if display is empty.

        Args:
            None

        Returns:
            True if display is empty, False otherwise.
        """
        return self.public_key is None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if self.public_key is None:
            self.public_key = generate_token()
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
