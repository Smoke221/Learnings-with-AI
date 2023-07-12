const express = require("express");
const { router } = require("./routes/openai");
const cors = require("cors");

require("dotenv").config();
const app = express();
app.use(express.json());
app.use(cors());
app.get("/", (req, res) => {
  res.status(200);
  res.send("App is running successfully");
});
app.use("/identify", router);

port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`App is running on port ${port}`);
});
