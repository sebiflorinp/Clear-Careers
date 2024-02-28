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
        <div className="bg-neutral-300 h-screen flex justify-center items-center">
            <div className="flex min-h-[33rem]">
                <div className="flex flex-col justify-start items-center gap-14 bg-neutral-200 border-solid border-black border-2 p-9 rounded-l-lg">
                    <h1 className="text-5xl">Sign up</h1>
                    <div className="flex flex-col gap-4 justify-center items-center min-h-72 min-w-96">
                        {Object.entries(stepsToDisplay).map(([key, value]) => {
                            if (value) {
                                return steps[key]
                            }
                        })}
                    </div>
                </div>
                <div className="bg-neutral-100">
                    <div>
                        
                    </div>
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