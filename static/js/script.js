document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append('image', document.getElementById('uploadInput').files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayPalette(data.colors);
    })
    .catch(error => console.error('Error:', error));
});

function displayPalette(colors) {
    let paletteContainer = document.getElementById('paletteContainer');
    paletteContainer.innerHTML = ''; // Clear previous results

    colors.forEach(color => {
        let colorBox = document.createElement('div');
        colorBox.style.backgroundColor = color.color;
        colorBox.textContent = color.hex;
        paletteContainer.appendChild(colorBox);
    });
}
