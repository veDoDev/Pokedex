document.addEventListener("DOMContentLoaded", () => {
    // Add hover effects for Pokémon cards
    const pokemonCards = document.querySelectorAll(".pokemon-card")
  
    pokemonCards.forEach((card) => {
      card.addEventListener("mouseenter", function () {
        this.style.transform = "translateY(-5px)"
        this.style.boxShadow = "0 5px 15px rgba(0, 0, 0, 0.2)"
      })
  
      card.addEventListener("mouseleave", function () {
        this.style.transform = "translateY(0)"
        this.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.1)"
      })
    })
  
    // Toggle advanced search section
    const toggleButton = document.getElementById("toggle-advanced-search")
    const advancedSearch = document.getElementById("advanced-search")
  
    if (toggleButton && advancedSearch) {
      toggleButton.addEventListener("click", () => {
        const isHidden = advancedSearch.style.display === "none"
        advancedSearch.style.display = isHidden ? "block" : "none"
        toggleButton.innerHTML = isHidden
          ? 'Hide Advanced Search <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="chevron-up"><polyline points="18 15 12 9 6 15"></polyline></svg>'
          : 'Show Advanced Search <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="chevron-down"><polyline points="6 9 12 15 18 9"></polyline></svg>'
      })
    }
  
    // Toggle sort dropdown
    const sortButton = document.querySelector(".sort-button")
    const sortOptions = document.querySelector(".sort-options")
  
    if (sortButton && sortOptions) {
      sortButton.addEventListener("click", () => {
        const isHidden = sortOptions.style.display === "none"
        sortOptions.style.display = isHidden ? "block" : "none"
      })
  
      // Close dropdown when clicking outside
      document.addEventListener("click", (event) => {
        if (!sortButton.contains(event.target) && !sortOptions.contains(event.target)) {
          sortOptions.style.display = "none"
        }
      })
    }
  
    // Surprise Me button functionality
    const surpriseButton = document.querySelector(".surprise-button")
  
    if (surpriseButton) {
      surpriseButton.addEventListener("click", () => {
        // Generate a random Pokémon ID between 1 and 251
        const randomId = Math.floor(Math.random() * 251) + 1
        window.location.href = `/pokemon/${randomId}/`
      })
    }
  
    // Search form validation
    const searchForm = document.querySelector(".search-form")
  
    if (searchForm) {
      searchForm.addEventListener("submit", function (e) {
        const searchInput = this.querySelector('input[name="search"]')
        if (searchInput.value.trim() === "") {
          e.preventDefault()
          searchInput.focus()
          // Add a subtle shake animation
          searchInput.classList.add("shake")
          setTimeout(() => {
            searchInput.classList.remove("shake")
          }, 500)
        }
      })
    }
  })
  
  // Add a CSS class for the shake animation
  const style = document.createElement("style")
  style.textContent = `
  @keyframes shake {
      0%, 100% { transform: translateX(0); }
      10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
      20%, 40%, 60%, 80% { transform: translateX(5px); }
  }
  .shake {
      animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
  }
  `
  document.head.appendChild(style)
  