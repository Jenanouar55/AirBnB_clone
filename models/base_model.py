import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instance attributes.
        If kwargs is provided, set instance attributes from them.
        Otherwise, generate a new ID and set creation and update timestamps.
        """
        if kwargs:
            self._set_attributes_from_kwargs(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def _set_attributes_from_kwargs(self, kwargs):
        """Sets instance attributes keyword arguments `kwargs`."""
        for key, value in kwargs.items():
            if key != "__class__":
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        """
        Returns an informal string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` timestamp.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dictionary containing all values of the instance's `__dict__`,
        along with the class name and ISO formatted datetime strings.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.update_at.isoformat()
        return dictionary
