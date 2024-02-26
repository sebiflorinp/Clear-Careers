import {useState} from "react";
function useValidators() {
    const [isLoginEmailValid, setIsLoginEmailValid] = useState(false)
    const [isLoginPasswordValid, setIsLoginPasswordValid] = useState(false)

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


    return [
        isLoginEmailValid,
        checkLoginEmail,
        isLoginPasswordValid,
        checkLoginPassword
    ]
}

export default useValidators()