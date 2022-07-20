function diagonalDifference(arr) {
	let sum_of_left_to_right = 0;
	let sum_of_right_to_left = 0;
	for(let x=0; x<arr.length; x++){
		sum_of_left_to_right = sum_of_left_to_right + arr[x][x];
		sum_of_right_to_left = sum_of_right_to_left + arr[x][arr.length - x - 1];
		console.log(arr[x][arr.length - x - 1])
	}
	sum_of_left_to_right = parseInt(sum_of_left_to_right);
	sum_of_right_to_left = parseInt(sum_of_right_to_left);
	// return sum_of_left_to_right;
	// return [sum_of_right_to_left, sum_of_left_to_right];
return sum_of_left_to_right >= sum_of_right_to_left ? sum_of_left_to_right - sum_of_right_to_left : sum_of_right_to_left - sum_of_left_to_right;

}
const arr_1 = [1, 2, 3];
const arr_2 = [4, 5, 6];
const arr_3 = [9, 8, 9];

diagonalDifference([arr_1, arr_2, arr_3]);

console.log("end of code");