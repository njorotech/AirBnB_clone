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

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
