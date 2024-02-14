import {Link} from "react-router-dom";
import logo from '../assets/logo.webp'

function NavBar() {
    return (
        <div className="flex flex-row justify-between align-middle p-2.5 pr-4 pl-2 border-solid border-black border-b-2">
            <Link to="/">
                <img src={logo} alt="clearCareersLogo" className="max-h-14"/>
            </Link>
            <div className="flex flex-row gap-7 text-3xl font-montserrat">
                <Link to="/sign-up" className="self-center p-1 transition hover:scale-125 duration-300 ease-in-out">Sign up</Link>
                <Link to="/log-in" className="self-center p-1 transition hover:scale-125 duration-300 ease-in-out">Log in</Link>
            </div>
        </div>
    )
}

export default NavBar