const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const path = require("path");
const session = require("express-session");

const CONNECT_MONGO = require("./config/mongo");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3070;

(async () =>
{
    try
    {
        // ✅ WAIT for MongoDB
        await CONNECT_MONGO();

        // middlewares
        app.use(cors());
        app.use(express.json());
        app.use(express.urlencoded({ extended: true }));

        app.use(session({
            secret: "your-secret-key",
            resave: false,
            saveUninitialized: false,
            cookie: { maxAge: 1000 * 60 * 60 }
        }));

        // static
        app.use("/uploads", express.static(path.join(__dirname, "uploads")));
        app.use("/public", express.static(path.join(__dirname, "public")));

        // view engine
        app.set("view engine", "ejs");
        app.set("views", path.join(__dirname, "views"));

        // routes
        app.use("/", require("./routes/home"));
        app.use("/login", require("./routes/login"));
        app.use("/citizen", require("./routes/citizen"));
        app.use("/government", require("./routes/government"));
        app.use("/hospital", require("./routes/hospital"));
        app.use("/court", require("./routes/court"));
        app.use("/transport", require("./routes/transpose"));

        // error handler (LAST)
        const { ERROR_HANDLER } = require("./middlewares/error_middlewares");
        app.use(ERROR_HANDLER);

        // start server ONLY after DB ready
        app.listen(PORT, () =>
        {
            console.log(`🚀 Server running on port ${PORT}`);
        });
    }
    catch(error)
    {
        console.error("❌ Server startup failed:", error.message);
        process.exit(1);
    }
})();
