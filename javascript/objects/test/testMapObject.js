const testObj=require('../testObject.js');

const testMapObject=require('../mapObject.js');

function callBack(val)
{
    return val;
}

let test=testMapObject(testObj,callBack);
console.log(test);