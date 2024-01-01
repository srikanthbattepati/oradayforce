function invertObject(obj)
{
    let newObject={};
    for(let key in obj)
    {
        if(typeof obj[key]!=='function')
        {
            newObject[obj[key]]=key;
        }
    }
    return newObject
}

module.exports=invertObject;