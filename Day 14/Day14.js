function dec2bin(dec){
    var binary = (dec >>> 0).toString(2)
    while(binary.length < 36){
        binary = "0" + binary
    }
    return binary;
} 

function applyMaskToValue(mask, binary){
    var newBinary = ""
    for(var i = 0; i < mask.length; i++){
        if(mask.charAt(i) != "X"){
            newBinary+= mask.charAt(i);   
        } else {
            newBinary+=binary.charAt(i)
        }
    }
    return newBinary;
}

function applyMaskToAddres(mask, address){
    var newAddress = ""
    for(var i = 0; i < mask.length; i++){
        if(mask.charAt(i) == "0"){
            newAddress+=address.charAt(i)
        } else {
            newAddress+=mask.charAt(i);
        }
    }
    return newAddress;
}

function part1(){
    var fs = require('fs');
    var textInput = fs.readFileSync('input.txt').toString().split("mask = ");
    var textChunks = []
    textInput.forEach(element => {
        textChunks.push(element.split("\n"))
    });
    textChunks.shift()
    var memory = []
    textChunks.forEach(chunk => { // for each chunk containing a mask and the following commands
        var mask = chunk.shift().toString() // Remove the mask
        chunk.forEach( element => {
            var both = element.toString().split("] = ")
            var address = both[0].replace("mem[", "")
            var value = dec2bin(both[1])
            memory[address] = parseInt(applyMaskToValue(mask, value), 2);
        })
    });
    var sum = 0;
    memory.forEach(element => {
        sum += parseInt(element);
    })
    return sum
}

function writeToMemory(address, value, array){
    if(value){ // remove weird parsing issues with new lines
        if(address.indexOf('X') != -1) {
                writeToMemory(address.replace('X', '0'), value, array)
                writeToMemory(address.replace('X', '1'), value, array)
            } else {
                array[parseInt(address, 2)] = value;
            }
    }
}

function part2(){
    var fs = require('fs');
    var textInput = fs.readFileSync('input2.txt').toString().split("mask = ");
    var textChunks = []
    textInput.forEach(element => {
        textChunks.push(element.split("\n"))
    });
    textChunks.shift()
    var memory = []
    textChunks.forEach(chunk => { // for each chunk containing a mask and the following commands
        var mask = chunk.shift().toString() // Remove the mask
        chunk.forEach( element => {
            var both = element.toString().split("] = ")
            var address = dec2bin(both[0].replace("mem[", ""))
            var value = parseInt(both[1])
            writeToMemory(applyMaskToAddres(mask, address), value, memory)
        })
    });
    var sum = 0;
    memory.forEach(element => {
        sum += element;
    })
    return sum
}
console.log(part1())
console.log(part2())  //Works with input2.txt, but regular input results in 0. Array does not seem to update