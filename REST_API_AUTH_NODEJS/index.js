const express = require('express');
const Datastore = require('nedb-promises');
const bcrypt = require('bcryptjs');

// initialize express
const app = express();

//configure body-parser to handle post requests
app.use(express.json());

const users = Datastore.create('Users.json');

app.get('/', (req, res) => {
    res.send('REST API Authorization and Authentication');
});

app.post('/api/auth/register', async (req, res) => {
    try {
        const { name, email, password } = req.body;
        if (!name || !email || !password) {
        return res.status(422).json({ error: "Please fill all fields" });
        }
        const hasPassword = await bcrypt.hash(password, 10);
        const newUser = await users.insert({
            name,
            email,
            password: hasPassword });
            return res.status(201).json(newUser);
    }
    catch (error) {
        return res.status(500).json({ error: error.message });
    }

});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
