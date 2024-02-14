import { Link } from "react-router-dom";

function LandingPage() {

    return (
        <div className="flex flex-col gap-7 justify-center align-middle font-tinos h-screen">
            <h1 className="text-6xl font-bold max-w-2xl self-center text-center">The place where talent meets opportunity</h1>
            <h2 className="text-4xl self-center text-center max-w-3xl">
                Whether you're looking to kickstart your career or are in search of skilled professionals you are in good hands
            </h2>
            <Link to="/sign-up" className="self-center">
                <button className="text-4xl border-black border-solid border-2 p-1 hover:scale-125 transition ease-in-out duration-300">Sign up</button>
            </Link>

        </div>
    )
}

export default LandingPage