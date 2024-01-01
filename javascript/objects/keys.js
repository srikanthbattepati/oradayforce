//const testObj =require('./testObject.js')
function keys(obj) {
    const propertyNames = [];
    
    for (let key in obj) {
      if (obj.hasOwnProperty(key)) {
        propertyNames.push(key);
      }
    }
  
    return propertyNames;
  }
module.exports=keys;