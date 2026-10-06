// Get references to DOM elements
const uploadForm = document.getElementById('uploadForm');
const htmlFile = document.getElementById('htmlFile');
const uploadStatus = document.getElementById('uploadStatus');
const previewContainer = document.getElementById('previewContainer');
const noPreview = document.getElementById('noPreview');
const pdfPreview = document.getElementById('pdfPreview');
const downloadLink = document.getElementById('downloadLink');

// Handle form submission
uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get the file from the input
    const file = htmlFile.files[0];

    // Validate that a file was selected
    if (!file) {
        showError('Please select an HTML file');
        return;
    }

    // Validate file type
    if (!file.name.endsWith('.html') && !file.name.endsWith('.htm')) {
        showError('Please select a valid HTML file');
        return;
    }

    // Validate file size (max 10MB)
    const maxSize = 10 * 1024 * 1024;
    if (file.size > maxSize) {
        showError('File is too large (max 10MB)');
        return;
    }

    // Show loading message
    showLoading('Converting your HTML to PDF...');

    try {
        // Read the file as text
        const htmlContent = await readFileAsText(file);

        // Send to Flask backend
        const response = await fetch('/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                html: htmlContent,
                filename: file.name
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Conversion failed');
        }

        // Get the PDF as a blob
        const pdfBlob = await response.blob();

        // Create a URL for the PDF
        const pdfUrl = URL.createObjectURL(pdfBlob);

        // Display the PDF preview
        displayPDF(pdfUrl, file.name);

        showSuccess('PDF created successfully!');
    } catch (error) {
        showError(`Error: ${error.message}`);
        console.error('Conversion error:', error);
    }
});

// Helper function: Read file as text
function readFileAsText(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (e) => resolve(e.target.result);
        reader.onerror = (e) => reject(new Error('Failed to read file'));
        reader.readAsText(file);
    });
}

// Helper function: Display PDF preview
function displayPDF(pdfUrl, filename) {
    previewContainer.classList.remove('hidden');
    noPreview.style.display = 'none';

    // Set iframe src to display PDF
    pdfPreview.src = pdfUrl;

    // Set download link
    downloadLink.href = pdfUrl;
    downloadLink.download = filename.replace('.html', '.pdf');
}

// Helper function: Show error message
function showError(message) {
    uploadStatus.textContent = message;
    uploadStatus.className = 'status-message error';
    previewContainer.classList.add('hidden');
    noPreview.style.display = 'flex';
}

// Helper function: Show loading message
function showLoading(message) {
    uploadStatus.textContent = message;
    uploadStatus.className = 'status-message loading';
}

// Helper function: Show success message
function showSuccess(message) {
    uploadStatus.textContent = message;
    uploadStatus.className = 'status-message success';
}
