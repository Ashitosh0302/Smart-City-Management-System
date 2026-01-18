const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config();

const app = express();
const PORT= process.env.PORT || 3070

//routes import
const home_route=require("./routes/home")
const citizen_route=require("./routes/citizen")
const government_route=require("./routes/government")
const hospital_route=require("./routes/hospital")
const court_route=require("./routes/court")
const transport_route=require("./routes/transpose")

//error handling middlwares
const { ERROR_HANDLER } = require("./middlewares/error_middlewares");

//middlewares
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

//uploads
app.use("/uploads", express.static(path.join(__dirname, "uploads")));
app.use("/public", express.static(path.join(__dirname, "public")));

//view engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

//eror handling
app.use((err, req, res, next) =>
{
    res.status(err.status || 500).json({
        success: false,
        message: err.message || "Internal Server Error"
    });
});

//app error hadnling
app.use(ERROR_HANDLER)

//routes
app.use("/",home_route)
app.use("/citizen",citizen_route)
app.use("/government",government_route)
app.use("/hospital",hospital_route)
app.use("/court",court_route)
app.use("/transport",transport_route)

//server running
app.listen(PORT,()=>{console.log("SERVER RUNNING")})