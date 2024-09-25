function solution(lines) {
    let countLine = new Array(201).fill(0);
    
    for (const line of lines) {        
        for (let i = line[0] + 100; i < line[1] + 100; i++) {
            countLine[i] += 1;
        }
    }
        
    return countLine.filter(el => el > 1).length;
}