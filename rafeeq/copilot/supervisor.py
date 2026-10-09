from rafeeq.samples import load_sample

def handle_message(room_id: str, text: str, file_id: str | None = None) -> dict:
    return load_sample("copilot_reply")