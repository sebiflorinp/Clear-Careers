import InputBox from "../components/InputBox.jsx";
import Cookies from 'js-cookie'
import {useState} from "react";



function LoginPage() {
    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const [errorMessage, setErrorMessage] = useState(null)


    function handleLogin() {
        fetch("https://clear-careers.onrender.com/api/v1/auth/jwt/create/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: email,
                password: password,
            }),
        })
            .then(response => {
                if (!response.ok)
                    throw new Error('The email and password combination is incorrect!')
                return response.json()
            })
            .then(json => {
                const {access, refresh} = json
                Cookies.set("access", access)
                Cookies.set('refresh', refresh)
            })
            .catch(error => {
                setErrorMessage("The email and password combination is incorrect!")
            })
    }

    return (
        <div className="flex flex-col justify-center items-center bg-neutral-300 h-screen">
            <div className="flex flex-col justify-center items-center bg-neutral-100 border-2 border-solid border-black rounded-lg min-h-96 pl-24 pr-24">
                <h1 className="text-7xl font-montserrat">Login</h1>
                <div className="pb-6">
                    <InputBox name="Email" placeHolder="ionescu@yahoo.com" setValue={setEmail}/>
                    <InputBox name="Password" placeHolder="QDvgh12" setValue={setPassword} type="password"/>
                </div>
                {errorMessage && <p className="text-xs text-red-700">{errorMessage}</p>}
                <button onClick={() => handleLogin()} className="bg-neutral-300 border-2 border-solid border-black rounded-lg text-xl min-w-52 hover:scale-110 duration-150 ease-in-out active:bg-zinc-400">Login</button>
            </div>
        </div>
    )
}

export default LoginPage