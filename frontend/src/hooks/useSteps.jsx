import {useState} from "react";

function useSteps() {
    const [step, setStep] = useState('1')
    const [stepsToDisplay, setStepsToDisplay] = useState({'1': true})

    function increaseStep(isEmployee) {
        switch (step) {
            case '1':
                if (isEmployee) {
                    setStep('2a')
                    setStepsToDisplay({...stepsToDisplay, '2a': true})
                }
                else {
                    setStep('2b')
                    setStepsToDisplay({...stepsToDisplay, '2b': true})
                }
                break
            case '2a':
                setStep('3a')
                setStepsToDisplay({...stepsToDisplay, '3a': true})
                break
            case '2b':
                setStep('3b')
                setStepsToDisplay({...stepsToDisplay, '3b': true})
                break
            case '3a':
                setStep('4a')
                setStepsToDisplay({ ...stepsToDisplay, '4a': true})
                break
            default:
                setStep(step)
        }
    }

    function decreaseStep() {
        switch (step) {
            case '4a':
                setStep('3a')
                setStepsToDisplay({...stepsToDisplay, '4a': false})
                break
            case '3a':
                setStep('2a')
                setStepsToDisplay({...stepsToDisplay, '3a': false})
                break
            case '3b':
                setStep('2b')
                setStepsToDisplay({...stepsToDisplay, '3b': false})
                break
            case '2a':
                setStep('1')
                setStepsToDisplay({...stepsToDisplay, '2a': false})
                break
            case '2b':
                setStep('1')
                setStepsToDisplay({...stepsToDisplay, '2b': false})
                break
            default:
                setStep(step)
        }
    }

    return [
        step,
        stepsToDisplay,
        increaseStep,
        decreaseStep,
    ]
}

export default useSteps