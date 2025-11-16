class FixParser:
    REQUIRED_TAGS = {
        "D": {"55", "54", "38"},
        "S": {"55", "132", "133"},
    }

    def parse(self, msg: str) -> dict:
        if not msg:
            raise ValueError("Empty FIX message")

        fields = msg.split('|')
        parsed = {}

        for field in fields:
            if '=' not in field:
                print(fields)
                raise ValueError(f"Malformed field: {field}")
            key, value = field.split('=', 1)
            parsed[key] = value

        msg_type = parsed.get("35")
        if msg_type is None:
            raise ValueError("Missing required tag 35 (MsgType)")

        required = self.REQUIRED_TAGS.get(msg_type, set())
        for tag in required:
            if tag not in parsed:
                raise ValueError(f"Missing required tag {tag} for MsgType={msg_type}")

        return parsed
