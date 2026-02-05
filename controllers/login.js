const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const Citizen = require("../models/citizen");
const Government = require("../models/government");
const Court = require("../models/court");
const Hospital = require("../models/hospital");
const Transport = require("../models/transpose");

function login_user(req, res)
{
    let { role, department, email, password } = req.body;

    role = role?.trim().toLowerCase();
    department = department?.trim().toLowerCase();

    // ===== CITIZEN LOGIN =====
    if(role === "citizen")
    {
        Citizen.findByEmailOrUsername(email, (err, citizen) =>
        {
            if(err || !citizen)
                return res.render("login_page", { error: "Invalid email or password" });

            if(!bcrypt.compareSync(password, citizen.password))
                return res.render("login_page", { error: "Invalid email or password" });

            const token = jwt.sign(
                { id: citizen.id, role: "citizen" },
                process.env.JWT_SECRET,
                { expiresIn: "2h" }
            );

            res.cookie("token", token, {
                httpOnly: true,
                sameSite: "lax",
                secure: false,
                maxAge: 2 * 60 * 60 * 1000
            });

            return res.redirect("/citizen");
        });
    }

    // ===== ADMIN LOGIN =====
    else if(role === "admin")
    {
        if(!department)
            return res.render("login_page", { error: "Please select department" });

        let Model, redirectURL;

        switch(department)
        {
            case "government":
                Model = Government;
                redirectURL = "/government";
                break;
            case "court":
                Model = Court;
                redirectURL = "/court";
                break;
            case "hospital":
                Model = Hospital;
                redirectURL = "/hospital";
                break;
            case "transport":
                Model = Transport;
                redirectURL = "/transport";
                break;
            default:
                return res.render("login_page", { error: "Invalid department" });
        }

        Model.findByEmail(email, (err, admin) =>
        {
            if(err || !admin)
                return res.render("login_page", { error: "Invalid email or password" });

            if(!bcrypt.compareSync(password, admin.password))
                return res.render("login_page", { error: "Invalid email or password" });

            const token = jwt.sign(
                { id: admin.id, role: "admin", department: department },
                process.env.JWT_SECRET,
                { expiresIn: "2h" }
            );

            res.cookie("token", token, {
                httpOnly: true,
                sameSite: "lax",
                secure: false,
                maxAge: 2 * 60 * 60 * 1000
            });

            return res.redirect(redirectURL);
        });
    }

    else
    {
        return res.render("login_page", { error: "Invalid role" });
    }
}

module.exports = { login_user };
