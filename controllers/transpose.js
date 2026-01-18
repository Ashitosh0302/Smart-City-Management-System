async function Transpose_home(req,res) {
    return res.render("transport_home_page")
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

module.exports={
    Transpose_home,
    Bus_transpose_home,
    Train_transpose_home,
    metro_transpose_home
}