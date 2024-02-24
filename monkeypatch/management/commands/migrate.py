# app/management/commands/migrate.py

"""
Override of Django migrate. When we use this version, we
will load the __init__ file above that patches models.Field.
"""

from django.core.management.commands.migrate import Command  # noqa
