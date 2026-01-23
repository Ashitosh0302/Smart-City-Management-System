const express = require("express");
const router = express.Router();

const {citizen_home,citizen_register_page,citizen_register} = require("../controllers/citizen");

router.get("/", citizen_home);
router.get("/citizen_register", citizen_register_page);
router.post("/citizen_register", citizen_register);

module.exports = router;