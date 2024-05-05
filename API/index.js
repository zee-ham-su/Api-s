import  express  from "express";
import crypto from "crypto";

const app = express();

app.use(express.json());


app.get('/', (req, res) => {
    res.status(200).send("Hello World");
});


app.listen(3000, () => {
    console.log("Server is running on port 3000");
});