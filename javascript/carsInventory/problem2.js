

const lastCar = (inventory) => {
    if (!Array.isArray(inventory) || inventory.length === 0) {
        return
    }
    if (inventory ==null || inventory ==undefined){
      return
    }
    // for(let idx =1;idx<=inventory.length;idx++){
    //     if(idx==inventory.length-1){
    //         console.log(`Last car is a car make ${inventory[idx].car_make} and car year is ${inventory[idx].car_model}`)
    //         break
    //     }
    // }

    result=inventory.filter(c => c.id==(inventory.length-1));
    console.log(`Last car is a car make ${result[0].car_make} and car year is ${result[0].car_model}`);
}

module.exports = lastCar