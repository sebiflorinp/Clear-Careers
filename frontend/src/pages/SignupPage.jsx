<<<<<<< Updated upstream
function SignupPage() {
    return (
        <div className="h-screen bg-neutral-300">
            <div>
                <div>
                    <h1>Sign up</h1>
                </div>
                <div>
=======
import Step from "../components/Step.jsx";

function SignupPage() {
    return (
        <div className="bg-neutral-300 h-screen">
            <div>
                <div className="bg-neutral-200">
                    <h1 className="text-5xl">Sign up</h1>
                    <Step title="credentiale" active={true} description="descriere" number={1}/>
                </div>
                <div className="bg-neutral-100">
                    <h1></h1>
>>>>>>> Stashed changes

                </div>
            </div>
        </div>
    )
}

export default SignupPage