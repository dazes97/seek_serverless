import os
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError


class AuthorizerService:

    def authorize(self, token: str):
        try:
            private_key = os.getenv("JWT_SECRET")
            if not private_key:
                raise ValueError("JWT_SECRET environment variable is not set")

            decoded_token = jwt.decode(
                token, private_key, algorithms=["HS256"])
            print(f"Decoded token: {decoded_token}")

            return self._generate_policy("Allow")

        except ExpiredSignatureError:
            print("Token has expired")
            return self._generate_policy("Deny", "Token has expired")

        except InvalidTokenError:
            print("Invalid token")
            return self._generate_policy("Deny", "Invalid token")

        except Exception as e:
            print(f"Error occurred while authorizing: {e}")
            return self._generate_policy("Deny", str(e))

    def _generate_policy(self, effect: str, message: str = None):
        policy = {
            "principalId": "user",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "execute-api:Invoke",
                        "Effect": effect,
                        "Resource": "*"
                    }
                ]
            }
        }
        if message:
            policy["context"] = {"message": message}
        return policy
