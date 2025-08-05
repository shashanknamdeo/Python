# pip install cryptography


from cryptography.fernet import Fernet

# Step 1: Generate a key (you need to keep this secret and safe)
key = Fernet.generate_key()
fernet = Fernet(key)

# Step 2: Encrypt the string
plain_text = "Hello, this is a secret!"
encrypted = fernet.encrypt(plain_text.encode())

# Step 3: Decrypt it back
decrypted = fernet.decrypt(encrypted).decode()


