const bcrypt = require("bcryptjs");
const Citizen = require("../models/citizen");
const Government = require("../models/government");
const Court = require("../models/court");
const Hospital = require("../models/hospital");

async function login_user(req, res)
{
    const { role, department, email, password } = req.body;

    // ===== CITIZEN LOGIN =====
    if(role === "citizen")
    {
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
            return res.redirect("/citizen");
        });

        return;
    }

    // ===== GOVERNMENT LOGIN =====
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
            return res.redirect("/government");
        });

        return;
    }

    // ===== COURT LOGIN =====
    if(role === "admin" && department === "court")
    {
        Court.findByEmail(email, (err, court) =>
        {
            if(err || !court)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            const match = bcrypt.compareSync(password, court.password);
            if(!match)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            req.session.court = court;
            return res.redirect("/court");
        });

        return;
    }

    // ===== HOSPITAL LOGIN =====
    if(role === "admin" && department === "hospital")
    {
        Hospital.findByEmail(email, (err, hospital) =>
        {
            if(err || !hospital)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            const match = bcrypt.compareSync(password, hospital.password);
            if(!match)
            {
                return res.render("login_page", { error: "Invalid credentials" });
            }

            req.session.hospital = hospital;
            return res.redirect("/hospital");
        });

        return;
    }

    // ===== FALLBACK =====
    return res.render("login_page", { error: "Invalid login" });
}

module.exports = {
    login_user
};
