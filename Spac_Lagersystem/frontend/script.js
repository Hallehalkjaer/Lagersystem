async function loadProducts() {

    //const response = await fetch('your-api-endpoint');
    const products = [
        { navn: "Sko", sku: "22341", lager: 52, status: "OK", lokation: "Ballerup" },
        { navn: "T-shirt", sku: "88321", lager: 10, status: "Lav lager", lokation: "Odense" },
        { navn: "Jakke #1", sku: "55321", lager: 200, status: "OK", lokation: "Aarhus" },
        { navn: "Bukser", sku: "25321", lager: 0, status: "Udsolgt", lokation: "København" },
        { navn: "Undertøj", sku: "78321", lager: 300, status: "OK", lokation: "Ballerup" },
    ];;

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