// products.js
const API_URL = ''; // Use relative path since frontend and backend are on the same domain

// Function to load products
function loadProducts() {
    fetch(`${API_URL}/products`)
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            content.innerHTML = data.map(product => `
                <div class="product-item">
                    <img src="${product.image_url || 'default-image.jpg'}" alt="${product.name}">
                    <h3>${product.name}</h3>
                    <p>${product.description}</p>
                    <p>Price: $${product.price}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error fetching products:', error));
}

// Function to show the Add Product form
function showProductForm() {
    const content = document.getElementById('content');
    content.innerHTML = `
        <h2>Add Product</h2>
        <form id="add-product-form">
            <input type="text" name="name" placeholder="Name" required><br>
            <input type="text" name="description" placeholder="Description" required><br>
            <input type="number" name="price" placeholder="Price" required><br>
            <input type="text" name="image_url" placeholder="Image URL" required><br>
            <button type="submit">Submit</button>
        </form>
    `;
    
    // Attach event listener to the form
    document.getElementById('add-product-form').addEventListener('submit', addProduct);
}

// Function to add a new product
function addProduct(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData);
    
    fetch(`${API_URL}/products`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadProducts(); // Refresh the product list
    })
    .catch(error => console.error('Error adding product:', error));
}

// Attach event listeners to the buttons
document.getElementById('view-products').addEventListener('click', loadProducts);
document.getElementById('view-products').insertAdjacentHTML('afterend', '<button id="add-product-button">Add Product</button>');
document.getElementById('add-product-button').addEventListener('click', showProductForm);

