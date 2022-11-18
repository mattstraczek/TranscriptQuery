var express = require('express'),
bodyParser = require('body-parser');
const {spawn} = require('child_process')
var router = express.Router();
const axios = require('axios')
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
    
    const python_ = spawn('python', ['back-end/web_scraper.py']);

    python_.stdout.on('data', (data) => {
        console.log('Pipe data from python script ...' + data);
        dataToSend = data.toString();
        // console.log(dataToSend)
    });

    python_.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        res.send({ message: dataToSend} )
    });
})

// Start the server
app.listen(port);
console.log('Server running on port ' + port);

