const alice = [17, 28, 30];
const bob = [17, 28, 30];
function calculate_triplets(alice, bob) {
	let alice_score = bob_score = 0;

	for (let x = 0; x < alice.length; x++) {
		if (alice[x] > bob[x]) {
			alice_score += 1;
		} else if (alice[x] < bob[x]) {
			bob_score += 1;
		}
	}
	return alice_score+' '+bob_score;
}

const calculation = calculate_triplets(alice, bob);

console.log("End of code");