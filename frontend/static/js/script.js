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
    
    // Define the card template
    const cardTemplate = `
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

    // Set up a variable to hold the generated HTML
    let cardsHTML = `<div class="querywrapper"><p>Displaying results for: ${query}</p></div><div class="cardgrid">`;

    // Generate X amount of cards (for example, 8 cards)
    const numberOfCards = 30;
    for (let i = 0; i < numberOfCards; i++) {
        cardsHTML += cardTemplate;
    }

    // Close the card grid container
    cardsHTML += `</div>`;

    // Set the generated HTML inside the results container
    resultsContainer.innerHTML = cardsHTML;
}
