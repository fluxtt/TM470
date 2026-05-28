function openModal() {
	document.getElementById("transactionModal").style.display = "block";
}

function closeModal() {
	document.getElementById("transactionModal").style.display = "none";
}

function updateCurrentQuantity() {
	const select = document.getElementById("itemSelect");

	const selectedOption = select.options[select.selectedIndex];
	const quantity = parseInt(selectedOption.dataset.quantity || 0);

	document.getElementById("currentQuantity").value = quantity;

	calculateNewQuantity();
}

function calculateNewQuantity() {
	const current =
		parseInt(document.getElementById("currentQuantity").value) || 0;
	const adjustment = parseInt(document.getElementById("adjustment").value) || 0;

	const newQuantity = current + adjustment;

	document.getElementById("newQuantity").value = newQuantity;
}
