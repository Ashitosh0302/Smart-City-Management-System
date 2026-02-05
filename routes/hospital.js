const express=require("express")
const router=express.Router()
const {hospital_home,hospital_register_page,hospital_register}=require("../controllers/hospital")
const {AUTH_MIDDLEWARE,HOSPITAL_ONLY}=require("../middlewares/auth_middlewares")

//hospital routes
router.get("/hospital_register",hospital_register_page)
router.post("/hospital_register",hospital_register)

//hospital home with JWT auth
router.use(AUTH_MIDDLEWARE, HOSPITAL_ONLY);
router.get("/",hospital_home)

module.exports=router