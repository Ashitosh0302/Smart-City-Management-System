const bcrypt = require("bcryptjs");
const Citizen = require("../models/citizen");

async function login_user(req, res)
{
    const { role, email, password } = req.body;

    if (role === "citizen")
    {
        Citizen.findByEmailOrUsername(email, (error, user) =>
        {
            if (error || !user)
            {
                return res.render("login_page", {
                    error: "Invalid Email or Password"
                });
            }

            // 🔐 compare plain password with HASHED password
            const is_match = bcrypt.compareSync(
                password,
                user.password
            );

            if (!is_match)
            {
                return res.render("login_page", {
                    error: "Invalid Email or Password"
                });
            }

            req.session.citizen = {
                id: user.id,
                full_name: user.full_name,
                username: user.username,
                email: user.email
            };

            // ✅ SUCCESS → SHOW CITIZEN PAGE
            return res.redirect("/citizen")
        });
    }
    else
    {
        return res.render("login_page", {
            error: "Only citizen login supported"
        });
    }
}

module.exports = {
    login_user
};
