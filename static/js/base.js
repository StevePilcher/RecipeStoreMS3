$(document).ready(function() {
    $(".navbar-burger").click(function() {
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});


/* Change category Icon for retrieved recipe
$( ".categoryname" ).each(function( index ) {
  console.log($( this ).text());
});

//for(var i=0; i<category.each; i++){
//    console.log(i)
//}
*/
$(".category_icon").each(function(index) {
    if ($(this).html() == "Breakfast") {
            $(this).replaceWith('<img class="recipecat" src="./static/images/breakfast.png"></img>');
        } else if ($('.category_icon').html() == "Lunch") {
            $(this).replaceWith('<img class="recipecat" src="./static/images/lunch.png"></img>');
        } else if ($('.category_icon').html() == "Dinner") {
            $(this).replaceWith('<img class="recipecat" src="./static/images/dinner.png"></img>');
        } else if ($('.category_icon').html() == "Brunch") {
            $(this).replaceWith('<img class="recipecat" src="./static/images/brunch.png"></img>');
        } else if ($('.category_icon').html() == "Dessert") {
            $(this).replaceWith('<img class="recipecat" src="./static/images/dessert.png"></img>');
        } else {
            $('.category_icon').replaceWith('<img class="recipecat" src="./static/images/baking.png"></img>');
    }
});


//console.log($('.category_icon').html())

/*
$('#categoryname').each(function(i, category) {
    if (category == "Breakfast") {
            $('#recipecat').attr('src' , 'static/images/breakfast.png');
        } else if (category == "Lunch") {
            $('#recipecat').attr('src' , 'static/images/lunch.png');
        } else if (category == "Dinner") {
            $('#recipecat').attr('src' , 'static/images/dinner.png');
        } else if (category == "Brunch") {
            $('#recipecat').attr('src' , 'static/images/brunch.png');
        } else if (category == "Dessert") {
            $('#recipecat').attr('src' , 'static/images/dessert.png');
        } else {
            $('#recipecat').attr('src' , 'static/images/baking.png');
        console.log(category);}});

/*
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
    });*/
});

