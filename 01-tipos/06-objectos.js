// Objects
let character = {
    name: "person",
    anime: "srx",
    age: 22
};

console.log(character);
console.log(character.name);
console.log(character['anime']);

character.age = 23;

let llave = 'value';
character[llave] = 24;

delete character.anime;

console.log(character);