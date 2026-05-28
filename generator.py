def generate_schema(design):
    entities = design.get("entities", [])
    roles = design.get("roles", [])

    db_tables = []
    for e in entities:
        db_tables.append({"name": e, "fields": ["id", "created_at"]})

    return {
        "ui": {"pages": ["Login", "Dashboard"]},
        "api": {"endpoints": ["/login", "/users"]},
        "db": {"tables": db_tables},
        "auth": {
            "roles": roles,
            "permissions": {
                "admin": ["create", "read", "update", "delete"],
                "user": ["read"]
            }
        },
        "logic": {
            "rules": ["role_based_access_control"]
        }
    }