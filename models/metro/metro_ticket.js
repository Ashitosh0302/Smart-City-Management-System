const mongoose = require("mongoose");

const METRO_TICKET_SCHEMA = new mongoose.Schema(
{
    citizenName:
    {
        type: String,
        required: true
    },

    cityName:
    {
        type: String,
        required: true
    },

    fromStation:
    {
        type: String,
        required: true
    },

    toStation:
    {
        type: String,
        required: true
    },

    metroLine:
    {
        type: String,
        required: true
    },

    metroNumber:
    {
        type: String,
        required: true
    },

    travelDate:
    {
        type: Date,
        required: true
    },

    tokenNumber:
    {
        type: Number,
        required: true
    },

    fare:
    {
        type: Number,
        required: true
    },

    bookingTime:
    {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model("MetroTicket", METRO_TICKET_SCHEMA);
