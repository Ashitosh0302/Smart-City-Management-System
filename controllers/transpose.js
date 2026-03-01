const bcrypt=require("bcryptjs")
const Transport=require("../models/transpose")

async function Transpose_home(req,res) {
    return res.render("transport_home_page")
}

async function transpose_register_page(req,res) {
    return res.render("transport_register")
}

async function Bus_transpose_home(req,res) {
    return res.render("bus_dashboard")
}

async function Train_transpose_home(req,res) {
    return res.render("train_dashboard")
}

async function metro_transpose_home(req,res) {
    return res.render("metro_dashboard")
}

async function transport_register(req, res)
{
    const {
        email,
        password,
        confirm_password
    } = req.body;

    if(password !== confirm_password)
    {
        return res.render("transport_register", {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Transport.createTransport(
        {
            email,
            password: password_hash
        },
        (error) =>
        {
            if(error)
            {
                console.error(error);
                return res.render("transport_register", {
                    error: "Registration failed"
                });
            }

            // After successful registration, go to common login (JWT-based)
            return res.redirect("/login");
        }
    );
}

module.exports={
    Transpose_home,
    Bus_transpose_home,
    Train_transpose_home,
    metro_transpose_home,
    transport_register,
    transpose_register_page
}