# HTML-to-PDF Converter Project Guide

## Project Overview
A Flask web application that converts HTML files to PDFs using the html2pdf.fly.dev API. This is a learning project focused on APIs, Python backend development, and intermediate CSS.

## Learning Objectives
- Understand Flask routing and request handling
- Learn how to make HTTP requests to external APIs using Python's `requests` library
- Implement client-side rate limiting
- Build beautiful, responsive web interfaces
- Understand async JavaScript and how it interacts with Flask

## Task Delegation

### You Write (Croix)
- **Flask `/upload` route** - file handling, API calls, error handling
- **Rate limiting logic** - track requests, enforce limits
- **Basic JavaScript** - with explanations of how it works

### I Write (Claude)
- **HTML structure** - semantic, accessible markup
- **CSS styling** - beautiful design, animations, responsive
- **Complex JavaScript** - async/await, state management, advanced interactions
- **Edge case handling** - security validation, error states

### We Discuss
- Engineering decisions (server vs client-side rendering)
- API integration strategy
- Security concerns and solutions

## Development Workflow

1. **Start Flask server**: `python app.py`
2. **Visit**: `http://localhost:5000`
3. **Test**: Upload HTML files and verify PDF conversion
4. **Iterate**: Adjust code based on errors and learning

## Key Files
- `app.py` - Flask application and routes
- `templates/index.html` - Main page structure
- `static/css/style.css` - Styling and layout
- `static/js/script.js` - File handling and form submission

## Next Steps
1. Implement Flask `/upload` route
2. Write API call logic with error handling
3. Add rate limiting
4. Test the full flow
5. Refine styling and user experience

## Notes
- The html2pdf.fly.dev API expects HTML content (no authentication required)
- Rate limit to prevent accidental API abuse
- Keep learning mode active - explain complex concepts as we go

## Git Commits
- Do NOT include "Co-Authored-By: Claude" attribution lines in commit messages
- Commits are authored by Croix only
