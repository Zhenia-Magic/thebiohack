import os
from datetime import datetime, timedelta
from enum import Enum
from typing import Union, Any, Optional

from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']   # should be kept secret
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']    # should be kept secret


class AuthMode(Enum):
    ACCESS = 'access'
    REFRESH = 'refresh'

    def get_expire_minutes(self):
        if self.name == AuthMode.ACCESS.name:
            return ACCESS_TOKEN_EXPIRE_MINUTES
        else:
            return REFRESH_TOKEN_EXPIRE_MINUTES


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    return get_encoded_jwt(subject, expires_delta, AuthMode.ACCESS)


def create_refresh_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    return get_encoded_jwt(subject, expires_delta, AuthMode.REFRESH)


def get_encoded_jwt(subject: Union[str, Any], expires_delta: Optional[timedelta], mode: AuthMode):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=mode.get_expire_minutes())
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt
