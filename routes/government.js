const express=require("express")
const router=express.Router()
const {government_home,government_register_page,government_register}=require("../controllers/government")

router.get("/",government_home)
router.get("/government_register",government_register_page)
router.post("/government_register",government_register)

module.exports=router