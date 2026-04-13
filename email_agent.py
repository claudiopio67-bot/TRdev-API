from app.services.email_service import send_email

def run(action: str, data: dict):
    if action == "send_email":
        return send_email(
            data["to"],
            data["subject"],
            data["body"]
        )
    return {"error": "action not supported"}
