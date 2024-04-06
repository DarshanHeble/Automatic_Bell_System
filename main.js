const { app, BrowserWindow, ipcMain, nativeTheme } = require("electron");
const path = require("path");
const fs = require("fs");
const url = require("url");

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
// if (require("electron-squirrel-startup")) {
//   app.quit();
// }

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    x: 200,
    y: 200,
    width: 1000,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
    icon: path.join(__dirname, "Assets/Images/Bell Logo.jpeg"),
  });

  mainWindow.webContents.on("did-finish-load", () => {
    mainWindow.webContents.send("display-alarm"); // Trigger function in renderer
  });
  // remove the menu bar
  mainWindow.setMenuBarVisibility(false);

  // and load the index.html of the app.
  //   mainWindow.loadFile(path.join(__dirname, "index.html"));
  mainWindow.loadURL("http://localhost:4200");

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // function when window is closed
  mainWindow.on("close", function (e) {
    console.log("hi");
  });
};

folder_path = "./Assets/music";
extensions = ["mp3"];

get_fle_names(folder_path, extensions);

function get_fle_names(folder_path, extensions) {
  return new Promise((resolve, reject) => {
    fs.readdir(path.join(__dirname, folder_path), (err, data) => {
      if (err) console.log(err);
      else console.log(data);
    });
  });
}

ipcMain.handle("dark-mode:toggle", () => {
  if (nativeTheme.shouldUseDarkColors) {
    console.log(nativeTheme.shouldUseDarkColors);
    nativeTheme.themeSource = "light";
  } else {
    console.log(nativeTheme.shouldUseDarkColors);
    nativeTheme.themeSource = "dark";
  }
  return nativeTheme.shouldUseDarkColors;
});

ipcMain.handle("dark-mode:system", () => {
  nativeTheme.themeSource = "system";
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", createWindow);

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
