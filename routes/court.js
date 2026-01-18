const express=require("express")
const router=express.Router()
const {court_home}=require("../controllers/court")

router.get("/",court_home)

module.exports=router