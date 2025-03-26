from pydantic import BaseModel


class User(BaseModel):
    """
    Description: User model

    Args: None

    Returns: None
    """
    username: str
    email: str
    password: str


class Item(BaseModel):
    """
    Description: Item model

    Args: None

    Returns: None
    """
    name: str
    description: str
    price: float
