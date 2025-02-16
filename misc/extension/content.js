const link = document.createElement('link');
link.rel = 'stylesheet';
link.href = chrome.runtime.getURL('style.css');
document.head.appendChild(link);

const img = document.createElement('img');
img.src = chrome.runtime.getURL('image.png');
img.alt = 'Overlay Image';
img.classList.add('overlay-image');
document.body.appendChild(img);