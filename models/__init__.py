#!/usr/bin/python3
"""
This module initializes the models package.

It sets up the FileStorage instance for the application and reloads any
previously saved data to ensure persistence across sessions.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
