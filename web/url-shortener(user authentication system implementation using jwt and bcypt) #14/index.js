const express = require("express");
const app = express();
const PORT = 8001;
const { connectToMongoDB } = require("./connectDB.js");
const cookieParser = require('cookie-parser');
const URL = require("./models/url.js");
const path = require("path");

const urlRoute = require("./routes/url.js");
const staticRoute = require("./routes/staticRoute.js");
const userRoute = require("./routes/user.js");
const { restrictToLoggedInUserOnly, checkAuth } = require("./middlewares/auth.js");

app.set("view engine", "ejs"); 
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser())    
app.set("views", path.resolve("./views"));  

MONGO_URL = "mongodb://localhost:27017/short-url";
connectToMongoDB(MONGO_URL)
  .then(() => {
    console.log("MongoDB connected");
  })
  .catch((err) => {
    console.log("MongoDB error:", err);
  });

app.use("/", checkAuth,staticRoute);
app.use("/url",restrictToLoggedInUserOnly, urlRoute);
app.use("/user", userRoute)   

app.get("/:shortId", async (req, res) => {
  shortId = req.params.shortId;
  const entry = await URL.findOneAndUpdate(
    { shortId },
    {
      $push: {
        viewHistory: { timestamp: Date.now() },
      },
    }
  );
  if(entry) res.redirect(entry.redirectURL);
});

app.listen(PORT, () => console.log(`Server started at port: ${PORT}`));
