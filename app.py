import os
import requests

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

from whatsapp_rag import ask_whatsapp_rag


app = FastAPI()


VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


# --------------------------------------------------
# Meta webhook verification
# --------------------------------------------------

@app.get("/webhook")
async def verify_webhook(request: Request):

    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Verification failed", status_code=403)


# --------------------------------------------------
# Receive WhatsApp messages
# --------------------------------------------------

@app.post("/webhook")
async def receive_message(request: Request):

    data = await request.json()

    try:

        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]

        messages = value.get("messages")

        if not messages:
            return {"status": "no message"}

        message = messages[0]

        # We only handle text messages
        if message.get("type") != "text":
            return {"status": "ignored"}

        user_phone = message["from"]
        user_text = message["text"]["body"]

        print("User:", user_phone)
        print("Message:", user_text)

        # Run your RAG
        answer = ask_whatsapp_rag(user_text)

        print("Answer:", answer)

        # Send answer back
        send_whatsapp_message(user_phone, answer)

    except Exception as e:

        print("Webhook error:", e)

    return {"status": "ok"}


# --------------------------------------------------
# Send WhatsApp message
# --------------------------------------------------

def send_whatsapp_message(to: str, message: str):

    url = (
        f"https://graph.facebook.com/"
        f"v25.0/{PHONE_NUMBER_ID}/messages"
    )

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print("Meta response:", response.status_code)
    print(response.text)


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def health():

    return {
        "status": "running",
        "service": "WhatsApp RAG bot"
    }
