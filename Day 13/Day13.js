function part1(){
    // Load in file
    var fs = require('fs');
    var textByLine = fs.readFileSync('input.txt').toString().split("\n");

    // Seperate inputs
    var arrivaltime = textByLine[0];
    var busIDs = textByLine[1].toString().replace(/,x/g, "").split(","); // Split into array with only the busID

    var waitingTimes = [];
    busIDs.forEach(bus => waitingTimes.push((Math.ceil(arrivaltime/bus)*bus) - arrivaltime));

    var leastWaitingTime = Math.min(...waitingTimes)
    const findLeast = (number) => number == leastWaitingTime;
    var bestBusID = busIDs[waitingTimes.findIndex(findLeast)] // Get the busID for the bus with the least waiting time, available at the same index.

    return bestBusID*leastWaitingTime
}

function checkOffset(num, busID, offset){
    return num+offset == Math.ceil(num/busID)*busID
}

function part2(){
    // Load in file
    var fs = require('fs');
    var textByLine = fs.readFileSync('input.txt').toString().split("\n");
    var busIDs = textByLine[1].toString().replace(/,x/g, "").split(","); // Get only busID
    var timeOffsets = [];
    busIDs.forEach(bus => timeOffsets.push(textByLine[1].split(",").indexOf(bus))); //Get the offsets
    // Chinese remainder theorem, equation to solve that in javascript.
}

console.log(part1())
console.log(part2())