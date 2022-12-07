import './App.css';
import Data from "./MOCK_DATA.json";
import React, { useState } from "react";
import { Platform, StyleSheet, View, Text } from "react-native";
import Axios from 'axios';
import { Link } from 'react-router-dom';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Header from './shared/Header';
import SearchEngine from './SearchEngine';
import Main_Page from './main_page';

function App() {
  const [ChannelName, setChannelName] = useState('');
  const [StartDate, setStartDate] = useState('');
  const [EndDate, setEndDate] = useState('');
  const [SearchQuery, setSearchQuery] = useState('');

  const sendInfo = () => {
    console.log(ChannelName);
    console.log(StartDate);
    console.log(EndDate);
    console.log(SearchQuery);
    <Link to='./SearchEngine'></Link>
    Axios.post('http://localhost:3002/query', {ChannelName: ChannelName, StartDate: StartDate, EndDate: EndDate, SearchQuery: SearchQuery}).then((response) => {
    console.log(response).catch(err => console.log(err));
  });
  }

  const styles = StyleSheet.create(
    {
      container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      },
      setFontSize: {
        fontWeight: 'bold',
        fontSize: 60,
        color: 'white',
        textAlign: 'center',
      },
    }
  );

  const styles1 = StyleSheet.create(
    {
      container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
      },
      setFontSize: {
        fontSize: 15,
        color: 'white',
        textAlign: 'center',
      },
    }
  );
  
  // const handleClick = () => {
  //   <Link to='/SearchEngine'> </Link>
  // }

  return (
    <div>
        <Router>
          <div class="flex flex-col h-screen ">
            <Header />
            <Routes>
                {/* <Route exact path = '/' element = {<App />} />  */}
                <Route exact path = '/' element = {<Main_Page />} />
                <Route exact path = '/SearchEngine' element = {<SearchEngine />} />
            </Routes>
          </div>
        </Router>
    </div> 

  );

} export default App;