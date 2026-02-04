const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const Citizen = require("../models/citizen");

function login_user(req, res)
{
    const { role, email, password } = req.body;

    if(role !== "citizen")
    {
        return res.render("login", {
            error: "Invalid role"
        });
    }

    Citizen.findByEmailOrUsername(email, (err, citizen) =>
    {
        if(err || !citizen)
        {
            return res.render("login", {
                error: "Invalid email or password"
            });
        }

        const match = bcrypt.compareSync(password, citizen.password);
        if(!match)
        {
            return res.render("login", {
                error: "Invalid email or password"
            });
        }

        const token = jwt.sign(
            {
                id: citizen.id,
                role: "citizen"
            },
            process.env.JWT_SECRET,
            { expiresIn: "2h" }
        );

        res.cookie("token", token, {
            httpOnly: true,
            sameSite: "lax",
            secure: false, // true in production
            maxAge: 2 * 60 * 60 * 1000
        });

        return res.redirect("/citizen");
    });
}

module.exports = { login_user };
