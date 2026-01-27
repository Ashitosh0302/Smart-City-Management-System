const express = require("express");
const router = express.Router();

const {citizen_home,citizen_register_page,citizen_register,Water_Complaints,garbage_complaint,electricity_complaint,road_complaint} = require("../controllers/citizen");

router.get("/", citizen_home);
router.get("/citizen_register", citizen_register_page);
router.post("/citizen_register", citizen_register);

//water
router.get("/complaints/water",Water_Complaints)
// router.post("/complaints/water",)

//garbage
router.get("/complaints/garbage",garbage_complaint)

//electricity
router.get("/complaints/electricity",electricity_complaint)

//roads
router.get("/complaints/roads",road_complaint)

module.exports = router;