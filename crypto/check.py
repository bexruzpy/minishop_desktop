from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature

def verify_signature(data: str, signature: bytes, public_key_path: str) -> bool:
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False

# CPU ID ni yana o‘qish (dastur ishga tushganda)
cpu_id = "BFEBFBFF000306A9"
with open("license.sig", "rb") as f:
    license_signature = f.read()

if verify_signature(cpu_id, license_signature, "public_key.pem"):
    print("✅ Aktivatsiya muvaffaqiyatli!")
else:
    print("❌ Aktivatsiya xato yoki soxta!")

