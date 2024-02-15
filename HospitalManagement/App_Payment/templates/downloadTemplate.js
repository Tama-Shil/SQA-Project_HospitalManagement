function downloadHTML() {
    // Get the content of the HTML body
    var content = document.documentElement.outerHTML;

    // Create a blob with the HTML content
    var blob = new Blob([content], { type: 'text/html' });

    // Create a link element to trigger the download
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'patient_details.html';

    // Append the link to the body and trigger the download
    document.body.appendChild(a);
    a.click();

    // Remove the link from the body
    document.body.removeChild(a);
}
