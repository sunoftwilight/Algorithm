function solution(array) {
    function compare(a, b) {
        return a - b;
    }
    
    array.sort(compare);
    
    var answer = array[Math.floor(array.length / 2)];
    return answer;
}