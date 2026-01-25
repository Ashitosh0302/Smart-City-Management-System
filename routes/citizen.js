const express = require("express");
const router = express.Router();

const {citizen_home,citizen_register_page,citizen_register,Water_Complaints} = require("../controllers/citizen");

router.get("/", citizen_home);
router.get("/citizen_register", citizen_register_page);
router.post("/citizen_register", citizen_register);

router.get("/complaints/water",Water_Complaints)
module.exports = router;