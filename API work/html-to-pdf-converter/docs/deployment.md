# Deployment Guide

## Local Development

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit
http://localhost:5000
```

## Production Deployment

### Recommended Approaches

#### Option 1: Heroku (Simple)
```bash
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Create runtime.txt
echo "python-3.11.0" > runtime.txt

# Deploy
heroku login
heroku create your-app-name
git push heroku main
```

#### Option 2: PythonAnywhere (Easy)
1. Sign up at pythonanywhere.com
2. Upload your code
3. Configure WSGI
4. Enable web app

#### Option 3: DigitalOcean/AWS/GCP (More Control)
Use Flask with gunicorn and Nginx reverse proxy.

### Important Configuration

#### Use Production WSGI Server
Never use `debug=True` in production. Use gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

#### Environment Variables
```bash
FLASK_ENV=production
DEBUG=False
```

#### Static Files
In production, serve static files with Nginx or CDN, not Flask.

### Security Checklist
- [ ] Set `debug=False`
- [ ] Use strong SECRET_KEY for sessions
- [ ] Set rate limiting appropriately
- [ ] Validate all file uploads
- [ ] Use HTTPS
- [ ] Monitor API usage costs (if using paid APIs)

### Monitoring
- Check request logs for errors
- Monitor API response times
- Track rate limit hits
- Watch for unusual file upload patterns

## Troubleshooting

### Common Issues
- **PDF not generating**: Check html2pdf API status
- **File upload fails**: Check file size limits
- **Slow conversion**: HTML might be too complex
- **Rate limit errors**: Adjust limits or add caching

### Debugging
Enable logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
