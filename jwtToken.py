import jwt
import datetime
import secrets

# Chave secreta para assinar o token (substitua por uma chave forte em produção)
secret_key = '29c089a81652ea60d331cc1cc2c21b05c88bbe8c250343f0641a85f6fba0ff23'

# Informações para incluir no payload do token
payload = {
    'sub': 'anzolim',  # Identificador do usuário
    'iat': datetime.datetime.utcnow(),  # Timestamp de quando o token foi emitido
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Timestamp de expiração (1 dia)
}

# Gera o token JWT
token = jwt.encode(payload, secret_key, algorithm='HS256')

print(token)
