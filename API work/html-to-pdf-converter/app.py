from flask import Flask, render_template, request, send_file
import requests
from io import BytesIO
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

# Rate limiting tracker: {ip: [(timestamp, count)]}
rate_limit_tracker = defaultdict()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # TODO 1: Get the JSON data from the request using request.get_json()
    # Store it in a variable (e.g., data)

    # TODO 2: Extract the 'html' field from the JSON data
    # Make sure it exists, otherwise return error 400

    # TODO 3: Validate the HTML
    # - Check if it's empty (len > 0)
    # - Check if it has HTML markers (contains '<' and '>')
    # If validation fails, return error 400 with message

    # TODO 4: Check rate limit for this IP address
    # Get the IP: request.remote_addr
    # Call check_rate_limit(ip)
    # If rate limited, return error 429

    # TODO 5: Make a POST request to html2pdf API
    # URL: https://html2pdf.fly.dev/api/generate
    # Send: {"html": html_content}
    # Use requests.post() with timeout=30
    # Store response

    # TODO 6: Check if API call was successful
    # If not (status_code != 200), return error with API's error message

    # TODO 7: Get the PDF binary data from response
    # response.content gives you the binary data

    # TODO 8: Return the PDF to JavaScript
    # Use send_file() or return with proper headers
    # Content-Type should be 'application/pdf'

    pass

def check_rate_limit(ip, max_per_minute=5, max_per_hour=20):
    # TODO: Implement rate limiting logic
    # See docs/rate-limiting.md for the strategy
    # Return (allowed: bool, message: str)
    pass

if __name__ == '__main__':
    app.run(debug=True)
