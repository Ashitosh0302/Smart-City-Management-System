const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");
const path = require("path");
const cookieParser = require("cookie-parser");

const CONNECT_MONGO = require("./config/mongo");
const { ERROR_HANDLER } = require("./middlewares/error_middlewares");
const { AUTH_MIDDLEWARE } = require("./middlewares/auth_middlewares");

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3070;

(async () => {
    try {
        // Connect to MongoDB
        await CONNECT_MONGO();

        // Global middleware
        app.use(cors());
        app.use(cookieParser());
        app.use(express.json());
        app.use(express.urlencoded({ extended: true }));

        // Static folders
        app.use("/uploads", express.static(path.join(__dirname, "uploads")));
        app.use("/public", express.static(path.join(__dirname, "public")));

        // View engine
        app.set("view engine", "ejs");
        app.set("views", path.join(__dirname, "views"));

        // Routes (JWT auth applied inside route files where needed)
        app.use("/", require("./routes/home"));
        app.use("/login", require("./routes/login"));
        app.use("/citizen", require("./routes/citizen"));
        app.use("/government", require("./routes/government"));
        app.use("/hospital", require("./routes/hospital"));
        app.use("/court", require("./routes/court"));
        app.use("/transport", require("./routes/transpose"));

        // Error handler
        app.use(ERROR_HANDLER);

        // Start server
        app.listen(PORT, () => {
            console.log(`🚀 Server running on port ${PORT}`);
        });
    } catch (error) {
        console.error("❌ Server startup failed:", error.message);
        process.exit(1);
    }
})();
