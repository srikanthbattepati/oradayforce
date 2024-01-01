function defaultObj(obj, defaultObject)
{
    for(let key in defaultObject)
    {
        if(obj[key]===null || (key in obj)===key || obj[key]===undefined || obj[key]==='')
        {
                obj[key]=defaultObject[key];
        }
    }
    return obj;
}

module.exports=defaultObj;