from typing import Optional

from pydantic import BaseModel


class Repository(BaseModel):
    """The class represents the Repository data object."""

    name: str
    full_name: str
    description: Optional[str]
    forks_count: int
    stars_count: int
    default_branch: Optional[str]
    ssh_url: str
    http_url: str
    created_at: str
    updated_at: Optional[str]
