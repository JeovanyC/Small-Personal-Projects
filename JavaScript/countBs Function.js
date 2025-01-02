function countChar(s , l) {
    var counter = 0;
    for (i = 0; i < s.length; i++) {
        if (s.charAt(i) === l)
            counter++;
    }
    return counter;
}
console.log(countChar("kakkerlak", "k"))