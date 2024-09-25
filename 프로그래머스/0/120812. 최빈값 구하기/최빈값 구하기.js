function solution(array) {
    var answer = 0;
    var freq = 0;
    var isSame = false;
    
    array.sort();
    
    let tmp = 0;
    for (let i = 0; i < array.length ; i += tmp) {
        tmp = array.filter(x => x === array[i]).length;
        
        if (freq === tmp) isSame = true;
        else if (freq < tmp) {
            isSame = false;
            freq = tmp;
            answer = array[i];
        }
    }

    if (isSame) return -1
    
    return answer;
}