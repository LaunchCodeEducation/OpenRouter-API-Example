import requests


MODEL = "anthropic/claude-haiku-4.5"

# Keep the LaunchCode-provided course key in a local file instead of pasting it into code.
try:
  with open("claude_cred.txt", "r", encoding="utf-8") as f:
    api_key = f.read().strip()
except FileNotFoundError:
  raise SystemExit(
    "Could not find claude_cred.txt. Create that file in this folder and paste in your LaunchCode-provided course key as the only content."
  )

if not api_key:
  raise SystemExit(
    "claude_cred.txt is empty. Paste your LaunchCode-provided course key into that file as the only content."
  )

payload = {
  # This course key can access only the approved model listed here.
  "model": MODEL,
  "messages": [
    {
      "role": "user",
      "content": "Hello, Claude. Please reply with a short greeting.",
    }
  ],
}

try:
  response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    json=payload,
    headers={
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json",
    },
    timeout=60,
  )
  response.raise_for_status()
  body = response.json()
except requests.exceptions.HTTPError as e:
  status_code = e.response.status_code
  error_body = e.response.text

  if status_code == 401:
    raise SystemExit(
      "401 Unauthorized: check that claude_cred.txt contains only your LaunchCode-provided course key on a single line."
    )

  if status_code == 404:
    raise SystemExit(
      "404 from OpenRouter: your course key is expected to work only with anthropic/claude-haiku-4.5. See example-open-router-responses/example_404_guardrail_error.json."
    )

  raise SystemExit(f"{status_code} error from OpenRouter:\n{error_body}")
except requests.exceptions.RequestException as e:
  raise SystemExit(
    f"Could not reach OpenRouter: {e}. Check your internet connection and try again."
  )

print(body["choices"][0]["message"]["content"])
