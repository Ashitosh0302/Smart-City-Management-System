const jwt = require("jsonwebtoken");

exports.AUTH_MIDDLEWARE = (req, res, next) =>
{
    try
    {
        const token = req.cookies.token;

        if(!token)
        {
            return res.redirect("/login");
        }

        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded;

        next();
    }
    catch(error)
    {
        res.clearCookie("token");
        return res.redirect("/login");
    }
};

exports.CITIZEN_ONLY = (req, res, next) =>
{
    if(req.user.role !== "citizen")
    {
        return res.status(403).send("Access denied");
    }
    next();
};
