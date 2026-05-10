import hashlib
import sys

def generate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hash_generator.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        hash_value = generate_sha256(file_path)
        print("\nSHA256:")
        print(hash_value)

    except FileNotFoundError:
        print("File not found.")
