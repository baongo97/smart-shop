# How to start the App

## Prerequisites

- Python 3.10+ (or a compatible Python 3.x)
- A valid OpenAI API key (set in an environment variable named `OPENAI_API_KEY`)


Create Python virtual environment
```bash
python3 -m venv .venv
```

Activate Python virtual environment
```bash
source .venv/bin/activate
```

Install Python dependencies
```bash
pip install -r ./shopping-list/backend/requirements.txt
```

Install React dependencies
```bash
cd shopping-list/frontend && npm install && cd ../..
```

## Environment variables

Create a `.env` file in the `shopping-list/backend/` directory or set the environment variable directly. Example `.env` (do NOT commit real keys):

```bash
cp ./shopping-list/backend/.env.example ./shopping-list/backend/.env
```

```
OPENAI_API_KEY=sk-...
```

## Run the server

Run `shopping-list/backend`
```bash
python3 shopping-list/backend/main.py
```

Run `shopping-list/frontend`
```bash
cd shopping-list/frontend && npm run dev
```

Go back to the root project
```bash
cd ../..
```

Run `smart-navigating` backend
```bash
python3 smart-navigating/store_locator.py
```

Run `smart-navigating` frontend
```bash
cd smart-navigating && python3 -m http.server 8080
```

## How to use the App
Use your browser and connect to
http://100.85.250.60:5173/
Or
http://localhost:5173/