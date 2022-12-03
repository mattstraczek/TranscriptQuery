import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import App from './App';
import SearchEngine from './SearchEngine';
import Header from './shared/Header'

function Establish() {
    return (
        <Router>
            <div class="flex flex-col h-screen justify-between">
            <Header />
            <Routes>
                <Route exact path = '/' element = {<App />} />
                <Route exact path = '/SearchEngine' element = {<SearchEngine />} />
            </Routes>
            </div>
        </Router>
    )
} export default Establish;