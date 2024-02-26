import Step from "../components/Step.jsx";
import useSteps from "../hooks/useSteps.jsx";

function SignupPage() {
    const [currentStep, nextStep, previousStep] = useSteps()
    return (
        <div className="bg-neutral-300 h-screen">
            <div>
                <div className="bg-neutral-200">
                    <h1 className="text-5xl">Sign up</h1>
                    <Step title="credentiale" active={true} description="descriere" number={1}/>
                </div>
                <div className="bg-neutral-100">
                    <h1></h1>
                </div>
            </div>
        </div>
    )
}

export default SignupPage