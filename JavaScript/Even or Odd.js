var oddEven = function (x) {
    if(x < 0){
        return "not a whole number"
        }
        if (x % 2 == 0) {
            return "even"
        }
        else {
            return "odd"
        }
}  
console.log(oddEven(-1))