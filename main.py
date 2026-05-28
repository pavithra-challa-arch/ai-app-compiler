from intent import extract_intent
from design import design_system
from generator import generate_schema
from validator import validate
from repair import repair


def run_pipeline(prompt: str):
    intent = extract_intent(prompt)
    design = design_system(intent)
    schema = generate_schema(design)

    errors = validate(schema)

    if errors:
        schema = repair(schema, errors)

    return schema


if __name__ == "__main__":
    user_prompt = input("Enter your requirement: ")
    result = run_pipeline(user_prompt)
    print(result)