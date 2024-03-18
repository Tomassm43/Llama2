from llama_cpp import Llama


model_path = "**path to the GGUF file**"
model = Llama(model_path=model_path)
system_message = "You are a helpful assistant"
user_message = "Generate a list of 5 funny dog names"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

max_tokens = 100

output = model(prompt, max_tokens=max_tokens, echo=True)

print(output)