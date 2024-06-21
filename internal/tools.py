def parse_integrity_exc_msg(integrity_msg: str):
    return integrity_msg.split("\n")[1].replace("\"", "").split(":")[1].strip() \
        .replace("(", "").replace(")", "")
