export const setIsLoggedIn = (isLoggedIn) => {
    localStorage.setItem('isLoggedIn', isLoggedIn)
}

export const getIsLoggedIn = () => {
    return localStorage.getItem('isLoggedIn') === 'true'
}