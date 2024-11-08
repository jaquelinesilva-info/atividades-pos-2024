import { fetchPokemon, fetchPokemonImage, fetchPokemonDetails } from './pokeApi.js';
import { renderPokemonCards, renderPokemonDetails } from './domHandler.js';

let currentPage = 1;

// Função para carregar os Pokémon
async function loadPokemon(page = 1) {
    try {
        const data = await fetchPokemon(page);
        renderPokemonCards(data, loadPokemonImage, loadPokemonDetails);

        // Controlar exibição dos botões de navegação
        document.getElementById('prev-page-btn').style.display = page > 1 ? 'block' : 'none';
        document.getElementById('next-page-btn').style.display = data.length === 20 ? 'block' : 'none';
    } catch (error) {
        console.error('Erro ao buscar os Pokémon:', error);
        alert('Não foi possível carregar os Pokémon.');
    }
}

// Função para carregar imagens dos Pokémon
async function loadPokemonImage(pokemonUrl, index) {
    try {
        const pokemon = await fetchPokemonImage(pokemonUrl);
        const imgElement = document.getElementById(`pokemon-img-${index}`);
        imgElement.src = pokemon.sprites.front_default;
    } catch (error) {
        console.error('Erro ao carregar a imagem do Pokémon:', error);
    }
}

// Função para carregar os detalhes de um Pokémon
async function loadPokemonDetails(pokemonUrl, pokemonName) {
    try {
        const pokemon = await fetchPokemonDetails(pokemonUrl);
        renderPokemonDetails(pokemon, pokemonName);

        // Exibe o modal com os detalhes
        const pokemonModal = new bootstrap.Modal(document.getElementById('pokemonModal'));
        pokemonModal.show();
    } catch (error) {
        console.error('Erro ao carregar os detalhes do Pokémon:', error);
        alert('Não foi possível carregar os detalhes do Pokémon.');
    }
}

// Delegação de eventos para capturar cliques nos botões "Ver Detalhes"
document.getElementById('pokemon-cards').addEventListener('click', function(event) {
    if (event.target && event.target.matches('button[data-pokemon-url]')) {
        const pokemonUrl = event.target.getAttribute('data-pokemon-url');
        const pokemonName = event.target.getAttribute('data-pokemon-name');
        loadPokemonDetails(pokemonUrl, pokemonName);
    }
});

// Função para carregar a próxima página
document.getElementById('next-page-btn').addEventListener('click', () => {
    currentPage++;
    loadPokemon(currentPage);
});

// Função para carregar a página anterior
document.getElementById('prev-page-btn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        loadPokemon(currentPage);
    }
});



// Carregar os Pokémon ao inicializar a página
loadPokemon(currentPage);
