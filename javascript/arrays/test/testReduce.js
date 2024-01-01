//const testCase=require('./testCase.js');

function each(array,callBack)
{
    if(Array.isArray(array))
    {
        for(let index in array)
        {
            callBack(array[index],index,array);
            //console.log(callBack);
        }
    }else
    {
        return 0;
    }

}
module.exports=each;