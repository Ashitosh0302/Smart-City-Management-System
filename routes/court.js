const express=require("express")
const router=express.Router()
const {court_home,court_register_page,court_register}=require("../controllers/court")

router.get("/",court_home)
router.get("/court_register",court_register_page)
router.post("/court_register",court_register)

module.exports=router