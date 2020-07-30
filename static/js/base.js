$(document).ready(function() {
    $(".navbar-burger").click(function() {
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});

var max_fields = 10;
var container = $(".ingredient-field");
var add_button = $("#add_ingredient_field");
var x = 1;

$(add_button).click(function(e) {
    e.preventDefault();
    if (x < max_fields) {
    x++;
    $(container).append('<br><div class="field-body is-fullwidth" id="ingredient_'+(x)+'"><div class="field has-addons "><p class="control is-expanded"><input id="ingeredients_'+(x)+'" name="ingredients_'+(x)+'" class="input is-info is-hovered" type="text" placeholder="Ingredient Item '+(x)+'"/></p><div class="control"><button type="submit" class="button is-link delete-ingredient"><i class="far fa-trash-alt "></i></a></button></div><a class="level-item"><div>');
//add input box
    } else {
    alert('You reached the ingredient limit')
    }

    $(container).on("click", ".delete-ingredient", function(e) {
            e.preventDefault();
            $(this).parent('div').remove();
            x--;
        });
    });
});

