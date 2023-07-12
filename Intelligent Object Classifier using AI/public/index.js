// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
const URL = "https://teachablemachine.withgoogle.com/models/LYk-iUL58/";

let model, webcam, labelContainer, maxPredictions;
let lastApiCallTime = Date.now(); // Track the time of the last API call
let isWebcamRunning = false; // Flag to track the webcam state

// Load the image model and setup the webcam
async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";

  // Load the model and metadata
  model = await tmImage.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();

  // Convenience function to setup a webcam
  const flip = true; // whether to flip the webcam
  webcam = new tmImage.Webcam(400, 400, flip); // width, height, flip
  await webcam.setup(); // request access to the webcam
  await webcam.play();
  isWebcamRunning = true; // Set the flag to indicate that the webcam is running

  // Append the webcam video element to the DOM
  const webcamContainer = document.getElementById("webcam-container");
  webcamContainer.innerHTML = ""; // Clear any existing content
  webcamContainer.appendChild(webcam.canvas);

  labelContainer = document.getElementById("label-container");
  for (let i = 0; i < maxPredictions; i++) {
    // and class labels
    labelContainer.appendChild(document.createElement("div"));
  }

  loop(); // Start the loop
}

async function loop() {
  if (isWebcamRunning) {
    webcam.update(); // update the webcam frame
    await predict();
    window.requestAnimationFrame(loop);
  }
}

// Run the webcam image through the image model
async function predict() {
  // Predict can take in an image, video, or canvas HTML element
  const prediction = await model.predict(webcam.canvas);
  for (let i = 0; i < maxPredictions; i++) {
    const classPrediction =
      prediction[i].className + ": " + prediction[i].probability.toFixed(2);

    const probabilityThreshold = 0.9;
    if (
      prediction[i].probability >= probabilityThreshold &&
      Date.now() - lastApiCallTime >= 5000
    ) {
      lastApiCallTime = Date.now(); // Update the last API call time

      const objectName = prediction[i].className; // Get the predicted object class

      // Make a POST request to the backend endpoint
      fetch("http://localhost:3000/identify/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ objectName }), // Send the predicted object class
      })
        .then((response) => response.json())
        .then((data) => {
          const objectInfo = data.response;
          // Display the object information in your UI as needed
          document.querySelector(".response").textContent = objectInfo;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  }
}

function stopWebcam() {
  if (webcam) {
    webcam.stop();
    webcam = null;
    isWebcamRunning = false; // Set the flag to indicate that the webcam is stopped
  }
}
