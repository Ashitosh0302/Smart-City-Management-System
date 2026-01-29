const EsetuAppointment = require("../models/Esetu_appointment");

const CREATE_ESETU_APPOINTMENT = async (req, res) =>
{
    try
    {
        const appointmentId = "ESETU-" + Date.now().toString().slice(-8);

        const appointment = new EsetuAppointment(
        {
            appointmentId: appointmentId,

            citizen:
            {
                fullName: req.body["citizen[fullName]"],
                phone: req.body["citizen[phone]"],
                email: req.body["citizen[email]"] || null
            },

            service:
            {
                serviceType: req.body["service[serviceType]"],
                department: req.body["service[department]"]
            },

            center:
            {
                centerName: req.body["center[centerName]"],
                location: req.body["center[location]"]
            },

            appointment:
            {
                date: req.body["appointment[date]"],
                timeSlot: req.body["appointment[timeSlot]"]
            },

            remarks: req.body.remarks || null
        });

        await appointment.save();

        return res.status(201).json(
        {
            success: true,
            message: "E-Setu appointment booked successfully",
            appointmentId: appointmentId
        });
    }
    catch(error)
    {
        return res.status(500).json(
        {
            success: false,
            message: "Failed to book appointment",
            error: error.message
        });
    }
};

module.exports =
{
    CREATE_ESETU_APPOINTMENT,
};
