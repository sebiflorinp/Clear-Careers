import {useState} from "react";

function useSteps() {
    const [step, setStep] = useState('1')

    function increaseStep(isEmployee) {
        switch (step) {
            case '1':
                if (isEmployee)
                    setStep('2a')
                else
                    setStep('2b')
                break
            case '2a':
                setStep('3a')
                break
            case '2b':
                setStep('3b')
                break
            default:
                setStep(step)
        }
    }

    function decreaseStep() {
        switch (step) {
            case '3a':
                setStep('2a')
                break
            case '3b':
                setStep('2b')
                break
            case '2a':
            case '2b':
                setStep('1')
                break
            default:
                setStep(step)
        }
    }

    return {
        step,
        increaseStep,
        decreaseStep
    }
}

export default useSteps