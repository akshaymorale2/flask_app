import os

from social_app.social import create_app

"""
WSGI config for this project.

It exposes the WSGI callable as a module-level variable named ``social``.
"""

env = os.environ.get('APP_ENV')

if not env:
    raise Exception('APP_ENV not found.')

application = create_app(env)
