import jwt


secretKey = "MekuSucks"
encoded_jwt = jwt.encode({'some': 'payload'},secretKey, algorithm='HS256')
print(encoded_jwt)
decocded_jwt = jwt.decode(encoded_jwt,secretKey,algorithms=['HS256'])
print(decocded_jwt)