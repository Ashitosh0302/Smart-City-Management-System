const bcrypt = require("bcryptjs")
const Government=require("../models/government")

async function government_home(req, res)
{
    return res.render("government");
}

async function government_register_page(req,res) {
    return res.render("government_register")
}

async function government_register(req, res)
{
    const {
        email,
        password,
        confirm_password
    } = req.body;

    if(password !== confirm_password)
    {
        return res.render("government_register", {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Government.createGovernment(
        {
            email,
            password : password_hash
        },
        (error, result) =>
        {
            if(error)
            {
                console.error(error);
                return res.render("government_register", {
                    error: "Registration failed"
                });
            }

            req.session.government = {
                email: email
            };

            

            res.redirect("/");
        }
    );
}

module.exports={
    government_home,
    government_register_page,
    government_register
}