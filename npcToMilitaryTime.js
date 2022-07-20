const time = '12:00:30AM';

let newTime;
const am_pm = time.slice(8, 10);
const hours = time.slice(0, 2);
if (am_pm.toLowerCase() == 'pm') {
	if (hours == 12) {
		newTime = time.slice(0, time.length - 2);
	} else {
		newTime = time.replace(hours, parseInt(hours) + parseInt(12)).slice(0, time.length - 2);
	}
} else if ((am_pm.toLowerCase() == 'am')) {
	if (hours == 12) {
		newTime = time.replace(hours, '00').slice(0, time.length - 2);
	} else {
		newTime = time.slice(0, time.length - 2);
	}
} 
console.log("End of code");