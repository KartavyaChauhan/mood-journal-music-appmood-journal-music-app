from transformers import pipeline

# Load once at module level
generator = pipeline("text-generation", model="gpt2")

def get_affirmation(mood):
    prompt = f"Give a short and calming affirmation for someone who is feeling {mood}. Limit to one or two sentences."

    try:
        result = generator(prompt, max_length=40, do_sample=True, temperature=0.7)
        return result[0]["generated_text"].replace(prompt, "").strip()
    except Exception as e:
        return f"Affirmation generation failed: {e}"
