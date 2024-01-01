let testObj=require('../testObject.js')
let keyFuction=require('../keys.js')
//const testObject = { name: 'Bruce Wayne', age: 36, location: 'Gotham' };

const testKey=keyFuction(testObj);
console.log(testKey);
