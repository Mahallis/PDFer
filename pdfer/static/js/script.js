let upload = document.getElementById("id_file_field");
upload.oninput = function() {
  const url = URL.createObjectURL(upload.files[0]);
  const loadingTask = pdfjsLib.getDocument(url);
  const container = document.querySelector("#canvas-container");
  container.innerHTML = "";

  async function drawPage(loadingTask) {
    const pdf = await loadingTask.promise;
    for (let num = 1; num <= pdf.numPages; num++) {
      const page = await pdf.getPage(num);
      createCanvas(num, container);
      renderPage(num, page);
    }
  }

  drawPage(loadingTask);
};

function createCanvas(num, container) {
  const canvas = document.createElement("canvas");
  canvas.id = "canvas" + num;
  canvas.style = "border: solid 1px black;";
  container.append(canvas);
}

function renderPage(num, page) {
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
  page.render(renderContext);
}
