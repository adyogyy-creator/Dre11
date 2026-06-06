import os
import time

WALLET = "prl1pxr5p479hr7qsmn6n8y5qz66tzhc9n32y5vcajf0nt6tdes3as4eqsxzms0"
WORKER = "modal-h100"
HOST = "pool.example.com"
PORT = "443"
USE_TLS = "1"

def get_env():
    return {
        "AKOYA_POOL_WALLET": WALLET,
        "AKOYA_POOL_WORKER": WORKER,
        "AKOYA_POOL_HOST": HOST,
        "AKOYA_POOL_PORT": PORT,
        "AKOYA_POOL_USE_TLS": USE_TLS,
    }

def main():
    env = get_env()
    for k, v in env.items():
        os.environ[k] = v
    print("ready")
    time.sleep(2)

if __name__ == "__main__":
    main()
