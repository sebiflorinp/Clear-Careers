import InputBox from "../components/InputBox.jsx";
import {useState} from "react";

function LoginPage() {
    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    return (
        <div className="flex flex-col justify-center items-center bg-neutral-300 h-screen">
            <div className="flex flex-col justify-center items-center bg-neutral-100 border-2 border-solid border-black rounded-lg min-h-96 pl-24 pr-24">
                <h1 className="text-7xl font-montserrat">Login</h1>
                <p>{email}</p>
                <div className="pb-6">
                    <InputBox name="Email" placeHolder="ionescu@yahoo.com" setValue={setEmail}/>
                    <InputBox name="Password" placeHolder="QDvgh12" setValue={setPassword} type="password"/>
                </div>
                <button className="bg-neutral-300 border-2 border-solid border-black rounded-lg text-xl min-w-52 hover:scale-110 duration-150 ease-in-out active:bg-zinc-400">Login</button>
            </div>
        </div>
    )
}

export default LoginPage