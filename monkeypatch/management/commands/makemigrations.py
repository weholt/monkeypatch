# app/management/commands/makemigrations.py

"""
Override of Django makemigrations. When we use this version, we
will load the __init__ file above that patches models.Field.
"""

from django.core.management.commands.makemigrations import Command  # noqa
