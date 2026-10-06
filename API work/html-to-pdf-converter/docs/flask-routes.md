# Flask Routes Documentation

## Routes Overview

### GET `/`
**Purpose:** Serve the main landing page

**Response:** HTML template (`index.html`)

**Example:**
```
GET http://localhost:5000/
```

---

## TODO: POST `/upload` (To be implemented)

**Purpose:** Receive HTML file, convert to PDF, return binary PDF

**Request:**
```json
{
  "html": "<html>...</html>",
  "filename": "document.html"
}
```

**Response:**
- **Success (200)**: Binary PDF file with Content-Type: application/pdf
- **Error (400)**: `{"error": "error message"}`
- **Error (429)**: `{"error": "Rate limit exceeded"}` (if rate limited)

**Implementation Notes:**
- Validate HTML is not empty
- Call html2pdf.fly.dev API
- Handle timeouts and API errors
- Implement rate limiting per IP
- Return PDF as binary data with proper headers

**Example Implementation Structure:**
```python
@app.route('/upload', methods=['POST'])
def upload():
    # 1. Get JSON data
    # 2. Validate HTML content
    # 3. Check rate limit
    # 4. Call html2pdf API
    # 5. Handle errors
    # 6. Return PDF
```

---

## Rate Limiting

See [rate-limiting.md](./rate-limiting.md) for detailed implementation guide.

**Default Rules:**
- Max 5 conversions per minute per IP
- Max 20 conversions per hour per IP
