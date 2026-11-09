import re


# Blocklist of common Prompt Injection / Jailbreaking patterns
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous\s+)?instructions",
    r"forget\s+(all\s+)?(previous\s+)?rules",
    r"you\s+are\s+now\s+dan",
    r"reveal\s+(the\s+)?system\s+prompt",
    r"print\s+(the\s+)?api\s*key",
    r"disregard\s+(all\s+)?rules",
]

def mask_pii(text: str) -> str:
    """
    Masks sensitive personal data (phone numbers and emails) from user text.
    """
    # 1. Mask Phone Numbers
    phone_pattern = r"\b(?:\+?91[-.\s]?)?[6-9]\d{9}\b|\b\d{10}\b"
    sanitized = re.sub(phone_pattern, "[REDACTED_PHONE]", text)

    # 2. Mask Emails
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    sanitized = re.sub(email_pattern, "[REDACTED_EMAIL]", sanitized)

    return sanitized


def is_prompt_injection(text: str) -> bool:
    """
    Detects whether the user query contains prompt injection or jailbreak attempts.
    Returns True if malicious, False if safe.
    """
    text_lower = text.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def secure_user_input(text: str) -> dict:
    """
    Security Gatekeeper:
    - Checks for injection attacks: blocks request if malicious.
    - Masks PII (phone, email): sanitizes text before sending to LLM.
    """
    if is_prompt_injection(text):
        return {"allowed": False, "sanitized_text": "", "reason": "Prompt injection detected and blocked 🛡️"}
    
    clean_text = mask_pii(text)
    return {"allowed": True, "sanitized_text": clean_text, "reason": "Safe ✅"}

