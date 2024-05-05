const express = require('express');
const { json } = require('express');

const app = express();

app.use(json());

app.use('/products', require('./routes/productRoutes'));

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
