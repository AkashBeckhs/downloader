
$(document).ready(function(){
    PopulateDropDownList();
})

function PopulateDropDownList() {
    var products = [
        { productId: 1, name: "Fanta", price: "4" },
        { productId: 2, name: "Coke", price: "2" },
        { productId: 3, name: "Sprite", price: "8" },
        { productId: 4, name: "Malta Guniness", price: "10" }
    ];

    select = document.getElementById('productsDropDown');
    for (var i = o; i <= products.length; i++) {
        var opt = document.createElement('option');
        opt.value = product[i].productId;
        opt.innerHTML = product[i].name;
        select.appendChild(opt);
    }


}