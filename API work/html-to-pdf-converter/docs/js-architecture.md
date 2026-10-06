# JavaScript Architecture

## Overview
The frontend JavaScript handles file upload, validation, and PDF display. It communicates with the Flask backend via fetch API.

## Key Functions

### File Handling
- **readFileAsText()** - Reads HTML file content using FileReader API
- **validateFile()** - Checks file type and size before upload

### Communication
- **uploadForm submission** - Triggers conversion process
- **fetch to /upload** - Sends HTML to Flask backend
- **Response handling** - Receives PDF binary data

### Display
- **displayPDF()** - Shows preview in iframe, creates download link
- **Status messages** - Error, loading, and success feedback

## Data Flow

```
User selects HTML file
    ↓
JavaScript reads file content
    ↓
User clicks "Convert"
    ↓
Fetch POST to /upload with HTML content
    ↓
Flask calls html2pdf API
    ↓
Returns PDF binary data
    ↓
JavaScript creates blob URL
    ↓
Display in iframe + download link
```

## Key Concepts Explained

### FileReader API
Allows reading file contents as text. Used to get HTML content from uploaded file.

### Fetch API
Modern way to make HTTP requests from JavaScript. Returns a Promise.

### Blob
Binary Large Object - used to handle PDF file data from API response.

### Object.createObjectURL()
Converts binary blob into a URL that can be used in href or iframe src.

## Error Handling
- File validation errors show immediately
- API errors caught in try-catch
- User-friendly error messages displayed
