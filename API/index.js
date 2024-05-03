import  express  from "express";


const app = express();

const products = [
    {
        name: 'Laptop',
        price: 488.96,
        quantity: 10,
        active: true
    },
    {
        name: 'Mouse',
        price: 9.99,
        quantity: 50,
        active: true
    },
    {
        name: 'Keyboard',
        price: 19.99,
        quantity: 30,
        active: false
    }
];

app.get('/products', (req, res) => {
    res.status(200).json(products);
});

app.post('/products', (req, res) => {
    console.log(req.body);
    res.send('Adding a product');
});

app.get('/', (req, res) => {
    res.status(200).send("Hello World");
});


app.listen(3000, () => {
    console.log("Server is running on port 3000");
});