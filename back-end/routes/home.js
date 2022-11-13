// const {spawn} = require('child_process')

// module.exports = function (router) {

//     var homeRoute = router.route('/');

//     homeRoute.get(function (req, res) {
//         // res.json({ message: 'Hello' });

//         var dataToSend
//         // spawn new child process to call the python script
//         const python_ = spawn('python', ['back-end/routes/script1.py']);
//         // collect data from script
//         // console.log('Before')
//         python_.stdout.on('data', function (data) {
//             console.log('Pipe data from python script ...');
//             dataToSend = data.toString();
//             // res.send(data);
//         });
//         // console.log('After')
//         // in close event we are sure that stream from child process is closed
//         python_.on('close', (code) => {
//             console.log(`child process close all stdio with code ${code}`);
//             // send data to browser
//             console.log(dataToSend)
//             // res.send(dataToSend)
//             res.send({ message: dataToSend} )
//         });
//         // const PythonShell = require('python-shell').PythonShell;

//         // PythonShell.run('script1.py', null, function (err) {
//         //     if (err) throw err;
//         //     console.log('finished');
//         // });
//     }); 

//     return router;
// }