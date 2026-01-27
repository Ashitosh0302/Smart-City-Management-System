const mongoose = require("mongoose");

function CONNECT_MONGO()
{
    mongoose.connect(
        "mongodb://localhost:27017/CityZen",
        {
            useNewUrlParser: true,
            useUnifiedTopology: true
        }
    )
    .then(() =>
    {
        console.log("MongoDB connected successfully");
    })
    .catch((error) =>
    {
        console.error("MongoDB connection error:", error);
    });
}

module.exports = CONNECT_MONGO;
