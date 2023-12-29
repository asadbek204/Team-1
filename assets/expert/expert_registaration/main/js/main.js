
const toggleBlur = () => {
  const blurEl = document.getElementById("blur");
  blurEl.classList.toggle("active");

  const popupEl = document.getElementById("popup");
  popupEl.classList.toggle("active");
};


const usernameInput = document.getElementById('username_input');
const usernamePassword = document.getElementById('username_password');


const onChangeWrap = (input) => (e) => {
    input.innerText = e.target.value;
    console.log(e.target.value)
}


usernameInput.addEventListener('input', onChangeWrap(usernameInput));
usernamePassword.addEventListener('input', onChangeWrap(usernamePassword));
