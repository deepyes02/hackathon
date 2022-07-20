var pokemon = {
    firstname: 'Pika',
    lastname: 'Chu ',
    getPokeName: function() {
        var fullname = this.firstname + ' ' + this.lastname;
        return fullname;
    }
};

var pokemonName = function() {
    return (this.getPokeName() + ', I choose you!');
};

let bindPokemon = pokemonName.bind(pokemon); // creates new object and binds pokemon. 'this' of pokemon === pokemon now
let callPokemon = pokemonName.call(pokemon);
let applyPokemon = pokemonName.apply(pokemon);

console.log(''); // 'Pika Chu I choose you!'