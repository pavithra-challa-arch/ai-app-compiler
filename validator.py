def validate(schema):
    errors = []

    required = ["ui", "api", "db", "auth", "logic"]

    for r in required:
        if r not in schema:
            errors.append(f"Missing section: {r}")

    return errors