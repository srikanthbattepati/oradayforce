
const carId = (inventory,id) => {
    let result = []
    if (inventory == null || inventory == undefined){
        return result;
      }
    if (!Array.isArray(inventory)) {
        return result;
    }
    
    if (typeof id != 'number') {
        return result;
    }
    // for(let idx = 0;idx < inventory.length;idx++){
    //     if(inventory[idx].id == id){
           
    //        result[0] = inventory[idx];
    //        return result;
    //     }
        
    // }
    result= inventory.filter(c=>c.id==id)
    return result;
}

module.exports = carId;