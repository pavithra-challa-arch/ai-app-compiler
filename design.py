def design_system(intent):
    features = intent.get("features", [])

    entities = ["User"]

    if "contacts" in features:
        entities.append("Contact")

    if "payments" in features:
        entities.append("Payment")

    if "analytics" in features:
        entities.append("Analytics")

    return {
        "entities": entities,
        "roles": intent.get("roles", []),
        "flows": ["authentication_flow", "dashboard_flow"]
    }