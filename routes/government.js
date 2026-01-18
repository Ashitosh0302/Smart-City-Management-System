const express=require("express")
const router=express.Router()
const {government_home}=require("../controllers/government")

router.get("/",government_home)

module.exports=router