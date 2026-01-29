const mongoose = require("mongoose");

const HOSPITAL_APPOINTMENT_SCHEMA = new mongoose.Schema(
{
    hospitalName:
    {
        type: String,
        required: true
    },

    hospitalAddress:
    {
        type: String,
        required: true
    },

    hospitalContact:
    {
        type: String,
        required: true
    },

    patientName:
    {
        type: String,
        required: true
    },

    age:
    {
        type: Number,
        required: true
    },

    gender:
    {
        type: String,
        enum: ["male", "female", "other"],
        required: true
    },

    contactNumber:
    {
        type: String,
        required: true
    },

    address:
    {
        type: String
    },

    purpose:
    {
        type: String,
        required: true
    },

    appointmentDate:
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
{
    timestamps: true
});

module.exports = mongoose.model("HospitalAppointment", HOSPITAL_APPOINTMENT_SCHEMA);
