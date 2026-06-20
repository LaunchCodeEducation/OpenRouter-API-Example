import json
import urllib.error
import urllib.request


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

request = urllib.request.Request(
  "https://openrouter.ai/api/v1/chat/completions",
  data=json.dumps(payload).encode("utf-8"),
  headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
  },
  method="POST",
)

try:
  with urllib.request.urlopen(request, timeout=60) as response:
    body = json.loads(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
  error_body = e.read().decode("utf-8")

  if e.code == 401:
    raise SystemExit(
      "401 Unauthorized: check that claude_cred.txt contains only your LaunchCode-provided course key on a single line."
    )

  if e.code == 404:
    raise SystemExit(
      "404 from OpenRouter: your course key is expected to work only with anthropic/claude-haiku-4.5. See example-open-router-responses/example_404_guardrail_error.json."
    )

  raise SystemExit(f"{e.code} error from OpenRouter:\n{error_body}")
except urllib.error.URLError as e:
  raise SystemExit(
    f"Could not reach OpenRouter: {e.reason}. Check your internet connection and try again."
  )

print(body["choices"][0]["message"]["content"])
