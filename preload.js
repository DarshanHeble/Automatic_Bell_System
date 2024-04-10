const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("darkMode", {
  toogle: () => ipcRenderer.invoke("toogle"),
});
