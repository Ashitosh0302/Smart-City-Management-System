const express = require("express");
const router = express.Router();
const {government_home,government_register_page,government_register,water_complaints_view,getComplaintById,updateComplaint,garbage_complaints_view,getGarbageComplaintById,updateGarbageComplaint} = require("../controllers/government");
const { AUTH_MIDDLEWARE, GOVERNMENT_ONLY } = require("../middlewares/auth_middlewares");

// Public routes
router.get("/government_register", government_register_page);
router.post("/government_register", government_register);

// ✅ Protected routes (require authentication)
router.use(AUTH_MIDDLEWARE, GOVERNMENT_ONLY);

// Government dashboard
router.get("/", government_home);

//Water complaints - same route for both HTML and JSON
router.get("/complaints/water", water_complaints_view);
router.get("/complaints/water/:id", getComplaintById);
router.put("/complaints/water/:id", updateComplaint);

//garbage complaints
router.get("/government/garbage", garbage_complaints_view);
router.get("/government/garbage/:id", getGarbageComplaintById);
router.put("/government/garbage/:id", updateGarbageComplaint);

module.exports = router;