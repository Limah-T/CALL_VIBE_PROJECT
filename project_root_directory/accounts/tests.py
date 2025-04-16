from django.test import TestCase

# Create your tests here.
import jwt

encode = jwt.encode(payload={"some": "payload"}, key="secret123", algorithm="HS256")
print(encode)
decode = jwt.decode(jwt=encode, key="secret123", algorithms="HS256")
print(decode)
