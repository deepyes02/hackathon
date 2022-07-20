function returnBigInt(arr) {
	let bigCalculations = calculations.map(element=> BigInt(element))
	let sum = BigInt(0);

	bigCalculations.forEach(element => {
		sum += element;
	});
	return sum;
}


let calculations = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005];
returnBigInt(calculations);
console.log("end of code");