const TrainRoute = require("../models/train/train_route");
const TrainTicket = require("../models/train/train_ticket");

exports.GET_TRAIN_CITIES = async (req, res) =>
{
    const cities = await TrainRoute.distinct("cityName");
    res.json(cities);
};

exports.GET_TRAIN_STATIONS = async (req, res) =>
{
    const { cityName } = req.params;

    const fromStations = await TrainRoute.distinct("fromStation", { cityName });
    const toStations = await TrainRoute.distinct("toStation", { cityName });

    res.json({ fromStations, toStations });
};

exports.SEARCH_TRAINS = async (req, res) =>
{
    const { cityName, fromStation, toStation } = req.body;

    const trains = await TrainRoute.find(
    {
        cityName,
        fromStation,
        toStation,
        availableSeats: { $gt: 0 }
    });

    res.json(trains);
};

exports.BOOK_TRAIN_TICKET = async (req, res) =>
{
    const { routeId, citizenName, travelDate } = req.body;

    const route = await TrainRoute.findById(routeId);

    if(!route || route.availableSeats === 0)
    {
        return res.status(400).json(
        {
            success: false,
            message: "Seats not available"
        });
    }

    route.availableSeats -= 1;
    await route.save();

    const ticket = new TrainTicket(
    {
        citizenName,
        cityName: route.cityName,
        fromStation: route.fromStation,
        toStation: route.toStation,
        trainName: route.trainName,
        trainNumber: route.trainNumber,
        travelDate,
        seatNumber: route.availableSeats + 1,
        fare: route.fare
    });

    await ticket.save();

    res.json(
    {
        success: true,
        message: "Train ticket booked successfully",
        ticket
    });
};
