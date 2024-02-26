import {Routes, Route, useLocation} from "react-router-dom";
import LandingPage from "./pages/LandingPage.jsx";
import SignupPage from "./pages/SignupPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import NavBar from "./components/NavBar.jsx";

function App() {
    const location = useLocation()
    const {hash, pathname, search} = location
    return (
        <div className={"flex flex-col h-screen bg-center bg-no-repeat bg-cover bg-opacity-5"
            + (pathname === "/" ?  " bg-main-page" : " ")}>
            <NavBar/>
            <Routes>
                <Route path="/" element={<LandingPage/>}/>
                <Route path="/sign-up" element={<SignupPage/>}/>
                <Route path="/log-in" element={<LoginPage/>}/>
            </Routes>
        </div>
    )
}

export default App
