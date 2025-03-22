  const { getUser } = require("../services/auth");

async function restrictToLoggedInUserOnly(req, res, next) {
  const userUid = req.cookies?.uid;
  if (!userUid) {
    res.redirect("/login");
  }

  const user = getUser(userUid);
 console.log(user);
 
  if (!user) {
    res.redirect("/login");
  }
 
  req.user = user;
  next();
}

async function checkAuth(req, res, next) {

  const userUid = req.cookies?.uid;
  const user = getUser(userUid);
 
  req.user = user;
  next();
}

module.exports = { restrictToLoggedInUserOnly , checkAuth}
