const mongoose = require("mongoose");

async function CONNECT_MONGO()
{
    if(mongoose.connection.readyState === 1)
    {
        console.log("✅ MongoDB already connected");
        return;
    }

    try
    {
        await mongoose.connect(
            process.env.MONGO_URI || "mongodb://127.0.0.1:27017/CityZen",
            {
                serverSelectionTimeoutMS: 5000,
                socketTimeoutMS: 45000,
                maxPoolSize: 10
            }
        );

        console.log("🚀 MongoDB connected successfully");
        console.log(`   Host     : ${mongoose.connection.host}`);
        console.log(`   Port     : ${mongoose.connection.port}`);
        console.log(`   Database : ${mongoose.connection.name}`);
    }
    catch(error)
    {
        console.error("❌ MongoDB connection failed");
        console.error(error.message);
        process.exit(1);
    }
}

mongoose.connection.on("disconnected", () =>
{
    console.log("⚠️ MongoDB disconnected");
});

module.exports = CONNECT_MONGO;
