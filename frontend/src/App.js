import React, { useState } from "react";
import axios from "axios";
import "./App.css";


// const apiUrl = process.env.REACT_APP_API_URL;

// if(apiUrl){
//     console.log(REACT_APP_API_URL)
// }


function App() {
    const [userInput, setUserInput] = useState("");
    const [messages, setMessages] = useState([]);

    const handleSend = async () => {
        if (userInput.trim()) {
            const newMessages = [...messages, { sender: "user", text: userInput }];
            setMessages(newMessages);
            setUserInput("");

            try {
                const response = await axios.post(`${process.env.REACT_APP_API_URL}/chat/`, {
                    text: userInput,
                });
                setMessages([...newMessages, { sender: "bot", text: response.data.response }]);
            } catch (error) {
                console.error("Error fetching response:", error);
            }
        }
    };

    return (
        <div className="App">
            <h1>Chatbot</h1>
            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <strong>{msg.sender === "user" ? "You" : "HR_Bot "}:{" "}</strong>
                        <span>{msg.text}</span>
                    </div>
                ))}
            </div>
            <div className="input-area">
                <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    onKeyPress={(e) => e.key === "Enter" && handleSend()}
                    placeholder="Type your message..."
                />
                <button onClick={handleSend}>Send</button>
            </div>
        </div>
    );
}

export default App;
