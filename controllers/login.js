const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const Citizen = require("../models/citizen");
const Government = require("../models/government");

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
            {
                return res.render("login_page", { error: "Invalid email or password" });
            }

            if(!bcrypt.compareSync(password, citizen.password))
            {
                return res.render("login_page", { error: "Invalid email or password" });
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
        {
            return res.render("login_page", { error: "Please select department" });
        }

        // ---- GOVERNMENT ADMIN ----
        if(department === "government")
        {
            Government.findByEmail(email, (err, government) =>
            {
                if(err || !government)
                {
                    return res.render("login_page", { error: "Invalid email or password" });
                }

                if(!bcrypt.compareSync(password, government.password))
                {
                    return res.render("login_page", { error: "Invalid email or password" });
                }

                const token = jwt.sign(
                    {
                        id: government.id,
                        role: "admin",
                        department: "government"
                    },
                    process.env.JWT_SECRET,
                    { expiresIn: "2h" }
                );

                res.cookie("token", token, {
                    httpOnly: true,
                    sameSite: "lax",
                    secure: false,
                    maxAge: 2 * 60 * 60 * 1000
                });

                return res.redirect("/government");
            });
        }

        // future departments
        else
        {
            return res.render("login_page", { error: "Invalid department" });
        }
    }

    else
    {
        return res.render("login_page", { error: "Invalid role" });
    }
}

module.exports = { login_user };
