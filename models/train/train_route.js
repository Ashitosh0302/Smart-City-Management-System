const mongoose = require("mongoose");

const TRAIN_ROUTE_SCHEMA = new mongoose.Schema(
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

    trainName:
    {
        type: String,
        required: true
    },

    trainNumber:
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

    availableSeats:
    {
        type: Number,
        required: true
    }
});

module.exports = mongoose.model("TrainRoute", TRAIN_ROUTE_SCHEMA);
