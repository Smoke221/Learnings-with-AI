# Object Identifier with Webcam

This project implements an object identifier using a webcam. It utilizes computer vision technologies and machine learning models to identify objects in real-time.

## Deployment

The project is deployed on [Netlify](https://grand-peony-970136.netlify.app/). You can visit the deployed link to access the application.

## Usage

To use the object identifier:

1. Visit the deployed link.
2. Click on "Start" and grant the necessary camera permissions.
3. Wait for the page to load. Initially, if you're not holding any object, the response will indicate "Not holding anything."
4. Experiment by holding different objects, such as a clothespin or a toothbrush.
5. Click on "Stop" to pause the video.

## Implementation Details

- The application incorporates computer vision and machine learning technologies, including ChatGPT and Google Teachable Machine.
- The backend server runs on port 3000. To run the code locally, follow these steps:
  - Install all dependencies by running `npm install`.
  - Start the backend server by running `npm run dev`.

Note: The project includes a 5-second delay for each API request to optimize performance and avoid overloading the system.

Feel free to explore and use the code to understand the technical implementation behind the object identifier application.

