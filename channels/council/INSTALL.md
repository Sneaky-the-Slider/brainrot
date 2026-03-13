# 🗣️ Council Installation Guide

## Quick Install (Recommended)

```bash
cd channels/council
./quickstart.sh
```

That's it! The script will:
1. Check Python 3 is installed
2. Install `google-generativeai` and `rich` if needed
3. Prompt for your API key if not set
4. Launch the council with chaos mode enabled

## Manual Install

### 1. Install Dependencies

```bash
pip install google-generativeai rich
```

### 2. Get Google AI API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Set it as environment variable:

```bash
export GOOGLE_API_KEY="your-key-here"
```

Or add to your `~/.bashrc` or `~/.zshrc`:

```bash
echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Run

```bash
python council.py

# With chaos agent
python council.py --chaos

# Deliberate mode
python council.py --deliberate --chaos
```

## From Project Root

```bash
make council
```

## Verify Installation

```bash
python3 -c "import google.generativeai; import rich; print('✅ All good!')"
```

## Troubleshooting

### "No module named 'google.generativeai'"

```bash
pip install google-generativeai
```

### "No API key provided"

Set the environment variable:

```bash
export GOOGLE_API_KEY="your-key-here"
```

Or pass inline:

```bash
python council.py --api-key "your-key-here"
```

### Rate limiting

Google AI has free tier limits. If you hit them:
- Wait a few minutes
- Use `--model gemini-1.5-flash-8b` for faster, cheaper model
- Upgrade to paid tier

### Dependencies conflict

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python council.py
```

## Advanced Setup

### Use with OpenAI instead

Modify `council.py` to use OpenAI SDK:

```python
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(persona_name, user_input, context=""):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": PERSONAS[persona_name]["prompt"]},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
```

### Use with Anthropic Claude

```python
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def get_response(persona_name, user_input, context=""):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=PERSONAS[persona_name]["prompt"],
        messages=[{"role": "user", "content": user_input}]
    )
    return message.content[0].text
```

---

**Need help?** Open an issue or check the main README.
