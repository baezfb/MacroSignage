from flask import Blueprint, render_template, url_for, redirect

display = Blueprint('display', __name__, template_folder='templates', url_prefix='/display')


@display.get('/<public_key>')
def display_public_key(public_key):
    return render_template('display/display.html', public_key=public_key)
