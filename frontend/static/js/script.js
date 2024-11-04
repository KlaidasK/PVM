function performSearch(event) {
    event.preventDefault(); // Prevent form submission
    const searchInput = document.querySelector('.search-container input[name="search"]').value;

    if (searchInput) {
        // Hide recommended teams and show search results by adding/removing classes
        document.querySelector('.presearch').classList.add('hidden');
        document.querySelector('.postsearch').classList.remove('hidden');

        // Display placeholder search results
        displaySearchResults(searchInput);
    }
}

function displaySearchResults(query) {
    const resultsContainer = document.querySelector('.results-container');
    
    // Placeholder content to simulate search results
    resultsContainer.innerHTML = `
        <p>Displaying results for "${query}":</p>
        <div class="card">
            <div class="card-header">
                <p>Looking for: Developer</p>
                <p class="title"><span>Web Development Team</span></p>
            </div>
            <div class="card-content">
                <p>Team activity: Moderate</p>
                <p>Members: 8</p>
                <div class="activity-dots">
                    <span></span><span></span><span></span>
                </div>
                <div class="arrow">&gt;</div>
            </div>
        </div>
        <div class="card">
            <div class="card-header">
                <p>Looking for: Designer</p>
                <p class="title"><span>UI/UX Design Team</span></p>
            </div>
            <div class="card-content">
                <p>Team activity: High</p>
                <p>Members: 10</p>
                <div class="activity-dots">
                    <span></span><span></span><span></span>
                </div>
                <div class="arrow">&gt;</div>
            </div>
        </div>
    `;
}
