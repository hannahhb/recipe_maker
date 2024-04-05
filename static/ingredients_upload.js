/* ==========================================
    SAVE TEXT INPUT
* ========================================== */
function saveRecipe(recipe) {
    // Here, you can save the recipe input to a database, localStorage, etc.
    console.log("Recipe saved:", recipe);
}

/* ==========================================
    HANDLE TEXT INPUT
* ========================================== */
function handleTextInput(input) {
    saveRecipe(input.value);
}

document.addEventListener("DOMContentLoaded", function() {
    // Get the text input element
    var recipeInput = document.getElementById('recipetext');
    
    // Add an event listener for changes in the input
    recipeInput.addEventListener('input', function() {
        handleTextInput(recipeInput);
    });
});
