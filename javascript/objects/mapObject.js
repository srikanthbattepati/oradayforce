//const testObj=require('./testObject.js');

function mapObject(obj, callBack) {
    
  
    for (let key in obj) 
    {
      
        obj[key] = callBack(obj[key]);
      
    }
  
    return obj;
  }

module.exports=mapObject;