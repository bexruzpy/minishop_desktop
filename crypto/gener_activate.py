from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_data(data: str, private_key_path: str) -> bytes:
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    signature = private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Misol uchun foydalanuvchi CPU ID:
cpu_id = "BFEBFBFF000306A9"
signature = sign_data(cpu_id, "private_key.pem")

with open("license.sig", "wb") as f:
    f.write(signature)
