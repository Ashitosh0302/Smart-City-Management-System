const mongoose = require("mongoose");

const METRO_ROUTE_SCHEMA = new mongoose.Schema(
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

    departureTime:
    {
        type: String,
        required: true
    },

    arrivalTime:
    {
        type: String,
        required: true
    },

    fare:
    {
        type: Number,
        required: true
    },

    availableTokens:
    {
        type: Number,
        required: true
    }
});

module.exports = mongoose.model("MetroRoute", METRO_ROUTE_SCHEMA);
