import random

class Generator:
    def generate(self):
        tags = {
            "8": "FIX.4.2",
            "35": "D",
            "55": random.choice(["AAPL", "GOOG", "MSFT", "AMZN"]),
            "54": random.choice(["1", "2"]),
            "38": str(random.randint(1, 100)),
            "40": "1",
        }
        msg = "|".join(f"{k}={v}" for k, v in tags.items())
        checksum = sum(ord(c) for c in msg) % 256
        msg += f"|10={checksum:03}"
        return msg