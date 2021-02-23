var password = document.getElementById("inputPassword");
var confirmPassword = document.getElementById("confirmPassword");
password.onkeyup = function() {
	if (password.value.length < 8) {
		document.getElementById("isPasswordValid").innerHTML = "Password should be at least 8 charachers long";
	}
	else {
		document.getElementById("isPasswordValid").innerHTML = "";
	}
};

document.getElementById("registerSubmit").onsubmit = function() {
	//if (password != confirmPassword) {
		alert("Password not match");
	//}
};


