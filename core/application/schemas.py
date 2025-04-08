from pydantic import BaseModel


class SchemaSecret(BaseModel):
    secret: str
    passphrase: str | None = None
    ttl_seconds: int
