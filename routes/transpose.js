const express=require("express")
const router=express.Router()
const {Transpose_home,Bus_transpose_home,Train_transpose_home,metro_transpose_home}=require("../controllers/transpose")

router.get("/",Transpose_home)
router.get("/bus",Bus_transpose_home)
router.get("/train",Train_transpose_home)
router.get("/metro",metro_transpose_home)

module.exports=router