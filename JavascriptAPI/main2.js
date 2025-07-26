const characterDisplay = document.getElementById("character-display");
const characterList = document.getElementById("character-list");
const Loading = document.getElementById("loading");
const radioButtons = document.querySelectorAll('input[name="character"]');

const baseUrl = "https://ihatov08.github.io/kimetsu_api/api/";
const classification = {
  hasira: "hashira.json",
  oni: "oni.json",
  kisatsutai: "kisatsutai.json",
  all: "all.json",
};

async function fetchCharacters(category) {
  showLoading(true);
  try {
    const response = await fetch(`${baseUrl}${classification[category]}`);
    const data = await response.json();
    console.log(data);
    displayCharacters(data);
  } catch (error) {
    console.error("エラーが発生しました");
  } finally {
    showLoading(false);
  }
}

function displayCharacters(data) {
  characterDisplay.innerHTML = "";
  data.forEach((char) => {
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `
      <h3>${char.name}</h3>
      <img src="https://ihatov08.github.io${char.image}" alt="${char.name}">
      <p>カテゴリ: ${char.category}</p>
    `;
    characterDisplay.appendChild(card);
  });
}

radioButtons.forEach((element) => {
  element.addEventListener("change", () => {
    fetchCharacters(element.value);
  });
});

function showLoading(toggle) {
  if (toggle) {
    Loading.style.display = "block";
  } else {
    Loading.style.display = "none";
  }
}
fetchCharacters("all");
