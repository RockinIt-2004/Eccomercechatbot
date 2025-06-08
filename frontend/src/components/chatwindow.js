import { useEffect, useState } from 'react';
import api from '../utils/api'; // Axios instance with JWT

function ChatWindow({ token, setToken }) {
  const [message, setMessage] = useState('');
  const [chatLog, setChatLog] = useState([]);

  // Format timestamp
  const formatTimestamp = (date) => {
    return new Date(date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const sendMessage = async () => {
    if (!message.trim()) return;

    const userMessage = { sender: 'user', text: message, timestamp: new Date() };
    setChatLog(prev => [...prev, userMessage]);

    try {
      const res = await api.post(
        '/chat/message',
        { message },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      const botResponse = {
        sender: 'bot',
        text: res.data.response,
        timestamp: new Date()
      };
      setChatLog(prev => [...prev, botResponse]);
      setMessage('');
    } catch (err) {
      console.error(err);
      if (err.response?.status === 401) {
        alert('Session expired. Please log in again.');
        setToken('');
      } else {
        alert('Error communicating with chatbot.');
      }
    }
  };

  const resetConversation = () => {
    setChatLog([]);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>E-commerce Chatbot</h2>
      
      <div style={{ minHeight: 300, maxHeight: 400, overflowY: 'auto', border: '1px solid #ccc', padding: 10, marginBottom: 10 }}>
        {chatLog.map((chat, idx) => (
          <div key={idx} style={{ textAlign: chat.sender === 'user' ? 'right' : 'left' }}>
            <p style={{ margin: '5px 0' }}>
              <b>{chat.sender === 'user' ? 'You' : 'Bot'}:</b> {chat.text}
              <br />
              <small style={{ color: '#888' }}>{formatTimestamp(chat.timestamp)}</small>
            </p>
          </div>
        ))}
      </div>

      <input
        type="text"
        placeholder="Type your message"
        value={message}
        onChange={e => setMessage(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && sendMessage()}
        style={{ width: '70%', marginRight: 10 }}
      />
      <button onClick={sendMessage}>Send</button>
      <button onClick={resetConversation} style={{ marginLeft: 10, backgroundColor: '#f0f0f0' }}>
        Reset Conversation
      </button>
    </div>
  );
}

export default ChatWindow;
