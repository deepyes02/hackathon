const arr = [[1, 2, -3, 4], [1, 2, 3, 4, 5], [12, 23, 12, 32, 56, 78, 90]];


function returnsumofArr(arr) {
	// console.log(arr.length);
	let newArr = []
	for (let x = 0; x < arr.length; x++) {
		//inner_array
		let returnVal = arr[x].reduce(
			(total, current) => {
				return total + current
			})
		newArr.push(returnVal)
	}
	console.log(newArr)
}



returnsumofArr(arr)