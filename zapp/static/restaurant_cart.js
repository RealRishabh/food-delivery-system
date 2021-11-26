if(localStorage.getItem('cart') == null){
    var cart = {};
}else{
    cart = JSON.parse(localStorage.getItem('cart'));
    var totalItem = 0;
    var itemInCart = Object.values(cart)
        for (let item of itemInCart) {
            totalItem += item;
        }
    document.getElementById('cart').innerHTML = totalItem;
}

$('.cart').click(function(){
    var dish = this.id.toString();
    if(cart[dish] != undefined){
        cart[dish] += 1;
    }else{
        cart[dish] = 1;
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    var totalItem = 0;
    var itemInCart = Object.values(cart)
        for (let item of itemInCart) {
            totalItem += item;
        }
    document.getElementById('cart').innerHTML = totalItem;
});
$('#popcart').popover();


updatePopover(cart);
function updatePopover(cart)
{
    var popStr = "";
    popStr = popStr + "<h5> Cart </h5><div class='mx-2 my-2'>";
    var i = 1;
    for (var item in cart){
        popStr = popStr + "<b>" + i + "</b>. ";
        popStr = popStr + item + " × " + cart[item] + '<br>';
        i = i+1;
    }
    popStr = popStr + "</div> <a href='checkout{{ rest_dish[0].dish_restaurant_name }}'><button class='btn btn-primary' id ='checkout'>Checkout</button></a> <button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>"
    popStr = popStr + "</div>" 
    document.getElementById('popcart').setAttribute('data-content', popStr);
    $('#popcart').popover('show');
}

function updateCart(cart) {
    var sum = 0;
    for (var item in cart) {
        sum = sum + cart[item];
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = sum;
    updatePopover(cart);
}

$(".addcart").click(function(){
    updateCart(cart);
});

function clearCart() {
    localStorage.clear();
    cart = {};
    updateCart(cart);
}