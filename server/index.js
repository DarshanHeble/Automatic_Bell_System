const express = require("express");
const port = 4300;

const app = express();

app.get("/test", (req, res) => {
  res.send("<h1>Hello <h1>");
});

app.use(express.static("./app/browser"));

app.listen(port, () => {
  console.log("http://localhost:" + port);
});
