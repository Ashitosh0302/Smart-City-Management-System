const bcrypt = require("bcryptjs");
const Court = require("../models/court");

async function court_home(req,res) {
    return res.render("court")
}

async function court_register_page(req,res) {
    return res.render("court_register")
}

async function court_register(req, res)
{
    const {
        email,
        password,
        confirm_password
    } = req.body;

    if(password !== confirm_password)
    {
        return res.render("court_register", {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Court.createCourt(
        {
            email,
            password: password_hash
        },
        (error, result) =>
        {
            if(error)
            {
                console.error(error);
                return res.render("court_register", {
                    error: "Registration failed"
                });
            }

            req.session.court = {
                email: email
            };

            res.redirect("/");
        }
    );
}

module.exports={
    court_home,
    court_register_page,
    court_register
}