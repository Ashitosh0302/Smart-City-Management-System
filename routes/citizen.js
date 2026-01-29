const express = require("express");
const router = express.Router();
const UPLOAD = require("../middlewares/uploads_middlewares");

const {citizen_home,citizen_register_page,citizen_register,Water_Complaints,garbage_complaint,electricity_complaint,road_complaint,traffic_alerts,weather_alerts,hospital_appointments} = require("../controllers/citizen");
const {CREATE_WATER_COMPLAINT}=require("../controllers/water_complaints");
const {CREATE_GARBAGE_COMPLAINT}=require("../controllers/garbage_comlaints");
const {CREATE_ELECTRICITY_COMPLAINT}=require("../controllers/electricity_complaints");
const {CREATE_ROAD_COMPLAINT}=require("../controllers/roads_complaints");
const {CREATE_HOSPITAL_APPOINTMENT}=require("../controllers/hospital_appoitnment")

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
router.get("/appointments/hospital",hospital_appointments)
router.post("/appointments/hospital", CREATE_HOSPITAL_APPOINTMENT);

module.exports = router;