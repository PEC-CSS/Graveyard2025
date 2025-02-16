const showAlert = document.getElementsByTagName("button")
const customAlert = document.getElementById('customAlert')
const confirmButton = document.getElementById('confirmButton')


for (let i = 0; i < showAlert.length; i++) {
    showAlert[i].addEventListener('click', function() {
        customAlert.style.display = 'flex'; 
    });
}

confirmButton.addEventListener('click', function(){
    customAlert.style.display = 'none';
});