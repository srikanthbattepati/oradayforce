

let carBrandArray = []

const carBrand = (b1,b2,inventory) => {

    if (!Array.isArray(inventory) || inventory.length === 0) {
        return
    }
    if (inventory ==null || inventory ==undefined){
      return
    }

    let found = false;
    // for(let idx =1;idx <inventory.length;idx++){
    //     if(inventory[idx].car_make ==b1 | inventory[idx].car_make ==b2){
    //         carBrandArray.push(` modal : ${inventory[idx].car_model} ,car make : ${inventory[idx].car_make} ,year : ${inventory[idx].car_year}`)
    //     }
    // }
    carBrandArray=inventory.filter(c=>(c.car_make== b1|c.car_make==b2)).map(c=>c);

    return JSON.stringify(carBrandArray)
}

module.exports = carBrand
