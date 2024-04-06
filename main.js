const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");

let win;

function createWindow() {
  win = new BrowserWindow({ width: 800, height: 600 });

  // load the dist folder from Angular
  // win.loadURL(
  //   url.format({
  //     pathname: path.join(__dirname, "./dist/bell-system/browser/index.html"),
  //     protocol: "file:",
  //     slashes: true,
  //   })
  // );
  win.loadURL("http://localhost:4200");

  // Open the DevTools.
  win.webContents.openDevTools();

  win.on("closed", () => {
    win = null;
  });
}

app.on("ready", createWindow);

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
