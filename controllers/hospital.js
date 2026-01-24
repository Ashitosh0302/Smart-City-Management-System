const bcrypt = require("bcryptjs")
const Hospital = require("../models/hospital")

async function hospital_home(req, res) {
    return res.render("hospital")
}

async function hospital_register_page(req, res) {
    return res.render("hospital_register")
}

async function hospital_register(req, res) {
    const {
        email,
        password,
        confirm_password
    } = req.body;

    if (password !== confirm_password) {
        return res.render("hospital_register", {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Hospital.createHospital(
        {
            email,
            password: password_hash
        },
        (error, result) => {
            if (error) {
                console.error(error);
                return res.render("hospital_register", {
                    error: "Registration failed"
                });
            }

            req.session.hospital = {
                email: email
            };

            res.redirect("/");
        }
    );
}

module.exports = {
    hospital_home,
    hospital_register_page,
    hospital_register
}