function solution(common) {
    const ptrn1 = common[2] - common[1];
    const ptrn2 = common[1] - common[0];
    
    if (ptrn1 === ptrn2) return common[common.length - 1] + ptrn1;
    else return common[common.length - 1] * (common[2] / common[1]);
}