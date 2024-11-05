const video = document.getElementById('webcam');
const captureButton = document.getElementById('captureButton');
const canvas = document.getElementById('snapshotCanvas');
const context = canvas.getContext('2d');

// Ask for webcam access and start video stream
navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.log("Error accessing the webcam: " + err);
    });

// Capture the current video frame when the button is clicked
captureButton.addEventListener('click', function() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Display the captured image
    canvas.style.display = 'block';
});
