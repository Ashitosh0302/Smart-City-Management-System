const express=require("express")
const router=express.Router()
const {government_home,government_register_page,government_register}=require("../controllers/government")
const {AUTH_MIDDLEWARE,GOVERNMENT_ONLY}=require("../middlewares/auth_middlewares")

//government routes
router.get("/government_register",government_register_page)
router.post("/government_register",government_register)

//government home with JWT auth
router.get("/",government_home)

module.exports=router