from os import environ


class Config:
    REPOSITORY = environ.get("REPOSITORY", "IN_MEMORY")
