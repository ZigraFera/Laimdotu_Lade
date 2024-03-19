

const videoPreview = document.getElementById('videoPreview');
const videoPreviewSource = document.getElementById('avots');
const documentPreview = document.getElementById('Document');
const audioPreview = document.getElementById('audioPreview');
let fileLocation = document.getElementById('fileLocation').value;

console.log("File Location:", fileLocation);

const fileExtension = fileLocation.split('.').pop().toLowerCase();
if (fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg') {
    // Video file
    videoPreview.style.display = 'block';
    videoPreviewSource.src = fileLocation;
} else if (fileExtension === 'pdf' || fileExtension === 'doc' || fileExtension === 'docx' || fileExtension === 'xls' || fileExtension === 'xlsx' || fileExtension === 'ppt' || fileExtension === 'pptx') {
    // Document file
    documentPreview.style.display = 'block';
    documentPreview.innerHTML = `<iframe src="${fileLocation}" type="application/pdf" frameborder="0" width="100%" height="600px"></iframe>`;
} else if (fileExtension === 'mp3' || fileExtension === 'wav' || fileExtension === 'ogg' || fileExtension === 'm4a') {
    // Audio file
    audioPreview.style.display = 'block';
    audioPreview.src = fileLocation;
} else {
    // Unsupported file type
    console.error('Unsupported file type');
}


    // Show the corresponding preview element based on the file extension
    
// const fileExtension = fileUrl.split('.').pop().toLowerCase();
// function Preview() {

//   // Render different file types accordingly
//   if (fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg') {
//       // Video file
//       document.getElementById('filePreview').innerHTML = `
//           <video controls>
//               <source src="${fileUrl}" type="video/${fileExtension}">
//               Your browser does not support the video tag.
//           </video>`;
//   } else if (fileExtension === 'jpg' || fileExtension === 'jpeg' || fileExtension === 'png' || fileExtension === 'gif') {
//       // Image file
//       document.getElementById('filePreview').innerHTML = `
//           <img src="${fileUrl}" alt="Image Preview" style="max-width: 100%; max-height: 100%;">`;
//   } else if (fileExtension === 'pdf' || fileExtension === 'doc' || fileExtension === 'docx' || fileExtension === 'xls' || fileExtension === 'xlsx' || fileExtension === 'ppt' || fileExtension === 'pptx') {
//       // Document file
//       document.getElementById('filePreview').innerHTML = `
//           <iframe src="https://docs.google.com/gview?url=${encodeURIComponent(fileUrl)}&embedded=true" style="width:100%; height:100%;" frameborder="0"></iframe>`;
//   } else {
//       // Unsupported file type
//       document.getElementById('filePreview').innerHTML = `<p>Unsupported file type</p>`;
//     }
// }  