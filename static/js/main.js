const inputBtn = document.getElementById("special-btn");
const inputEl = document.getElementById("citi");

function getInputVal() {
  console.log(inputEl.value);
}

inputBtn.addEventListener("click", getInputVal);