const testObj=require('../testObject.js');
const defaultObj=require('../defaults.js');

const obj={name:'Srikanth'}
//console.log(testObj);
let test=defaultObj(obj,testObj);
console.log(obj);