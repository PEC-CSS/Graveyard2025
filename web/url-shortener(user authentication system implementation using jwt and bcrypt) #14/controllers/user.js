const User = require("../models/user");
const { v4: uuidv4 } = require("uuid");
const { setUser } = require("../services/auth");
const bcrypt = require('bcrypt');
const saltRounds = 10;

async function handleUserSignup(req, res) {
  const { name, email, password } = req.body;
  await bcrypt.hash(password, saltRounds, async function(err, hash) {
    console.log(hash);
     
    await User.create({
      name,
      email, 
      password:hash,
    });
});
return res.redirect("/");
}

async function handleUserLogin(req, res) {
  const { email, password } = req.body;
  user = await User.findOne({ email });
  if (!user) {
    return res.render("login", { error: "Invalid  username or password" });
  }
  await bcrypt.compare(password, user.password, async function(err, result) {
    if(!result){
      return res.render("login", { error: "Invalid  username or password" });
    }
});
 
  const token = setUser(user);
  res.cookie("uid", token);
  return res.redirect("/");
}

module.exports = { handleUserSignup, handleUserLogin };
