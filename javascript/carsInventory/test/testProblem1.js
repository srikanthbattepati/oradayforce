let inventory = require('../cars.js')

let problem1 = require('../problem1.js')

let ans = problem1(inventory, 33)
if (ans.length > 0){
            console.log(`car model is ${ans[0].car_year} ${ans[0].car_make} ${ans[0].car_model} `)
            
}