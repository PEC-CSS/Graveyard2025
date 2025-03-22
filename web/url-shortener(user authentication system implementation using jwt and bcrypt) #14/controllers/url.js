const ShortUniqueId = require("short-unique-id");
const URL = require("../models/url");
const uid = new ShortUniqueId({ length: 10 });

async function handleGenerateNewShortURL(req, res) {
  const body = req.body;
  if (!body) return res.status(400).json({ error: "url us required" });

  const shortId = uid.rnd();
  await URL.create({
    shortId: shortId,
    redirectURL: body.url,
    viewHistory: [],
    createdBy:req.user._id
  });

  return res.render("home",{id:shortId});
}

async function handleGetAnalytics(req,res) {
    const shortId = req.params.shortId
    const result = await URL.findOne({shortId})
    return res.json({ totalClicks: result.viewHistory.length, analytics: result.viewHistory})
}

module.exports = { handleGenerateNewShortURL ,handleGetAnalytics };
