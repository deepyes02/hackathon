const arr = [5, 4, 3, 7, 2, 1]
const sorted_arr = arr.sort((a, b) => a - b);
const min_sum = sorted_arr.slice(0, arr.length - 1).reduce((previous, current)=>previous + current)
const max_sum = sorted_arr.slice(1, arr.length).reduce((previous, current)=>previous + current)
console.log(min_sum+' '+max_sum);
console.log('end of code');