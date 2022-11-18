var express = require('express'),
bodyParser = require('body-parser');
const {spawn} = require('child_process')
var router = express.Router();
const axios = require('axios')
// const { Builder, By } = require('selenium-webdriver');
// let axios = require('axios');
let cheerio = require('cheerio');
let fs = require('fs');

var app = express();

var port = process.env.PORT || 3002

// Allow CORS so that backend and frontend could be put on different servers
var allowCrossDomain = function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept");
    res.header("Access-Control-Allow-Methods", "POST, GET, PUT, DELETE, OPTIONS");
    next();
};
app.use(allowCrossDomain);

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

// Use routes as a module (see index.js)
// require('./routes')(app, router);

app.get('/', (req, res) => {
    var dataToSend
    // spawn new child process to call the python script
    const python_ = spawn('python', ['back-end/web_scraper.py']);
    // collect data from script
    // console.log('Before')
    python_.stdout.on('data', (data) => {
        console.log('Pipe data from python script ...' + data);
        dataToSend = data.toString();
        // dataToSend = data
        console.log(dataToSend)
        // res.send(data);
    });
    // console.log('After')
    // in close event we are sure that stream from child process is closed
    python_.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        // // send data to browser
        // console.log(dataToSend)
        // res.send(dataToSend)
        res.send({ message: dataToSend} )
    });
    // const py_child = spawn('python', ['--version'])
    // const py_child = spawn('python3', ['web_scraper.py'])
    // py_child.stdout.on('data', (data) => {
    //     console.log('stdout: ' + data)
    // })
    // py_child.on('close', (code) => {
    //     console.log('child process exited with code ${code}')
    // })
    // res.send("Hi")

})

// axios.get('https://dev.to/aurelkurtula')
//     .then((response) => {
//         if(response.status === 200) {
//         const html = response.data;
//             const $ = cheerio.load(html); 
//     }
//     }, (error) => console.log(err) );




// app.get('/', async (request, response) => {
//         // Web Scraping Code here
//         try {
//           const data = await WebScrapingLocalTest();
//           response.status(200).json(data);
//         } catch (error) {
//           response.status(500).json({
//             message: 'Server error occurred',
//           });
//         }
// });

app.get('/', async (request, res) => {
    // console.log(res)

    // axios.get('https://dev.to/aurelkurtula').then((response) => {
    //     if(response.status === 200) {
    //         const html = response.data;
    //         const $ = cheerio.load(html); 
    //         let devtoList = [];
    //         console.log($.text())
    //         $('.single-article').each(function(i, elem) {
    //             devtoList[i] = {
    //                 title: $(this).find('h3').text().trim(),
    //                 url: $(this).children('.index-article-link').attr('href'),
    //                 tags: $(this).find('.tags').text().split('#')
    //                       .map(tag =>tag.trim())
    //                       .filter(function(n){ return n != "" })
    //             }    
    //         });
    //     }   
    // }, (error) => console.log(err) );
    // res.send('Hello');
})

// Start the server
app.listen(port);
console.log('Server running on port ' + port);




// async function WebScrapingLocalTest() {
//     try {
//       driver = await new Builder().forBrowser('chrome').build();
//       await driver.get('https://www.youtube.com/c/LambdaTest/videos');
//       const allVideos = await driver.findElements(
//         By.css('ytd-grid-video-renderer.style-scope.ytd-grid-renderer')
//       );
//       return await getVideos(allVideos);
//     } catch (error) {
//       throw new Error(error);
//     } finally {
//       await driver.quit();
//     }
// }