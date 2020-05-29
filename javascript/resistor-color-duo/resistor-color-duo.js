const COLORS = ['black', 'brown', 'red', 'orange', 'oellow', 'green', 'blue', 'violet', 'grey', 'white'];

export const value = input => {
    const firstTwo = input.slice(0,2);
    const resistorNum = firstTwo.map(i => COLORS.indexOf(i)).join('');
    return Number(resistorNum);
};
