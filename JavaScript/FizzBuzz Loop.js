var numbers = 0
while(numbers <= 99){
    numbers++
    if(numbers % 3 == 0){
        if(numbers % 5 == 0){
            console.log("FizzBuzz")
        }
    }
            if(numbers % 3 == 0){
                if(!(numbers % 5 == 0)){
                console.log("Fizz")
                }
            }
            if(numbers % 5 == 0){
                if(!(numbers % 3 == 0)){
                console.log("Buzz")
                }
            }
    console.log(numbers)
}