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
