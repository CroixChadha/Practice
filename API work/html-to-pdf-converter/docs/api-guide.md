# HTML-to-PDF API Integration Guide

## Service: html2pdf.fly.dev

### Endpoint
```
POST https://html2pdf.fly.dev/api/generate
```

### Request Format
The API expects JSON with the HTML content:
```json
{
  "html": "<html>...</html>"
}
```

### Response
- **Success (200)**: Binary PDF data
- **Error**: JSON error message

### Example Usage
```python
import requests

response = requests.post(
    'https://html2pdf.fly.dev/api/generate',
    json={'html': html_content},
    timeout=30
)

if response.status_code == 200:
    pdf_data = response.content  # Binary PDF
else:
    error = response.json()
```

### Important Notes
- No authentication required
- No API key needed
- Free service (be respectful with usage)
- Response is binary PDF data, not JSON
- Timeout: Set a reasonable timeout (30 seconds)
- Error handling: Always check status code before processing response

### Common Errors
- **400**: Invalid HTML provided
- **408**: Request timeout (HTML too complex)
- **500**: Service error

### Testing
You can test the API directly with curl:
```bash
curl -X POST https://html2pdf.fly.dev/api/generate \
  -H "Content-Type: application/json" \
  -d '{"html":"<html><body>Hello World</body></html>"}'
```
