let carOldArray = []

let oldCar = (carYear) => {
    if (!Array.isArray(carYear) || carYear.length === 0) {
        return carOldArray
    }
    if (carYear ==null || carYear ==undefined){
      return carOldArray
    }

    // for(let idx =1;idx<carYear.length;idx++){
    //     if(carYear[idx]<2000){
    //         carOldArray.push(carYear[idx])
    //     }
        
    // }

    carOldArray=carYear.filter(c=>c<2000).map(c=>c);
    return (carOldArray);
}

module.exports = oldCar