import React, { useState, useEffect } from 'react';
import Login from './components/login';
import ChatWindow from './components/chatwindow';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
    } else {
      localStorage.removeItem('token');
    }
  }, [token]);

  if (!token) {
    return <Login setToken={setToken} />;
  }

  return <ChatWindow token={token} setToken={setToken} />;
}

export default App;
