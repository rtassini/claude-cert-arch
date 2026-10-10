import anthropic

# Lê a chave da variável de ambiente ANTHROPIC_API_KEY automaticamente.
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[
        {"role":"user", "content":"cite ao 10 grupos mais populares de kpop"}
    ]
)

print(response.content[0].text)