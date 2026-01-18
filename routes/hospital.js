const express=require("express")
const router=express.Router()
const {hospital_home}=require("../controllers/hospital")

router.get("/",hospital_home)

module.exports=router