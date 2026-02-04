const express=require("express")
const router=express.Router()
const {court_home,court_register_page,court_register}=require("../controllers/court")
const {AUTH_MIDDLEWARE,COURT_ONLY}=require("../middlewares/auth_middlewares")

//court routes
router.get("/court_register",court_register_page)
router.post("/court_register",court_register)

//court home with JWT auth
router.get("/",court_home)

module.exports=router