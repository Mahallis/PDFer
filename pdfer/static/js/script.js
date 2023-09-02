let upload = document.getElementById("id_file_field");

if (document.querySelector("#canvas-container")) {
  upload.addEventListener("input", async () => {
    drawPage();
  });
}

async function drawPage() {
  const url = URL.createObjectURL(upload.files[0]);
  const loadingTask = pdfjsLib.getDocument(url);
  const container = document.querySelector("#canvas-container");
  container.innerHTML = "";
  const pdf = await loadingTask.promise;

  for (let num = 1; num <= pdf.numPages; num++) {
    const page = await pdf.getPage(num);
    createCanvas(num, container);
    renderPage(num, page);
  }
}

async function createCanvas(num, container) {
  const canvas = document.createElement("canvas");
  const canvasDiv = document.createElement("div");
  canvas.id = "canvas" + num;
  canvas.style = "border: solid 1px black; margin: 5px";
  canvasDiv.style =
    "border: solid 1px black; display: flex; align-items: center; justify-content: center;";
  canvasDiv.append(canvas);
  container.append(canvasDiv);
}

async function renderPage(num, page) {
  const scale = 0.2;
  const viewport = page.getViewport({ scale });
  const outputScale = window.devicePixelRatio || 1;

  const canvas = document.querySelector("#canvas" + num);
  const context = canvas.getContext("2d");

  canvas.width = Math.floor(viewport.width * outputScale);
  canvas.height = Math.floor(viewport.height * outputScale);
  canvas.style.width = Math.floor(viewport.width) + "px";
  canvas.style.height = Math.floor(viewport.height) + "px";

  const transform =
    outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null;

  const renderContext = {
    canvasContext: context,
    transform,
    viewport,
  };
  await page.render(renderContext);
}
