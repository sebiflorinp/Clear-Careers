import {useState} from "react";
function useValidators() {
    const [isLoginEmailValid, setIsLoginEmailValid] = useState(false)
    const [isLoginPasswordValid, setIsLoginPasswordValid] = useState(false)
    const [isEmailValid, setIsEmailValid] = useState(false)
    const [isPasswordValid, setIsPasswordValid] = useState(false)

    function checkLoginEmail(loginEmail) {
        if (loginEmail !== "")
            setIsLoginEmailValid(true)
        setIsLoginEmailValid(false)
    }

    function checkLoginPassword(loginPassword) {
        if (loginPassword !== "")
            setIsLoginPasswordValid(true)
        setIsLoginPasswordValid(false)
    }

    function checkEmail(email) {
        const emailPattern = new RegExp('[a-zA-Z][a-zA-Z0-9]{1,}@[a-z]{1,}.[a-z]{1,}')
        setIsEmailValid(emailPattern.test(email))
    }

    function checkPassword(password) {
        const passwordPattern = new RegExp('[a-zA-Z0-9]{4,32}')
        const checkIfCapitalExist = new RegExp('[A-Z]')
        const checkIfNumberExists = new RegExp('[0-9]')
        setIsPasswordValid(passwordPattern.test(password) &&
            checkIfNumberExists.test(password) && checkIfCapitalExist.test(password))
    }


    return [
        isLoginEmailValid,
        checkLoginEmail,
        isLoginPasswordValid,
        checkLoginPassword,
        isEmailValid,
        checkEmail,
        isPasswordValid,
        checkPassword
    ]
}

export default useValidators()