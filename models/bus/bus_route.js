// models/BusRoute.js
const mongoose = require("mongoose");

const BUS_ROUTE_SCHEMA = new mongoose.Schema(
{
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

    departureTime:
    {
        type: String,
        required: true
    },

    fare:
    {
        type: Number,
        required: true
    },

    availableSeats:
    {
        type: Number,
        required: true
    }
});

module.exports = mongoose.model("BusRoute", BUS_ROUTE_SCHEMA);
