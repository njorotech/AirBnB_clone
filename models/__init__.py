#!/usr/bin/python3
"""models package.

The package contains the following models:
    base_model
    engine.file_storage
    engine.__init__
    user
    state
    city
    amenity
    place
    review
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
