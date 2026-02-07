const bcrypt = require("bcryptjs");
const Hospital = require("../models/hospital");
const HospitalAppointment = require("../models/hospital_appointment");

// =====================
// HOSPITAL AUTH
// =====================
async function hospital_home(req, res)
{
    return res.render("hospital");
}

async function hospital_register_page(req, res)
{
    return res.render("hospital_register");
}

async function hospital_register(req, res)
{
    const { email, password, confirm_password } = req.body;

    if(password !== confirm_password)
    {
        return res.render("hospital_register",
        {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Hospital.createHospital(
        {
            email,
            password: password_hash
        },
        (error) =>
        {
            if(error)
            {
                return res.render("hospital_register",
                {
                    error: "Registration failed"
                });
            }

            res.redirect("/hospital");
        }
    );
}

// =====================
// HOSPITAL APPOINTMENTS
// =====================
async function hospital_appointments_view(req, res)
{
    try
    {
        const appointments = await HospitalAppointment.find({});

        // 🔁 map ONLY what frontend expects
        const formattedAppointments = appointments.map(app => ({
            _id: app._id,
            fullName: app.patientName,
            age: app.age,
            gender: app.gender,
            contactNumber: app.contactNumber,
            department: app.purpose || "General",

            appointmentDate: app.appointmentDate,
            appointmentTime: app.timeSlot,   // 🔥 MATCH FRONTEND
            urgency: app.urgency || "normal",
            status: app.status || "pending",

            createdAt: app.createdAt
        }));

        // ✅ SAME AS COURT
        if (req.headers.accept && req.headers.accept.includes("application/json"))
        {
            return res.json({
                success: true,
                appointments: formattedAppointments
            });
        }

        return res.render("hospital", {
            appointments: formattedAppointments
        });
    }
    catch (error)
    {
        return res.json({
            success: false,
            appointments: []
        });
    }
}

async function getHospitalAppointmentById(req, res)
{
    const appointment = await HospitalAppointment.findById(req.params.id);
    return res.json(appointment);
}

async function updateHospitalAppointment(req, res)
{
    await HospitalAppointment.findByIdAndUpdate(
        req.params.id,
        req.body,
        { new: true }
    );

    return res.json({
        success: true,
        message: "Appointment updated"
    });
}

module.exports =
{
    hospital_home,
    hospital_register_page,
    hospital_register,
    hospital_appointments_view,
    getHospitalAppointmentById,
    updateHospitalAppointment,
};
