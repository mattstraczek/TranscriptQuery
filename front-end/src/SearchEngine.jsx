// import React, { useState } from "react";
// import axios from 'axios';

// function SearchEngine() {
//     // const printData = () => {
//     //     Axios.post('http://localhost:3002/query').then((response) => {
//     //     console.log(response).catch(err => console.log(err));
//     //   });
//     //   }

//       return (
//         <div>
//             Will Display Search Engine!
//         </div>
//     )
// } export default SearchEngine;


import React, { useState } from "react";
import Axios from 'axios'




const SearchEngine = () => {
    const [triggerList, setTriggerList] = useState([]);

    const displayTriggers = () => {
        Axios.post('http://localhost:3002/results/display',).then((response) => {
          setTriggerList(response.data)
          console.log(response);
        });
      };



    window.onload = function() {
      displayTriggers()
    };

    const data = triggerList
    
    return (

        <div class="overflow-x-auto">
        <progress className="progress w-100 bg-red-400"></progress>

            
        <table class="table w-full table-zebra">
            <thead>
            <tr>
                <th>ChannelName</th>
                <th class="text-center">DateRange</th>
                <th>Query</th>
                <th>Results</th>

            </tr>
            </thead>
            <tbody>

      <button onClick={displayTriggers}>
        Show results
      </button>

             {data.map((val,key) => {
                  return (
                    <tr key = {key}>
                    <td>{val.ChannelName}</td>
                    <td>{val.DateRange}</td>
                    <td>{val.Query} </td>
                    <td>{val.Results} </td>
                    </tr> 
                  ) 
             })}
            </tbody>
        </table>

        </div>
        

 
        
 
    )
}

export default SearchEngine