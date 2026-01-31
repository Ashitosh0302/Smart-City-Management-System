const MetroRoute = require("../models/metro/metro_route");
const MetroTicket = require("../models/metro/metro_ticket");

exports.GET_METRO_CITIES = async (req, res) =>
{
    const cities = await MetroRoute.distinct("cityName");
    res.json(cities);
};

exports.GET_METRO_STATIONS = async (req, res) =>
{
    const { cityName } = req.params;

    const fromStations = await MetroRoute.distinct("fromStation", { cityName });
    const toStations = await MetroRoute.distinct("toStation", { cityName });

    res.json({ fromStations, toStations });
};

exports.SEARCH_METROS = async (req, res) =>
{
    const { cityName, fromStation, toStation } = req.body;

    const metros = await MetroRoute.find(
    {
        cityName,
        fromStation,
        toStation,
        availableTokens: { $gt: 0 }
    });

    res.json(metros);
};

exports.BOOK_METRO_TICKET = async (req, res) =>
{
    const { routeId, citizenName, travelDate } = req.body;

    const route = await MetroRoute.findById(routeId);

    if(!route || route.availableTokens === 0)
    {
        return res.status(400).json(
        {
            success: false,
            message: "Tokens not available"
        });
    }

    route.availableTokens -= 1;
    await route.save();

    const ticket = new MetroTicket(
    {
        citizenName,
        cityName: route.cityName,
        fromStation: route.fromStation,
        toStation: route.toStation,
        metroLine: route.metroLine,
        metroNumber: route.metroNumber,
        travelDate,
        tokenNumber: route.availableTokens + 1,
        fare: route.fare
    });

    await ticket.save();

    res.json(
    {
        success: true,
        message: "Metro ticket booked successfully",
        ticket
    });
};
