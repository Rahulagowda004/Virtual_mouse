let videoStream;
let captureInterval;

document.getElementById("startButton").addEventListener("click", async () => {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert("Camera not supported on your browser.");
    return;
  }
  videoStream = await navigator.mediaDevices.getUserMedia({
    video: true,
  });
  const videoElement = document.createElement("video");
  videoElement.srcObject = videoStream;
  videoElement.play();

  captureInterval = setInterval(async () => {
    const canvas = document.createElement("canvas");
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    const context = canvas.getContext("2d");
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL("image/jpeg");

    await fetch("/upload_frame", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ frame: dataUrl }),
    });
  }, 100); // Adjust the interval as needed
});

document.getElementById("stopButton").addEventListener("click", () => {
  if (videoStream) {
    videoStream.getTracks().forEach((track) => track.stop());
    clearInterval(captureInterval);
  }
});