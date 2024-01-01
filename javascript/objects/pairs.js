//const testObj =require('./testObject.js')
function pairObj(obj) {
    const pairArray = [];
    
    for (let key in obj) 
    {
        tempArray=[];
      tempArray.push(key);
      tempArray.push(obj[key]);

      pairArray.push(tempArray);
    }
    
  
    return pairArray;
  }
//console.log(pairObj(testObj));
module.exports=pairObj;