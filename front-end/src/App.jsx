import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from './Components/Home';

function App() {
  return (
    <Router>
      <div class="flex flex-col h-screen justify-between">
      <Routes>
        <Route exact path = '/' element = {<Home />} />
      </Routes>
      </div>
    </Router>
  );
}

export default App;