def repair(schema, errors):
    if "Missing section: ui" in errors:
        schema["ui"] = {"pages": []}

    if "Missing section: api" in errors:
        schema["api"] = {"endpoints": []}

    if "Missing section: db" in errors:
        schema["db"] = {"tables": []}

    if "Missing section: auth" in errors:
        schema["auth"] = {"roles": ["admin", "user"]}

    if "Missing section: logic" in errors:
        schema["logic"] = {"rules": []}

    return schema