import { ChangeEventHandler, useState } from 'react';
import './App.css'


function App() {

    const [input,setInput] = useState("");

    const handleInputChange = (e: React.FormEvent<HTMLInputElement>)=> {
        setInput(e.currentTarget.value);
      };

    return (
        <div>
        <input id ="input" onChange={handleInputChange} className="form-label" placeholder='Enter Url to Shorten' value={input} />
        <button id="submitButton">Create Short URL</button>
        </div>
    )
}

export default App;