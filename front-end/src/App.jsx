import logo from './logo.svg';
import './App.css';
import Data from "./MOCK_DATA.json";
import React, { useState } from "react";
import { Platform, StyleSheet, View, Text } from "react-native";
import Axios from 'axios';


function App() {
  const [ChannelName, setChannelName] = useState('');
  const [StartDate, setStartDate] = useState('');
  const [EndDate, setEndDate] = useState('');

  const sendInfo = () => {
    console.log(ChannelName);
    console.log(StartDate);
    console.log(EndDate);
    Axios.post('http://localhost:3001/getQuery', {ChannelName: ChannelName, StartDate: StartDate, EndDate: EndDate}).then((response) => {
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

  return (
    // <div className="App">
    //   <input placeholder="Enter text"/>
    //   {Data.filter(
    //     post => {
    //       if (query == '') {
    //         return post;
    //       } else if (post.title.toLowerCase().includes(query.toLowerCase())) {
    //         return post
    //       }
    //     }
    //   ).map((post) => (
    //     <div className="box" key={post.id}>
    //       <p>{post.title}</p>
    //       <p>{post.author}</p>
    //     </div>
    //   ))}
    // </div>

    <form>   
    <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300">Search</label>
    <View syle={styles.container}><Text style={styles.setFontSize}>YouTube Transcript Search</Text></View>
    <View syle={styles.container}><Text style={styles1.setFontSize}>Adnan Noorullah - Vrush Patel - Heet Parikh - Matt Straczek - Anshul Goswami</Text></View>
    <div class="relative">
        <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
            <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>
        <input value = {ChannelName} onChange={(event) => {setChannelName(event.target.value);}} type="search" id="default-search" class="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Channel Name" required />

        <input value = {StartDate} onChange={(event) => {setStartDate(event.target.value);}} type="search" id="default-search" class="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Start Date (ENTER YEAR)" required />

        <input value = {EndDate} onChange={(event) => {setEndDate(event.target.value);}} type="search" id="default-search" class="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="End Date (ENTER YEAR)" required />

        <input value = {EndDate} onChange={(event) => {setEndDate(event.target.value);}} type="search" id="default-search" class="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search Query (ENTER PHRASE)" required />

        <button onClick={sendInfo} class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
    </div>
</form>

  );

} export default App;