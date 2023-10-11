#!/usr/bin/python3
"""Define all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    """Define all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes objects of BaseModel class"""

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self.to_dict())
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """string representation of Basemodel objects"""

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the updated_at with the current datetime"""

        storage.save()
        self.updated_at = datetime.now()
        #storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of
        __dict__ of the instance
        """

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict
