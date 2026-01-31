// controllers/citizenBusController.js
const BusRoute = require("../models/bus/bus_route");
const BusTicket = require("../models/bus/bus_ticket");

exports.GET_CITIES = async (req, res) =>
{
    const cities = await BusRoute.distinct("cityName");
    res.json(cities);
};

exports.GET_STATIONS = async (req, res) =>
{
    const { cityName } = req.params;

    const fromStations = await BusRoute.distinct("fromStation", { cityName });
    const toStations = await BusRoute.distinct("toStation", { cityName });

    res.json({ fromStations, toStations });
};

exports.SEARCH_BUSES = async (req, res) =>
{
    const { cityName, fromStation, toStation } = req.body;

    const buses = await BusRoute.find(
    {
        cityName,
        fromStation,
        toStation,
        availableSeats: { $gt: 0 }
    });

    res.json(buses);
};

exports.BOOK_TICKET = async (req, res) =>
{
    const { routeId, citizenName, travelDate } = req.body;

    const route = await BusRoute.findById(routeId);

    if(!route || route.availableSeats === 0)
    {
        return res.status(400).json(
        {
            success: false,
            message: "Seats not available"
        });
    }

    const seatNumber = route.availableSeats;

    route.availableSeats -= 1;
    await route.save();

    const ticket = new BusTicket(
    {
        citizenName,
        cityName: route.cityName,
        fromStation: route.fromStation,
        toStation: route.toStation,
        busName: route.busName,
        travelDate,
        seatNumber,
        fare: route.fare
    });

    await ticket.save();

    res.json(
    {
        success: true,
        message: "Ticket booked successfully",
        ticket
    });
};
