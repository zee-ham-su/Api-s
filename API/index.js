import  express  from "express";
import crypto from "crypto";

const app = express();

app.use(express.json());

const products = [
    {
        "id": "1b99b728-7c2c-462c-b23b-fd5a21199983",
        "name": "Laptop",
        "price": 488.96,
        "quantity": 10,
        "active": true
    },
    {
        "id": "1b99b728-7c2c-462c-b23b-fd5a21199982",
        "name": "Mouse",
        "price": 9.99,
        "quantity": 50,
        "active": true
    },
    {
        "id": "1b99b728-7c2c-462c-b23b-fd5a21199981",
        "name": "Keyboard",
        "price": 19.99,
        "quantity": 30,
        "active": false
    },
    {
        "id": "1b99b728-7c2c-462c-b23b-fd5a21199980",
        "name": "Power bank",
        "price": 4500.99,
        "quantity": 15,
        "active": true
    }
]
app.get('/products', (req, res) => {
    res.status(200).json(products);
});

app.post('/products', (req, res) => {
    const { name, price, quantity, active } = req.body;
    if (!name || !price || !quantity || !active) {
        return res.status(400).json({ message: 'All fields are required' });
     }
    const id = crypto.randomUUID()
    products.push({ id, name, price, quantity, active }); 
    res.status(201).json({ message: 'product successfully added', id: id });
});

app.get('/', (req, res) => {
    res.status(200).send("Hello World");
});


app.listen(3000, () => {
    console.log("Server is running on port 3000");
});