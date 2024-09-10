// app.js
const API_URL = 'http://127.0.0.1:5000'; 
document.addEventListener('DOMContentLoaded', () => {
    const gridContainer = document.querySelector('.grid-container');
    const filterSelect = document.getElementById('category-filter');
    const searchInput = document.getElementById('search-input');
    const prevPageBtn = document.getElementById('prev-page');
    const nextPageBtn = document.getElementById('next-page');
    const currentPageSpan = document.getElementById('current-page');
    const totalPagesSpan = document.getElementById('total-pages');

    let currentPage = 1;
    let totalPages = 1;
    let itemsPerPage = 12;

    // Simulated data loading
    loadProducts();

    // Event listeners
    filterSelect.addEventListener('change', updateGrid);
    searchInput.addEventListener('input', updateGrid);

    prevPageBtn.addEventListener('click', handlePagination);
    nextPageBtn.addEventListener('click', handlePagination);

    function loadProducts() {
        // In a real application, this would fetch data from an API
        const products = [
            { id: 1, name: 'Apple', category: 'Fruits' },
            { id: 2, name: 'Carrot', category: 'Vegetables' },
            { id: 3, name: 'milk', category: 'Dairy'}
            // ... add more products
        ];

        totalPages = Math.ceil(products.length / itemsPerPage);
        updateGrid();
    }

    function updateGrid() {
        const filteredProducts = getFilteredProducts(Products);
        renderProducts(filteredProducts);
    }

    function getFilteredProducts() {
        const selectedCategory = filterSelect.value;
        const searchQuery = searchInput.value.toLowerCase();

        return products.filter(product => 
            (selectedCategory === '' || product.category === selectedCategory) &&
            product.name.toLowerCase().includes(searchQuery)
        );
    }
    function loadProducts() {
        fetch(`${API_URL}/products`)
          .then(response => response.json())
          .then(products => {
              totalPages = Math.ceil(products.length / itemsPerPage);
              updateGrid(products);
          })
          .catch(error => console.error('Error fetching products:', error));
    }
    

    function renderProducts(products) {
        gridContainer.innerHTML = '';
        const paginatedProducts = products.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
        paginatedProducts.forEach(product => {
            const item = document.createElement('div');
            item.className = 'product-item';
            item.innerHTML = `
                <img src="../static/images/${product.image}.jpg" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>Price: $${product.price.toFixed(2)}</p>
        `   ;
            gridContainer.appendChild(item);
        });
    }
    

    function handlePagination(e) {
        const target = e.target;
        if (target.id === 'prev-page') {
            currentPage > 1 ? currentPage-- : null;
        } else if (target.id === 'next-page') {
            currentPage < totalPages ? currentPage++ : null;
        }

        updatePageDisplay();
        updateGrid();
    }

    function updatePageDisplay() {
        currentPageSpan.textContent = currentPage;
        totalPagesSpan.textContent = totalPages;
    }
});

