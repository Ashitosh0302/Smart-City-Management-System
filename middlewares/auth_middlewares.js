const jwt = require("jsonwebtoken");

function AUTH_MIDDLEWARE(req, res, next)
{
    const token = req.cookies.token;

    if(!token)
    {
        return res.redirect("/login");
    }

    try
    {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded;
        next();
    }
    catch(error)
    {
        res.clearCookie("token");
        return res.redirect("/login");
    }
}

function CITIZEN_ONLY(req, res, next)
{
    if(req.user.role !== "citizen")
    {
        return res.status(403).send("Access denied");
    }
    next();
}

function GOVERNMENT_ONLY(req, res, next)
{
    if(req.user.role !== "admin" || req.user.department !== "government")
    {
        return res.redirect("/login");
    }
    next();
}

module.exports =
{
    AUTH_MIDDLEWARE,
    CITIZEN_ONLY,
    GOVERNMENT_ONLY
};
