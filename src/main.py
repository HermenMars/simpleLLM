from model_utils import load_model, generate_text

def main():
    tokenizer, model = load_model("gpt2")
    prompt = input("Enter a prompt: ")
    output = generate_text(tokenizer, model, prompt)
    print(f"Generated: {output}")

if __name__ == "__main__":
    main()
