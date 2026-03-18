const btn = document.getElementById("add")


btn.addEventListener("click", function(){
    fetch("/add_smth")
        .then(response => response.text())
        .then(text =>  console.log(text));
})



async function loadProducts() {

    //const response = await fetch('your-api-endpoint');
    var stuff = await fetch("/loadProducts")
        .then(response => response.json())
        .then(data =>  stuff = data);


    // Format retrieved data for displaying
    var products = [];
    stuff.forEach(row => {
        products.push({
            navn:       row[0],
            sku:        row[1], 
            lager:      row[2],
            lokation:   row[3]
        });
    });

    const tbody = document.getElementById('product-table-body');

    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><input type="checkbox"></td>
            <td>${product.navn}</td>
            <td>${product.sku}</td>
            <td>${product.lager}</td>
            <td>${getStatusBadge(product.lager)}</td>
            <td>${product.lokation}</td>
            <td><img src="images/delete.png" class="delete-icon"></td>
        `;

        row.querySelector('.delete-icon').addEventListener('click', () => {
            row.remove();
    });

        tbody.appendChild(row);

        
    });
}

function getStatusBadge(lager) {
    if (lager === 0) {
        return `<span class="badge udsolgt">● Udsolgt</span>`;
    } else if(lager <= 15){
        return `<span class="badge lav-lager">● Lav lager</span>`;
    } else {
        return `<span class="badge ok">● OK</span>`;
    } 
}

loadProducts();