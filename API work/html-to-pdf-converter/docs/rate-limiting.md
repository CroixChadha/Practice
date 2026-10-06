# Rate Limiting Implementation

## Purpose
Prevent abuse of the html2pdf API and control costs. We track requests per IP address and enforce limits.

## Strategy

**Rate Limits:**
- Max 5 conversions per minute per IP
- Max 20 conversions per hour per IP

**Implementation Approach:**
1. Create a dictionary to track request timestamps per IP
2. Check timestamp history when request comes in
3. If over limit, return 429 error
4. Clean up old timestamps periodically

## Python Implementation Guide

### Data Structure
```python
from collections import defaultdict
from datetime import datetime, timedelta

rate_limit_tracker = defaultdict(list)  # {ip: [timestamp1, timestamp2, ...]}
```

### Rate Limit Check Function
```python
def check_rate_limit(ip, max_per_minute=5, max_per_hour=20):
    now = datetime.now()
    
    # Get timestamps for this IP
    timestamps = rate_limit_tracker[ip]
    
    # Remove old timestamps (older than 1 hour)
    timestamps = [t for t in timestamps if (now - t).total_seconds() < 3600]
    rate_limit_tracker[ip] = timestamps
    
    # Check limits
    recent_minute = [t for t in timestamps if (now - t).total_seconds() < 60]
    if len(recent_minute) >= max_per_minute:
        return False, "Too many requests in the last minute"
    
    if len(timestamps) >= max_per_hour:
        return False, "Too many requests in the last hour"
    
    # Add current request
    timestamps.append(now)
    return True, "OK"
```

### Usage in Route
```python
@app.route('/upload', methods=['POST'])
def upload():
    ip = request.remote_addr
    allowed, message = check_rate_limit(ip)
    
    if not allowed:
        return {"error": message}, 429
    
    # ... rest of implementation
```

## Testing
- Upload 5 PDFs quickly - 6th should be rate limited
- Wait 1 minute and try again - should work
- Monitor the rate_limit_tracker to see what's being tracked
