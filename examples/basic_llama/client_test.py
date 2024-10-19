import ollama

# client = Client(host='http://localhost:11434')
ollama_client = ollama.Client(host="http://0.0.0.0:11434")
# print(ollama_client)
print(ollama_client.generate(model="qwen2.5:14b", prompt="Translate the following English text to Spanish: 'Hello'"))