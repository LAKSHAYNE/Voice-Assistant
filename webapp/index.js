require("dotenv").config();
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({ extended: true }));
const mongoose = require("mongoose");
const crypto = require("crypto");
app.use(express.static("public"));
mongoose.connect(
  "mongodb+srv://" +
    process.env.DBUSERNAME +
    ":" +
    process.env.DBPASSWORD +
    "@cluster0.siopf.mongodb.net/" +
    process.env.DBNAME +
    "?retryWrites=true&w=majority",
  { useNewUrlParser: true, useUnifiedTopology: true }
);
const userSchema = mongoose.Schema({
  email: String,
  password: String,
});
const userS = mongoose.model("users", userSchema);
app.get("/register", (req, res) => {
  res.sendFile(__dirname + "/register.html");
});
app.post("/register", (req, res) => {
  console.log(req.body.email);
  if (req.body.cpass != req.body.pass) {
    res.send("Password didn't match please retry");
  }
  const pass = crypto
    .createHash("sha256")
    .update(process.env.SECRET)
    .digest("hex");
  const newdata = new userS({
    email: req.body.email,
    password: pass,
  });
  newdata.save();
  res.send("Thank you");
});
app.listen("3000", () => console.log("Server is running"));
