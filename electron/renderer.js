const fileInput = document.getElementById('file');
const preview = document.getElementById('preview');
const status = document.getElementById('status');
const removeBtn = document.getElementById('removeBtn');
let selectedFile = null;

fileInput.onchange = () => {
  selectedFile = fileInput.files[0];
  if (!selectedFile) return;
  const url = URL.createObjectURL(selectedFile);
  preview.src = url;
  status.innerText = 'File loaded: ' + selectedFile.name;
};

removeBtn.onclick = async () => {
  if (!selectedFile) { alert('Pilih file dulu'); return; }
  status.innerText = 'Uploading...';
  const fd = new FormData();
  fd.append('file', selectedFile);
  // send to local backend
  try {
    const res = await fetch('http://localhost:9000/remove', { method: 'POST', body: fd });
    const j = await res.json();
    status.innerText = 'Processing started. Output: ' + j.output;
  } catch (e) {
    status.innerText = 'Error: ' + e.message;
  }
};
