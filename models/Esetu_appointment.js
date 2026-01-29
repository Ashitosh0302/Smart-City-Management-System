const mongoose = require("mongoose");

const ESETU_APPOINTMENT_SCHEMA = new mongoose.Schema(
{
    appointmentId:
    {
        type: String,
        unique: true,
        required: true
    },

    citizen:
    {
        fullName:
        {
            type: String,
            required: true,
            trim: true
        },

        phone:
        {
            type: String,
            required: true,
            match: /^[0-9]{10}$/
        },

        email:
        {
            type: String,
            default: null
        }
    },

    service:
    {
        serviceType:
        {
            type: String,
            required: true
        },

        department:
        {
            type: String,
            required: true
        }
    },

    center:
    {
        centerName:
        {
            type: String,
            required: true
        },

        location:
        {
            type: String,
            required: true
        }
    },

    appointment:
    {
        date:
        {
            type: Date,
            required: true
        },

        timeSlot:
        {
            type: String,
            required: true
        }
    },

    remarks:
    {
        type: String,
        default: null
    },

    status:
    {
        type: String,
        enum: ["pending", "approved", "rejected", "completed"],
        default: "pending"
    }
},
{
    timestamps: true
});

module.exports = mongoose.model("EsetuAppointment", ESETU_APPOINTMENT_SCHEMA);
