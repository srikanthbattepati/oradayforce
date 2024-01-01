
let carYearArray = []

const carYear = (inventory) => {
    if (!Array.isArray(inventory) || inventory.length === 0) {
        return carYearArray
    }
    if ( inventory == null || inventory == undefined) {
        return carYearArray
    }

    for(let idx =0;idx<inventory.length;idx++){
        carYearArray.push(inventory[idx].car_year)
    }
    // carYearArray=inventory.map(c=>c.car_year);

    return carYearArray;
}

module.exports = carYear