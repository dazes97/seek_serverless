import os
import jwt
from jwt.exceptions import PyJWTError


class AuthService:
    def authenticate(self, email, password):
        if email == 'admin@gmail.com' and password == '12345678':
            secret = os.getenv('JWT_SECRET')
            if not secret:
                raise ValueError("JWT_SECRET environment variable is not set")
            try:
                token = jwt.encode({'email': email}, secret,
                                   algorithm='HS256')
                return token
            except PyJWTError as e:
                print(f"Error encoding JWT: {e}")
                return None
        else:
            return None
