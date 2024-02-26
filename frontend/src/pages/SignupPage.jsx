import Step from "../components/Step.jsx";
import useSteps from "../hooks/useSteps.jsx";

function SignupPage() {
    const [currentStep, stepsToDisplay, nextStep, previousStep] = useSteps()
    const steps = {
        '1':  <Step title="Credentials" active={currentStep === '1'} description="The information required to login." number={1}/>,
        '2a': <Step title="Personal information" active={currentStep === '2a'} description="Some information about youself?" number={2}/>,
        '2b': <Step title="Company information" active={currentStep === '2b'} description="Some information about your business?" number={2}/>,
        '3a': <Step title="Education" active={currentStep === '3a'} description="Something about your education?" number={3}/>,
        '3b': <Step title="Locations" active={currentStep === '3b'} description="Where is your business located?" number={3}/>,
        '4a': <Step title="Experience" active={currentStep === '4a'} description="Something about your experience?" number={4}/>
    }
    return (
        <div className="bg-neutral-300 h-screen">
            <div>
                <div className="bg-neutral-200">
                    <h1 className="text-5xl">Sign up</h1>
                    {Object.entries(stepsToDisplay).map(([key, value]) => {
                        if (value) {
                            return steps[key]
                        }
                    })}
                </div>
                <div className="bg-neutral-100">
                    <div>
                        <button onClick={() => previousStep()}
                                className="bg-neutral-300 text-2xl min-w-40 border-2 border-black border-solid rounded-lg hover:scale-105 duration-200 ease-in-out active:bg-neutral-400">
                            Previous
                        </button>
                        <button onClick={() => nextStep(true)}
                                className="bg-neutral-300 text-2xl min-w-40 border-2 border-black border-solid rounded-lg hover:scale-105 duration-200 ease-in-out active:bg-neutral-400">
                            Next
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SignupPage