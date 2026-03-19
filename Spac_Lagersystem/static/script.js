const btn = document.getElementById("add");
const addModalOverlay = document.getElementById("add-modal-overlay");
const modalCancel = document.getElementById("modal-cancel");
const modalSubmit = document.getElementById("modal-submit");


btn.addEventListener("click", function () {
    addModalOverlay.classList.add("active");
});

modalCancel.addEventListener("click", function () {
    addModalOverlay.classList.remove("active");
});

addModalOverlay.addEventListener("click", function (e) {
    if (e.target === addModalOverlay) {
        addModalOverlay.classList.remove("active");
    }
});


modalSubmit.addEventListener("click", async function () {
    const navn     = document.getElementById("input-navn").value;
    const sku      = parseInt(document.getElementById("input-sku").value);
    const lager    = parseInt(document.getElementById("input-lager").value);
    const lokation = document.getElementById("input-lokation").value;

    if (!navn || !sku || isNaN(lager) || !lokation) {
        alert("Udfyld venligst alle felter!");
        return;
    }

    const response = await fetch("/addProduct", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ navn, sku, lager, lokation })
    });

    if (response.ok) {
        addModalOverlay.classList.remove("active");
        location.reload();
    } else {
        alert("Kunne ikke tilføje produktet!");
    }
});

async function loadProducts() {
    var stuff = await fetch("/loadProducts")
        .then(response => response.json())
        .then(data => stuff = data);

    var products = [];
    stuff.forEach(row => {
        products.push({
            navn:     row[0],
            sku:      row[1],
            lager:    row[2],
            lokation: row[3]
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
            fetch(`/deleteProduct/${product.sku}`, { method: "DELETE" })
                .then(response => {
                    if (response.ok) {
                        row.remove();
                    } else {
                        alert("Kunne ikke slette produktet!");
                    }
                });
        });

        tbody.appendChild(row);
    });
}

function getStatusBadge(lager) {
    if (lager === 0) {
        return `<span class="badge udsolgt">● Udsolgt</span>`;
    } else if (lager <= 15) {
        return `<span class="badge lav-lager">● Lav lager</span>`;
    } else {
        return `<span class="badge ok">● OK</span>`;
    }
}

loadProducts();