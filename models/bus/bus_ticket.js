// models/BusTicket.js
const mongoose = require("mongoose");

const BUS_TICKET_SCHEMA = new mongoose.Schema(
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

    busName:
    {
        type: String,
        required: true
    },

    travelDate:
    {
        type: Date,
        required: true
    },

    seatNumber:
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

module.exports = mongoose.model("BusTicket", BUS_TICKET_SCHEMA);
