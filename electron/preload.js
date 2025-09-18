const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  uploadFile: (filePath) => ipcRenderer.invoke('upload-file', filePath)
});
