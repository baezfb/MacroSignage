from flask import Blueprint, render_template, url_for, redirect

from .models import Display

display = Blueprint('display', __name__, template_folder='templates', url_prefix='/display')


@display.before_app_first_request
def before_request():
    """
    Execute before request.
    """
    if Display.is_empty:
        Display.insert_default_displays()


@display.get('/')
def index():
    """
    Index page.
    """
    dsp = Display.query.filter_by(name='Default').first()
    dsp = dsp.public_key
    print(dsp)
    return redirect(url_for('.display_public_key', public_key=dsp))


@display.get('/<public_key>')
def display_public_key(public_key):
    """
    Get display by public key.

    Args:
        public_key: Public key of display.

    Returns:
        Display object.
    """
    dsp = Display.query.filter_by(public_key=public_key, active=True).first()
    if dsp is None:
        return redirect(url_for('.index'))
    return render_template('display/display.html', display=dsp)
