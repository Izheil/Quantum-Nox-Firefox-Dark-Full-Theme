// We wait for page load
document.addEventListener('DOMContentLoaded', function() {
	
	var parentBody = window.parent.document.body;
	var frameBody = document.body;
	var lightMode = document.querySelector("#lightOn input");
	var advancedMode = document.querySelector("#advancedOn input");

	lightMode.addEventListener("click", changeToLight, false);

	function changeToLight() {
		if (lightMode.checked == true) {
			parentBody.setAttribute("class", "light");
			frameBody.setAttribute("class", "light");
		} else {
			parentBody.removeAttribute("class");
			frameBody.removeAttribute("class");
		}
	}

}, false);