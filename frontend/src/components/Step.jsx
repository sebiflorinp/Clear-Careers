function Step({number, title, description, active}) {
    return (
        <div className="flex p-1 gap-3 min-w-10">
            <div className={"flex justify-center items-center bg-zinc-400 rounded-full text-3xl text-white h-12 w-12 "
             + (active === true ? "bg-zinc-600" : "bg-zinc-400")}>
                <p className="p-2 m-2">{number}</p>
            </div>
            <div className="flex flex-col justify-center items-center min-w-40">
                <h2 className="text-xl">{title}</h2>
                <p className="text-sm">{description}</p>
            </div>
        </div>
    )
}

export default Step