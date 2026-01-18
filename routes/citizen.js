const express=require("express")
const router=express.Router()
const {citizen_home}=require("../controllers/citizen")

router.get("/",citizen_home)

module.exports=router