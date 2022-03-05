// We wait for page load
document.addEventListener('DOMContentLoaded', function() {
	
	// Get relevant elements first
    var sideTabs = document.getElementsByClassName("sideLink");
    var iframe = document.getElementById("contentFrame");
    var overlay = document.getElementById("dialogOverlay");
    var addDialog = document.getElementById("addMod");
    var remDialog = document.getElementById("remMod");
    var cancelDialog = document.getElementsByClassName("canBtn");
    var radioLabel = document.querySelectorAll("#addMod label");
    var urlInput = document.querySelector("#addMod input[type='url']");
    var fileInputBtn = document.getElementById("fileFrontBtn");
    var fileSpan = document.getElementById("filePath");
    var filePath = document.querySelector("#filePath small");
    var fileInput = document.getElementById('fileInput');
    var addMod = document.querySelector("#addMod .actBtn");
    var currentFrame = (window.location.href).split("#");
    var radioURL = document.getElementById("radioURL");
    var radioFile = document.getElementById("radioFile");

	// We add radio listeners for the dialog windows
    for (let i = 0; i < radioLabel.length; i++) {
		radioLabel[i].addEventListener("click", disableInput, false);
    }

    // We check if the current page category is selected here
    if (currentFrame[1]) {
		changeActive(currentFrame[1]);
    }

    // We handle the actions of the file input front button here
    fileSpan.addEventListener("click", promptForFile, false);

    // We add the action for the "add mod" button here
    addMod.addEventListener("click", validateAndPrompt, false)

    // We remove the dialog and the overlays when clicking outside the dialogs
    overlay.addEventListener("click", hideDialogs, false);

    // We do the same for the cancel buttons of the dialogs
    cancelDialog[0].addEventListener("click", hideDialogs, false);
    cancelDialog[1].addEventListener("click", hideDialogs, false);

	// We add the "click" listeners to change the active tab
	for (let i = 0; i < sideTabs.length; i++) {
		sideTabs[i].addEventListener("click", activateCategory, false);
	}

	// We prompt for file dialog on selection here
	function promptForFile() {
		fileInput.click();
		fileInput.onchange = e => {
			var file = e.target.files[0].mozFullPath;
			filePath.innerHTML = file;
		}
	}

	function validateAndPrompt() {
		let radioValue = document.querySelector("#addMod input[type='radio']:checked").value;
		let isValidInput;
		let urlToUse;

		// We validate the input first
		if (radioValue == 1) {
			isValidInput = urlInput.checkValidity();
			urlToUse = urlInput.value;
		} else if (radioValue == 2) {
			if (fileInput.files.length > 0) {
				isValidInput = true;
				urlToUse = "file:///" + fileInput.files[0].mozFullPath;
			} else {
				isValidInput = false;
			}
		}

		if (isValidInput) {
			iframe.src = "./html/import-mod.html?source=" + urlToUse;
			hideDialogs();
		} else {
			alert("You need to enter a valid value on the input field.");
		}
	}

	// We disable inputs on radio change here
	function disableInput(event) {
		let radioClicked = event.target.querySelector('input[type="radio"]').value;
		if (radioClicked == 1) {
			fileSpan.setAttribute("disabled", true);
			fileInputBtn.setAttribute("disabled", true);
			fileSpan.style.pointerEvents = "none";
			urlInput.removeAttribute("disabled");
		} else if (radioClicked == 2) {
			urlInput.setAttribute("disabled", true);
			fileSpan.style.pointerEvents = "auto";
			fileSpan.removeAttribute("disabled");
			fileInputBtn.removeAttribute("disabled");
		}
	}

	// We hide the dialogs here
	function hideDialogs() {
		overlay.style.display = "none";
		addDialog.style.display = "none";
		remDialog.style.display = "none";
		urlInput.value = "";
		filePath.innerHTML = "Select a file..."
		fileInput.value = "";
		if (urlInput.hasAttribute("disabled")) {
			urlInput.removeAttribute("disabled");
			fileSpan.setAttribute("disabled", true);
			fileInputBtn.setAttribute("disabled", true);
			radioURL.checked = true;
		}
	}

	// We get the clicked event to trigger the category change here
	function activateCategory(event) {
		let element = event.target;
		changeActive(element);
	}

	// We change the selected category here
	function changeActive(element) {
		let currentActive = document.querySelector(".sideLink.active");
		let activeCategory;

		// We transform the different possible element versions here (if element is string)
		if (typeof element == "string") {			
			switch(element) {
				case "settings.html":
					activeCategory = "settingsLink";
					break;
				case "css.html":
					activeCategory = "cssLink";
					break;
				case "javascript.html":
					activeCategory = "jsLink";
					break;
				case "chrome.html":
					activeCategory = "chromeLink";
					break;
				case "about.html":
					activeCategory = "aboutLink";
					break;
				case "donate.html":
					activeCategory = "donateLink";
					break;
				default:
				activeCategory = "settingsLink";
			}

			// We activate the category from the current url of the iframe here
			if (activeCategory != currentActive.id) {
				currentActive.classList.remove("active");
				document.getElementById(activeCategory).classList.add("active");
			}

		// We transform the different possible element versions here (if element is node)
		} else {
			activeCategory = element.id;

			// We activate the category from the clicked element here 
			if (element != currentActive) {
				currentActive.classList.remove("active");
				element.classList.add("active");
			}
		}

		// We change the content of the iframe
		switch(activeCategory) {
			case "settingsLink":
				iframe.src = "./html/settings.html";
				window.location.href = currentFrame[0] + "#settings.html"
				break;
			case "cssLink":
				iframe.src = "./html/css.html";
				window.location.href = currentFrame[0] + "#css.html"
				break;
			case "jsLink":
				iframe.src = "./html/javascript.html";
				window.location.href = currentFrame[0] + "#javascript.html"
				break;
			case "aboutLink":
				iframe.src = "./html/about.html";
				window.location.href = currentFrame[0] + "#about.html"
				break;
			default:
				iframe.src = "./html/settings.html";
				window.location.href = currentFrame[0] + "#settings.html"
		}
	}

}, false);