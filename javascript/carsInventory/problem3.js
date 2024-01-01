
const carSort = (inventory) => {
    if (!Array.isArray(inventory) || inventory.length === 0) {
        return
    }
    if (inventory ==null || inventory ==undefined){
      return
    }
    let sortedArray  = inventory.sort(function (a, b) {
        if (a.car_model.toLowerCase()<b.car_model.toLowerCase() ) {
          return -1;
        }
        if (a.car_model.toLowerCase()> b.car_model.toLowerCase() ) {
          return 1;
        }
        return 0;
      });
    return sortedArray
    
}

module.exports = carSort

