import json
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes, serialization

def encrypt_json(data: dict) -> bytes:
    # JSONni string holatga o‘tkazamiz
    json_data = json.dumps(data).encode()

    # Kalitni o‘qiymiz
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Shifrlaymiz
    encrypted = public_key.encrypt(
        json_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Misol uchun:
data = {"username": "bexruz", "access": "admin"}
encrypted_data = encrypt_json(data, "public_key.pem")


def decrypt_json(encrypted_bytes: bytes) -> dict:
    # Kalitni o‘qiymiz
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Deshifrlaymiz
    decrypted = private_key.decrypt(
        encrypted_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # JSON ga aylantiramiz
    return json.loads(decrypted.decode())

decrypted_data = decrypt_json(encrypted_bytes, "private_key.pem")
print("Ochilgan ma'lumot:", decrypted_data)

