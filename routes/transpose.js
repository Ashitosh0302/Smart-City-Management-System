const express=require("express")
const router=express.Router()
const {Transpose_home,Bus_transpose_home,Train_transpose_home,metro_transpose_home,transport_register,transpose_register_page}=require("../controllers/transpose")

router.get("/",Transpose_home)
router.get("/transpose_register",transpose_register_page)
router.post("/transpose_register",transport_register)
router.get("/bus",Bus_transpose_home)
router.get("/train",Train_transpose_home)
router.get("/metro",metro_transpose_home)

module.exports=router