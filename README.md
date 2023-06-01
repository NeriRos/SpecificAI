# SpecificAI

Ask your question regarding one of our topics and get a specific answer from the AI.

## Build

```bash
docker build -t specific_ai .
```

this could take a while... (about 400-500 seconds)

## Run

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY=your_open_api_key specific_ai
```

## Usage

### Web

1. Browse to http://localhost:8000
2. Choose a topic and submit. (wait for the model to load)
3. Enter your prompt

### API

```bash
curl -X POST -H "Content-Type: application/json" -d '{"prompt":"What vitamins help to fight cancer", "action": "insights"}' http://localhost:8000/query/execute?topic=gbm
```