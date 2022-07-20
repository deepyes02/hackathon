class Animal {
	constructor(fullName, numberOfLegs, sound) {
		this.fullName = fullName;
		this.numberOfLegs = numberOfLegs;
		this.sound = sound;
	}

	defineAnimal() {
		return "Hello I am a " + this.fullName + " and I have " + this.numberOfLegs + " legs";
	}

	introduce() {
		this.defineAnimal();
	}
}


const cow = new Animal("Kali", 4, "Moow");



console.log("End of file");