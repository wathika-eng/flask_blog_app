import React from 'react';

import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from './Components/Home';
import Register from './Components/Register';
import Login from './Components/Login';
import Account from './Components/Account';


function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" exact element={Home} />
          <Route path="/register" element={Register} />
          <Route path="/login" element={Login} />
          /<Route path="/account" element={Account} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
