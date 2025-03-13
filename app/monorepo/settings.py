"""App configurations."""

from pydantic import computed_field, PostgresDsn
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database settings for the project.

    Attributes:
        NAME: Name of the database.
        HOST: Hostname of the database.
        USER: Username of the database.
        PASS: Password of the database.
        PORT: Port number of the database.
    """

    model_config = SettingsConfigDict(env_prefix="_")

    NAME: str
    HOST: str
    USER: str
    PASS: str
    PORT: int

    @computed_field
    def db_url(self) -> PostgresDsn:
        """Generate database URL.

        Returns:
                Database URL.
        """
        return MultiHostUrl.build(  # type: ignore
            scheme="postgresql+asyncpg",
            username=self.USER,
            password=self.PASS,
            host=self.HOST,
            path=self.NAME,
            port=self.PORT,
        )


class Settings(BaseSettings):
    """Settings for the project."""

    model_config = SettingsConfigDict(env_nested_delimiter="__")

    DB: DatabaseSettings


settings: Settings = Settings()
