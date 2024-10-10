from sqlmodel import Field, SQLModel
from typing import Optional

class retrovideogame(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    developer: str
    year_of_release: int
    genre: str
    platform: str
    rating: Optional[float] = Field(default=None, ge=0.0, le=10.0)
    description: Optional[str] = Field(default=None, max_length=500)