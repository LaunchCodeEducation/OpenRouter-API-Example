# OpenRouter Hello Claude Example

This repo is a beginner-friendly example of how to send a simple Claude request through OpenRouter.

For this exercise, LaunchCode provides a course OpenRouter key. You will store that key in a local file named `claude_cred.txt` and use it with the course-approved model `anthropic/claude-haiku-4.5`.

This tutorial uses the `requests` library to make the OpenRouter call.

## What You Will Learn

- How to keep an API key in a local file instead of pasting it into Python code.
- How to run a Python script that sends a request to OpenRouter.
- How to make a successful OpenRouter request to the course-approved model `anthropic/claude-haiku-4.5`.
- How to recognize common OpenRouter error responses for this course key.

## What You Need

### Python 3

To check whether Python 3 is installed, open a terminal and run:

macOS or Linux:

```bash
python3 --version
```

Windows:

```powershell
py --version
```

If you see a Python version such as `Python 3.12.4`, Python 3 is installed.

If your computer says the command is not recognized, download Python 3 from [Python Downloads](https://www.python.org/downloads/).

### Visual Studio Code

If you do not have Visual Studio Code yet, download it from [Visual Studio Code Download](https://code.visualstudio.com/Download).

### LaunchCode OpenRouter API Key

Have your LaunchCode-provided OpenRouter API key ready before you begin.

## Get This Project On Your Computer

You do not need a GitHub account to complete this tutorial.

### Option A: Download ZIP

This is the simplest option if you only need to run the example locally.

1. Open the [OpenRouter-API-Example repository](https://github.com/LaunchCodeEducation/OpenRouter-API-Example).
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Unzip the downloaded file.
5. Move it to your `Documents` folder.
6. Open the unzipped project folder on your computer using [Visual Studio Code](https://code.visualstudio.com/).

> The unzipped folder may be named `OpenRouter-API-Example-main`.

### Option B: Clone With Git

If you already have Git installed, you can clone the repo instead.

```bash
cd path-on-your-computer-you-want-project-to-be-cloned-to
git clone https://github.com/LaunchCodeEducation/OpenRouter-API-Example.git
cd OpenRouter-API-Example
```

## Add Your OpenRouter Key

1. In the project folder, create a file named `claude_cred.txt`.
2. Paste the LaunchCode-provided course key into that file.
3. Make sure the file contains only the key.

Do not add quotes, labels, or extra lines.

## Open The Terminal In Visual Studio Code

After you open this project folder in Visual Studio Code:

1. At the top of the Visual Studio Code window, click **Terminal** in the menu bar.
2. In the dropdown menu, click **New Terminal**.
3. A terminal panel will open at the bottom of the VS Code window.
4. Make sure the terminal is in this project folder, where `hello_claude.py` is located.

### Verify You Are In The Project Folder

To check your current folder, run the command for your operating system:

macOS or Linux:

```bash
pwd
ls
```

Windows:

```powershell
pwd
dir
```

You should see this project folder path, and `hello_claude.py` should appear in the file list.

If you are not in the correct folder yet, use `cd` to move into it.

If you downloaded the ZIP file:

```bash
cd ~/Documents/OpenRouter-API-Example-main
```

If you used `git clone`:

```bash
cd ~/Documents/OpenRouter-API-Example
```

You will run the Python command in that VS Code terminal window.

## Create And Activate A Virtual Environment

This project uses a local Python virtual environment named `.venv`.

That keeps this project's Python package installation separate from other Python projects on your computer.

Use the terminal window inside Visual Studio Code.

### macOS And Linux

On macOS, use `python3` for the commands in this tutorial. Depending on how Python is installed on your Mac, `python` may point to a different interpreter or may not be available.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

Use the default VS Code terminal window.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

When the environment is active, your terminal prompt usually starts with `(.venv)`.

## Install The Project Dependency

With the virtual environment activated, run the command for your operating system.

### macOS And Linux

```bash
python3 -m pip install -r requirements.txt
```

### Windows

```powershell
python -m pip install -r requirements.txt
```

## Run The Example

Use the terminal window inside Visual Studio Code.

With the virtual environment activated, run the command for your operating system.

### macOS And Linux

```bash
python3 hello_claude.py
```

### Windows

```powershell
python hello_claude.py
```

If everything is set up correctly, the script prints a short reply from Claude.

## Deactivate The Virtual Environment

When you are done working in this project, run:

```bash
deactivate
```

This returns your terminal to your normal system Python so you do not accidentally keep using this project's virtual environment in other work.

If you forget, your terminal prompt usually still starts with `(.venv)`.

## Keep Your Key Safe

- Do not paste your course key into `hello_claude.py` or any other Python file.
- Do not share your API key with other people.
- Keep `claude_cred.txt` on your own computer.
- This repo already lists `claude_cred.txt` in `.gitignore`, which helps prevent accidental commits if you later use Git.

You do not need to commit or upload anything to complete this tutorial.

If you later decide to store your work in Git or GitHub, make sure files that contain secrets stay ignored and never get uploaded. See GitHub Docs: [Ignoring files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files).

## Files In This Repo

- `hello_claude.py`: the minimal Python example for the course-approved OpenRouter call.
- `requirements.txt`: the Python dependency list for this project.
- `example-open-router-responses/successful_call_example.json`: an example JSON response from a successful request.
- `example-open-router-responses/example_404_guardrail_error.json`: an example JSON response returned when the request tries a model the course key cannot access.
- `example-open-router-responses/claude-haiku-4.5_model-details.json`: reference details for the course-approved model from OpenRouter.

You send the alias `anthropic/claude-haiku-4.5`, but the JSON response may show a more specific provider model version in the `model` field.

## Common Python Errors

- **Missing `claude_cred.txt`**: If Python says it cannot find `claude_cred.txt`, make sure that file is in the same folder as `hello_claude.py`.
- **`ModuleNotFoundError: No module named 'requests'`**: Your virtual environment is not activated yet, or you have not run the `pip install -r requirements.txt` command for your operating system.
- **`401 Unauthorized`**: `claude_cred.txt` does not contain the correct key, or it contains extra whitespace or extra text.
- **`404 from OpenRouter`**: You tried to use a model outside the access allowed for your course key. For this course, use only `anthropic/claude-haiku-4.5`.
- **`python3`, `py`, or `python` is not recognized**: Python may not be installed yet. If you just installed Python, close the terminal, open a new one, and try the command again.
- **Could not reach OpenRouter**: Check your internet connection and try again.
- **SSL certificate errors**: These are less common with `requests`, but they can still happen on some school, work, or proxy-managed networks. If this happens, use your Claude chat account or Claude desktop/web app to help troubleshoot the Python environment, certificate store, or proxy settings. Do not use your OpenRouter API key for troubleshooting.
- **PowerShell blocks `.\.venv\Scripts\Activate.ps1`**: Switch the VS Code terminal profile to Command Prompt and use `.venv\Scripts\activate.bat` instead.

## OpenRouter Language

This example uses Claude through OpenRouter, not through Anthropic's direct API.

That means:

- the credential file is still named `claude_cred.txt`
- the key is still read from a local text file at runtime
- the network request goes to OpenRouter
- the course-approved model is `anthropic/claude-haiku-4.5`
