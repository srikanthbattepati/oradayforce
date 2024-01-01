//const testObj =require('./testObject.js')
//console.log(testObj);
function values(obj) 
{
    const objValues = [];
    
    for (let key in obj) 
    {
        //console.log(typeof obj[key]!=='fuction')
        if(typeof obj[key]!=='function')
        {//console.log(obj[key]);
          objValues.push(obj[key]);
        }
    }
  
    return objValues;
}
//console.log(values(testObj));

module.exports=values;