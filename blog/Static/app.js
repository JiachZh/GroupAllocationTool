const usernameBox = document.getElementById('username');
const firstnameBox = document.getElementById('firstname');
const lastnameBox = document.getElementById('lastname');
const emailBox = document.getElementById('email');
const passwordBox = document.getElementById('password');
const confirmPasswordBox = document.getElementById('confirm_password');
const usernameMessage = document.getElementById('usernameMessage');
const firstnameMessage = document.getElementById('firstnameMessage');
const lastnameMessage = document.getElementById('lastnameMessage');
const emailMessage = document.getElementById('emailMessage');
const passwordMessage = document.getElementById('passwordMessage');
const confirmPasswordMessage = document.getElementById('confirm_passwordMessage');

function addUsernameMessage(e) {
    usernameMessage.style.visibility = null;
}
function removeUsernameMessage(e) {
    usernameMessage.style.visibility = 'hidden';
}
function addFirstnameMessage(e) {
    firstnameMessage.style.visibility = null;
}
function removeFirstnameMessage(e) {
    firstnameMessage.style.visibility = 'hidden';
}
function addLastnameMessage(e) {
    lastnameMessage.style.visibility = null;
}
function removeLastnameMessage(e) {
    lastnameMessage.style.visibility = 'hidden';
}
function addEmailMessage(e) {
    emailMessage.style.visibility = null;
}
function removeEmailMessage(e) {
    emailMessage.style.visibility = 'hidden';
}
function addPasswordMessage(e) {
    passwordMessage.style.visibility = null;
}
function removePasswordMessage(e) {
    passwordMessage.style.visibility = 'hidden';
}
function addConfirmPasswordMessage(e) {
    confirmPasswordMessage.style.visibility = null;
}
function removeConfirmPasswordMessage(e) {
    confirmPasswordMessage.style.visibility = 'hidden';
}

usernameBox.addEventListener('mouseover', addUsernameMessage);
usernameBox.addEventListener('mouseout', removeUsernameMessage);

firstnameBox.addEventListener('mouseover', addFirstnameMessage);
firstnameBox.addEventListener('mouseout', removeFirstnameMessage);

lastnameBox.addEventListener('mouseover', addLastnameMessage);
lastnameBox.addEventListener('mouseout', removeLastnameMessage);

emailBox.addEventListener('mouseover', addEmailMessage);
emailBox.addEventListener('mouseout', removeEmailMessage);

passwordBox.addEventListener('mouseover', addPasswordMessage);
passwordBox.addEventListener('mouseout', removePasswordMessage);

confirmPasswordBox.addEventListener('mouseover', addConfirmPasswordMessage);
confirmPasswordBox.addEventListener('mouseout', removeConfirmPasswordMessage);

