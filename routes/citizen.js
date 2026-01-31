const express = require("express");
const router = express.Router();
const UPLOAD = require("../middlewares/uploads_middlewares");
const multer = require("multer");

const upload = multer(); // memory storage

const {citizen_home,citizen_register_page,citizen_register,Water_Complaints,garbage_complaint,electricity_complaint,road_complaint,traffic_alerts,weather_alerts,hospital_appointments,court_appointments,Esetu_appointments,police_alerts,ambulance_alerts,fire_alerts} = require("../controllers/citizen");
const {CREATE_WATER_COMPLAINT}=require("../controllers/water_complaints");
const {CREATE_GARBAGE_COMPLAINT}=require("../controllers/garbage_comlaints");
const {CREATE_ELECTRICITY_COMPLAINT}=require("../controllers/electricity_complaints");
const {CREATE_ROAD_COMPLAINT}=require("../controllers/roads_complaints");
const {CREATE_HOSPITAL_APPOINTMENT}=require("../controllers/hospital_appoitnment")
const {CREATE_COURT_APPOINTMENT}=require("../controllers/court_appointment")
const {bookAppointment}=require("../controllers/Esetu_appointment")
const {CREATE_EMERGENCY_ALERT_police}=require("../controllers/police_emergency")
const {CREATE_AMBULANCE_REQUEST}=require("../controllers/ambulance_emergency")
const {CREATE_FIRE_EMERGENCY_REQUEST}=require("../controllers/fire_emergency")
const {GET_CITIES, GET_STATIONS, SEARCH_BUSES, BOOK_TICKET} = require("../controllers/bus");
const {GET_TRAIN_CITIES, GET_TRAIN_STATIONS, SEARCH_TRAINS, BOOK_TRAIN_TICKET} = require("../controllers/train");
const {GET_METRO_CITIES, GET_METRO_STATIONS, SEARCH_METROS, BOOK_METRO_TICKET} = require("../controllers/metro");

router.get("/", citizen_home);
router.get("/citizen_register", citizen_register_page);
router.post("/citizen_register", citizen_register);

//water
router.get("/complaints/water",Water_Complaints)
router.post("/complaints/water",UPLOAD.array("media", 5),CREATE_WATER_COMPLAINT);

//garbage
router.get("/complaints/garbage",garbage_complaint)
router.post("/complaints/garbage",UPLOAD.array("media", 5),CREATE_GARBAGE_COMPLAINT);

//electricity
router.get("/complaints/electricity",electricity_complaint)
router.post("/complaints/electricity",UPLOAD.array("media", 5),CREATE_ELECTRICITY_COMPLAINT);

//roads
router.get("/complaints/roads",road_complaint)
router.post("/complaints/roads",UPLOAD.array("media", 5),CREATE_ROAD_COMPLAINT);

//alerts
router.get("/alerts/traffic",traffic_alerts)
router.get("/alerts/weather",weather_alerts)

//appointments
//hospital
router.get("/appointments/hospital",hospital_appointments)
router.post("/appointments/hospital", CREATE_HOSPITAL_APPOINTMENT);

//court
router.get("/appointments/court",court_appointments)
router.post("/appointments/court",CREATE_COURT_APPOINTMENT);

//E-setu
router.get("/appointments/Esetu",Esetu_appointments)
router.post("/appointments/Esetu",upload.none(),bookAppointment);

//alerts
//police
router.get("/emergency/police",police_alerts)
router.post("/emergency/police",CREATE_EMERGENCY_ALERT_police);

//ambulance
router.get("/emergency/ambulance",ambulance_alerts)
router.post("/emergency/ambulance",CREATE_AMBULANCE_REQUEST)

//fire
router.get("/emergency/fire",fire_alerts)
router.post("/emergency/fire",CREATE_FIRE_EMERGENCY_REQUEST)

//booking
//bus
router.get("/cities", GET_CITIES);
router.get("/stations/:cityName", GET_STATIONS);
router.post("/search_buses", SEARCH_BUSES);
router.post("/book_ticket", BOOK_TICKET);

//train
router.get("/train_cities", GET_TRAIN_CITIES);
router.get("/train_stations/:cityName", GET_TRAIN_STATIONS);
router.post("/search_trains", SEARCH_TRAINS);
router.post("/book_train_ticket", BOOK_TRAIN_TICKET);

//metro
router.get("/metro_cities", GET_METRO_CITIES);
router.get("/metro_stations/:cityName", GET_METRO_STATIONS);
router.post("/search_metros", SEARCH_METROS);
router.post("/book_metro_ticket", BOOK_METRO_TICKET);

module.exports = router;