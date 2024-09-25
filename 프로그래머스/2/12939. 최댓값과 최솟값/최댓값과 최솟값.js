function solution(s) {
    var answer = '';
    
    const numArray = s.split(' ').map(el => Number(el));
    
    numArray.sort((a, b) => a - b);
    
    return `${numArray[0]} ${numArray[numArray.length - 1]}`;
}