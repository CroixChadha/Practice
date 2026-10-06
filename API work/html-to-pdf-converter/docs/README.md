# HTML-to-PDF Converter Documentation

## Quick Links
- [API Integration Guide](./api-guide.md) - How the html2pdf API works
- [Flask Routes](./flask-routes.md) - Backend endpoint documentation
- [JavaScript Architecture](./js-architecture.md) - Frontend flow and design
- [Rate Limiting](./rate-limiting.md) - Implementation strategy
- [Deployment](./deployment.md) - How to deploy this app

## Project Structure
```
docs/
├── README.md                 # This file
├── api-guide.md             # html2pdf.fly.dev API documentation
├── flask-routes.md          # Backend routes and handlers
├── js-architecture.md       # Frontend JavaScript design
├── rate-limiting.md         # Rate limiting implementation
└── deployment.md            # Deployment instructions
```

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`
3. Visit `http://localhost:5000`
4. Upload an HTML file and convert to PDF

## Key Technologies
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: html2pdf.fly.dev (free, no authentication)
