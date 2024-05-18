const express = require('express');

// initialize express

const app = express();

//configure body-parser to handle post requests

app.use(express.json());


app.get('/', (req, res) => {
    res.send('REST API Authorization and Authentication');
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
