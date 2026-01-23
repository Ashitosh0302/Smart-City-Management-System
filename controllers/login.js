const bcrypt = require("bcryptjs");
const Citizen = require("../models/citizen");
const Government = require("../models/government");

async function login_user(req, res)
{
    const { role, department, email, password } = req.body;

    // ===== CITIZEN LOGIN =====
    if(role === "citizen")
    {
        // use existing function
        Citizen.findByEmailOrUsername(email, (err, citizen) =>
        {
            if(err || !citizen)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            const match = bcrypt.compareSync(password, citizen.password);
            if(!match)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            req.session.citizen = citizen;
            return res.redirect("/citizen"); // successful login
        });

        return; // exit function to prevent further execution
    }

    // ===== ADMIN LOGIN =====
    if(role === "admin" && department === "government")
    {
        Government.findByEmail(email, (err, gov) =>
        {
            if(err || !gov)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            const match = bcrypt.compareSync(password, gov.password);
            if(!match)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            req.session.government = gov;
            return res.redirect("/government"); // successful login
        });

        return;
    }

    // fallback for wrong role/department
    return res.render("login_page", { error: "Invalid login" });
}

module.exports = {
    login_user
};
