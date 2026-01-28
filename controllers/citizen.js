const bcrypt = require("bcryptjs");
const Citizen = require("../models/citizen");

async function citizen_home(req,res) {
    if (!req.session.citizen) {
        return res.redirect("/login");
    }

    return res.render("citizen_dashboard", { citizen: req.session.citizen });
}

async function citizen_register_page(req, res)
{
    return res.render("citizen_register");
}

async function citizen_register(req, res)
{
    const {
        first_name,
        last_name,
        username,
        email,
        phone_number,
        password,
        confirm_password,
        gender,
        city
    } = req.body;

    if(password !== confirm_password)
    {
        return res.render("citizen_register", {
            error: "Passwords do not match"
        });
    }

    const full_name = first_name + " " + last_name;
    const password_hash = bcrypt.hashSync(password, 10);

    Citizen.createCitizen(
        {
            full_name,
            username,
            email,
            phone_number,
            password: password_hash,
            gender,
            city
        },
        (error) =>
        {
            if(error)
            {
                console.error(error);
                return res.render("citizen_register", {
                    error: "Registration failed"
                });
            }

            req.session.citizen = {
                id: user.id,
                full_name: user.full_name,
                username: user.username,
                email: user.email
            };

            res.redirect("/");
        }
    );
}

//water complaints
async function Water_Complaints(req,res) {
    return res.render("water");
}

//garbage complaints
async function garbage_complaint(req,res) {
    return res.render("garbage");
}

//electricity complaints
async function electricity_complaint(req,res) {
    return res.render("electricity");
}

//road complaints
async function road_complaint(req,res) {
    return res.render("road");
}

//alerts
async function traffic_alerts(req,res) {
    return res.render("traffic_alerts");
}

async function weather_alerts(req,res) {
    return res.render("weather_alerts");
}

module.exports = {
    citizen_home,
    citizen_register_page,
    citizen_register,
    Water_Complaints,
    garbage_complaint,
    electricity_complaint,
    road_complaint,
    traffic_alerts,
    weather_alerts
};
