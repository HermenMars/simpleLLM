from model_utils import load_model, generate_text

def main():
    tokenizer, model = load_model("gpt2-large")
    prompt = input("Enter a prompt: ")
    output = generate_text(tokenizer, model, prompt, max_length=500)
    print(f"Generated: {output}")

if __name__ == "__main__":
    main()
