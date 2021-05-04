process.stdin.resume();
process.stdin.setEncoding('utf8');
 
// your code goes here
 
const coordinates = [
	[
		[
			[128.25102850494045,35.2218726568253],
			[128.2510682508522,35.22174302304637],
			[128.25109473156576,35.22144358857119],
			[128.25108211971454,35.22133409021277],
			[128.2510642530481,35.22099598463809],
			[128.25104584785123,35.22097892575142],
			[128.25073006116577,35.22179103979821],
			[128.25102850494045,35.2218726568253]
		]
	]
]
 
const result = 1685.8000000000
function toRadians(v) {
	return v * (Math.PI / 180);
}
 
const R = 6371; // radius of the Earth km
// const R = 3959; // radius of the Earth square miles
const length = coordinates[0][0].length;
console.log(length);
const data = coordinates[0][0];
let area = 0;
for (var i =0; i < length - 1; i++) {
	const p1 = data[i];
	const p2 = data[i + 1];
	area += toRadians(p2[0] - p1[0]) * (
		2 + 
		Math.sin(toRadians(p1[1])) + 
		Math.sin(toRadians(p2[1]))
	);
}
 
area = area * R * R  / 2;
const res = Math.round(area * 10000000) / 10;
console.log(`Returned result from API: ${result}`);
console.log(`Got value from formular: ${res}`);
