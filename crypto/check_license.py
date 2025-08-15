# app.py
import json, base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def verify_license():
    # Public key yuklash
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Litsenziya faylini o‘qish
    with open("license.key", "r") as f:
        license_file = json.load(f)

    data = base64.b64decode(license_file["data"])
    signature = base64.b64decode(license_file["signature"])

    try:
        # Imzoni tekshirish
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("✅ Litsenziya to‘g‘ri, dasturni ishlatish mumkin")
        print("📄 Litsenziya ma’lumotlari:", json.loads(data))
        return True
    except Exception:
        print("❌ Litsenziya noto‘g‘ri yoki buzilgan!")
        return False

if __name__ == "__main__":
    verify_license()
