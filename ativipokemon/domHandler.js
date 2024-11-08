export function renderPokemonCards(pokemonList, loadImage, loadPokemonDetails) {
    const pokemonCardsContainer = document.getElementById('pokemon-cards');
    pokemonCardsContainer.innerHTML = ''; // Limpa os cards anteriores

    pokemonList.forEach((pokemon, index) => {
        const card = document.createElement('div');
        card.classList.add('col-md-3', 'mb-4');
        card.innerHTML = `
            <div class="card h-100 shadow-sm pokemon-card">
                <div class="card-body text-center">
                    <h5 class="card-title">${pokemon.name}</h5>
                    <img id="pokemon-img-${index}" class="img-fluid mb-3" alt="${pokemon.name}" style="height: 150px; object-fit: contain;">
                    <button class="btn btn-custom" id="details-btn-${index}">Ver Detalhes</button>
                </div>
            </div>
        `;
        pokemonCardsContainer.appendChild(card);

        // Adiciona o evento de clique para abrir os detalhes
        const detailsBtn = document.getElementById(`details-btn-${index}`);
        detailsBtn.addEventListener('click', () => loadPokemonDetails(pokemon.url, pokemon.name));

        // Carrega a imagem do Pokémon
        loadImage(pokemon.url, index);
    });
}


export function renderPokemonDetails(pokemon, pokemonName) {
    const modalContent = document.getElementById('modal-content');
    modalContent.innerHTML = `
        <h4>${pokemonName}</h4>
        <p><strong>Altura:</strong> ${pokemon.height} decímetros</p>
        <p><strong>Peso:</strong> ${pokemon.weight} hectogramas</p>
        <p><strong>Habilidades:</strong> ${pokemon.abilities.map(ability => ability.ability.name).join(', ')}</p>
        <img src="${pokemon.sprites.front_default}" alt="${pokemonName}" class="img-fluid">
    `;
}
