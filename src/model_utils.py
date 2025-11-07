from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model(model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model

def generate_text(tokenizer, model, prompt, max_length=300, temperature=0.7, top_k=50, top_p=0.9):
    """
    Generate text from a prompt using sampling for better results.

    Args:
        tokenizer: Hugging Face tokenizer
        model: Hugging Face model
        prompt: input string
        max_length: maximum number of tokens to generate
        temperature: randomness (0.0–1.0)
        top_k: sample from top k tokens
        top_p: nucleus sampling (0.0–1.0)
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # If you have GPU, move model and inputs to GPU
    if torch.cuda.is_available():
        model = model.to("cuda")
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    outputs = model.generate(
        **inputs,
        max_length=max_length,
        do_sample=True,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        pad_token_id=tokenizer.eos_token_id
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

