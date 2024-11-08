// src/main.js
import { fetchPokemon, fetchPokemonImage, fetchPokemonDetails } from './pokeApi.js';
import { renderPokemonCards, renderPokemonDetails } from './domHandler.js';

let currentPage = 1;

async function loadPokemon(page = 1) {
    try {
        const data = await fetchPokemon(page);
        renderPokemonCards(data, loadPokemonImage, loadPokemonDetails);
        document.getElementById('prev-page-btn').style.display = page > 1 ? 'block' : 'none';
    } catch (error) {
        console.error('Erro ao buscar os Pokémon:', error);
        alert('Não foi possível carregar os Pokémon.');
    }
}

async function loadPokemonImage(pokemonUrl, index) {
    try {
        const pokemon = await fetchPokemonImage(pokemonUrl);
        const imgElement = document.getElementById(`pokemon-img-${index}`);
        imgElement.src = pokemon.sprites.front_default;
    } catch (error) {
        console.error('Erro ao carregar a imagem do Pokémon:', error);
    }
}

async function loadPokemonDetails(pokemonUrl, pokemonName) {
    try {
        const pokemon = await fetchPokemonDetails(pokemonUrl);
        renderPokemonDetails(pokemon, pokemonName);

        const pokemonModal = new bootstrap.Modal(document.getElementById('pokemonModal'));
        pokemonModal.show();
    } catch (error) {
        console.error('Erro ao carregar os detalhes do Pokémon:', error);
        alert('Não foi possível carregar os detalhes do Pokémon.');
    }
}

document.getElementById('next-page-btn').addEventListener('click', () => {
    currentPage++;
    loadPokemon(currentPage);
});

document.getElementById('prev-page-btn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        loadPokemon(currentPage);
    }
});

// carregar pokémon na inicialização
loadPokemon(currentPage);
