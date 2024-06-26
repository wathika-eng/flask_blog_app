import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Account() {
  const [username, setUsername] = useState('');

  useEffect(() => {
    const fetchAccount = async () => {
      try {
        const res = await axios.get('http://localhost:5000/api/account');
        setUsername(res.data.username);
      } catch (error) {
        console.error(error);
      }
    };
    fetchAccount();
  }, []);

  return <h2>Logged in as: {username}</h2>;
}

export default Account;
