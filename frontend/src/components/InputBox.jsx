function InputBox({name, placeHolder, setValue, type="text"}) {
    return (
        <div className="p-2">
            <h2 className="text-2xl ml-2">{name}</h2>
            <input placeholder={placeHolder} onChange={(e) => setValue(e.target.value)} type={type}
                 className="border-2 border-solid pl-2 border-black rounded-lg bg-neutral-200 placeholder-neutral-500 placeholder:pl-10 text-xl outline-none"/>
        </div>
    )
}

export default InputBox