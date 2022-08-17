let required = (properType) => {
    return v => v && v.length > 0 || `You must input a ${properType}`
}

let minLenght = (properType, minLenght) => {
    return v => v && v.length >= minLenght || `${properType} must be at least ${minLenght}`
}

let maxLenghth = (properType, maxLenghth) => {
    return v => v && v.length <= maxLenghth || `${properType} must be less than ${maxLenghth}`
}

let emailFormat = () => {
    let regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return v => v && regex.test(v) || "Must be a valid email"
}

export default{ required, minLenght, maxLenghth, emailFormat }