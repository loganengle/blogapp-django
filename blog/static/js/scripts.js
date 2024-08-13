// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const searchForm = document.getElementById('searchForm');

    // Handle the "clear" button in the search input field
    searchInput.addEventListener('input', function () {
        if (searchInput.value === '') {
            // When search input is cleared, redirect to home page
            window.location.href = searchForm.action;
        }
    });
});