import  express  from "express";


const app = express();

app.use(express.json());

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
    const { name, price, quantity, active } = req.body;
    if (!name || !price || !quantity || !active) {
        return res.status(400).send({ message: 'All fields are required' });
     }
    products.push({ name, price, quantity, active }); 
    res.status(201).send({ message: 'product successfully added' });
});

app.get('/', (req, res) => {
    res.status(200).send("Hello World");
});


app.listen(3000, () => {
    console.log("Server is running on port 3000");
});