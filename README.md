# OpenRouter Hello Claude Example

This repo is a beginner-friendly example of how to send a simple Claude request through OpenRouter.

For this exercise, LaunchCode provides a course OpenRouter key. You will store that key in a local file named `claude_cred.txt` and use it with the course-approved model `anthropic/claude-haiku-4.5`.

This tutorial uses only Python's standard library, so you do not need to install any extra Python packages.

## What You Will Learn

- How to keep an API key in a local file instead of pasting it into Python code.
- How to run a Python script that sends a request to OpenRouter.
- How to make a successful OpenRouter request to the course-approved model `anthropic/claude-haiku-4.5`.
- How to recognize common OpenRouter error responses for this course key.

## What You Need

- Python 3 installed on your computer.
- The LaunchCode-provided course OpenRouter key.

## Get This Project On Your Computer

You do not need a GitHub account to complete this tutorial.

### Option A: Download ZIP

This is the simplest option if you only need to run the example locally.

1. Open `https://github.com/LaunchCodeEducation/OpenRouter-API-Example`.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Unzip the downloaded file.
5. Open the unzipped project folder on your computer.

> The unzipped folder may be named `OpenRouter-API-Example-main`.

### Option B: Clone With Git

If you already have Git installed, you can clone the repo instead.

```bash
git clone https://github.com/LaunchCodeEducation/OpenRouter-API-Example.git
cd OpenRouter-API-Example
```

## Add Your OpenRouter Key

1. In the project folder, create a file named `claude_cred.txt`.
2. Paste the LaunchCode-provided course key into that file.
3. Make sure the file contains only the key.

Do not add quotes, labels, or extra lines.

## Run The Example

### macOS

Use `python3`, not `python`. On many Macs, `python` may point to a different interpreter or may not be available in the way you expect.

```bash
python3 hello_claude.py
```

### Windows

```bat
py hello_claude.py
```

If everything is set up correctly, the script prints a short reply from Claude.

## Keep Your Key Safe

- Do not paste your course key into `hello_claude.py` or any other Python file.
- Do not share your API key with other people.
- Keep `claude_cred.txt` on your own computer.
- This repo already lists `claude_cred.txt` in `.gitignore`, which helps prevent accidental commits if you later use Git.

You do not need to commit or upload anything to complete this tutorial.

If you later decide to store your work in Git or GitHub, make sure files that contain secrets stay ignored and never get uploaded. See GitHub Docs: [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files).

## Files In This Repo

- `hello_claude.py`: the minimal Python example for the course-approved OpenRouter call.
- `example-open-router-responses/successful_call_example.json`: an example JSON response from a successful request.
- `example-open-router-responses/example_404_guardrail_error.json`: an example JSON response returned when the request tries a model the course key cannot access.
- `example-open-router-responses/claude-haiku-4.5_model-details.json`: reference details for the course-approved model from OpenRouter.

You send the alias `anthropic/claude-haiku-4.5`, but the JSON response may show a more specific provider model version in the `model` field.

## Troubleshooting

- If Python says it cannot find `claude_cred.txt`, make sure that file is in the same folder as `hello_claude.py`.
- `401 Unauthorized` usually means `claude_cred.txt` does not contain the correct key, or it contains extra whitespace or extra text.
- `404` usually means you tried to use a model outside the access allowed for your course key. For this course, use only `anthropic/claude-haiku-4.5`.
- If your computer says `python3` or `py` is not recognized, Python may not be installed or may not be available in your terminal yet.
- If the script says it could not reach OpenRouter, check your internet connection and try again.

## OpenRouter Language

This example uses Claude through OpenRouter, not through Anthropic's direct API.

That means:

- the credential file is still named `claude_cred.txt`
- the key is still read from a local text file at runtime
- the network request goes to OpenRouter
- the course-approved model is `anthropic/claude-haiku-4.5`
