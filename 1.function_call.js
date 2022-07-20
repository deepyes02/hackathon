const person = {
	sayFullName: function () {
		return this.firstName + ' ' + this.lastName;
	}
}

const person1 = {
	firstName: "Deepesh",
	lastName: "Dhakal"
}

const person2 = {
	firstName: "Radhika", lastName: "Ghimire"
}
person.sayFullName.call(person1)