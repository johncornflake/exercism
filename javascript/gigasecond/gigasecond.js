export const gigasecond = (dt) => {
    var start = dt.getTime();
    return new Date(start + (1000 * Math.pow(10, 9)));
};
