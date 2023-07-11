# Syllable Counting API

This Flask API provides a single endpoint for counting the number of syllables in a word. The endpoint accepts a POST request with the word provided in the request body and responds with the corresponding syllable count.

## Endpoint

- `/syllable`

## Request

- Method: `POST`
- Body: JSON object containing the word to count syllables for

Example:
```json
{
  "word": "example"
}
```

## Response

- Content-Type: `application/json`
- Body: JSON object containing the syllable count

Example:
```json
{
  "syllables": 3
}
```

