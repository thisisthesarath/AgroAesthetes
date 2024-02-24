import openai

openai.api_key = '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'

def generate_value_addition_guide(vegetable):
    prompt = f"Generate value addition steps for {vegetable}."
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=200
    )
    return response.choices[0].text.strip()

vegetable = input("Enter the name of the vegetable for which you want to generate the value addition guide: ")

value_addition_guide = generate_value_addition_guide(vegetable)

print(f"\nValue Addition Guide for {vegetable}:")
print(value_addition_guide)