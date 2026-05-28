def extract_intent(prompt: str):
    prompt_lower = prompt.lower()

    intent = {
        "raw_prompt": prompt,
        "app_type": "crm" if "crm" in prompt_lower else "generic",
        "features": [],
        "roles": ["admin", "user"]
    }

    keywords = ["login", "dashboard", "contacts", "payments", "analytics", "roles"]

    for word in keywords:
        if word in prompt_lower:
            intent["features"].append(word)

    return intent