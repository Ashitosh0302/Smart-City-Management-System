const express=require("express")
const router=express.Router()
const {hospital_home,hospital_register_page,hospital_register}=require("../controllers/hospital")

router.get("/",hospital_home)
router.get("/hospital_register",hospital_register_page)
router.post("/hospital_register",hospital_register)

module.exports=router