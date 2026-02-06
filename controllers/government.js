const bcrypt = require("bcryptjs");
const Government = require("../models/government");
const { ObjectId } = require("mongodb");

// =====================
// GOVERNMENT AUTH
// =====================
async function government_home(req, res)
{
    return res.render("government");
}

async function government_register_page(req, res)
{
    return res.render("government_register");
}

async function government_register(req, res)
{
    const { email, password, confirm_password } = req.body;

    if(password !== confirm_password)
    {
        return res.render("government_register", {
            error: "Passwords do not match"
        });
    }

    const password_hash = bcrypt.hashSync(password, 10);

    Government.createGovernment(
        {
            email,
            password: password_hash
        },
        (error, result) =>
        {
            if(error)
            {
                console.error(error);
                return res.render("government_register", {
                    error: "Registration failed"
                });
            }

            req.session.government = { email };
            res.redirect("/");
        }
    );
}

// =====================
// WATER COMPLAINTS
// =====================
async function water_complaints_view(req, res)
{
    try
    {
        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        if(!db)
        {
            throw new Error("Database not connected");
        }

        const complaints = await db
            .collection("watercomplaints")
            .find({})
            .sort({ createdAt: -1 })
            .toArray();

        if(req.headers.accept && req.headers.accept.includes("application/json"))
        {
            return res.json({ success: true, complaints });
        }

        return res.render("water_government", { complaints });
    }
    catch(error)
    {
        console.error(error);

        return res.render("water_government", {
            complaints: [],
            error: error.message
        });
    }
}

async function getComplaintById(req, res)
{
    try
    {
        const { id } = req.params;
        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        const complaint = await db
            .collection("watercomplaints")
            .findOne({ _id: new ObjectId(id) });

        if(!complaint)
        {
            return res.status(404).json({
                success: false,
                message: "Complaint not found"
            });
        }

        return res.json({ success: true, complaint });
    }
    catch(error)
    {
        return res.status(500).json({
            success: false,
            message: error.message
        });
    }
}

async function updateComplaint(req, res)
{
    try
    {
        const { id } = req.params;
        const updateData = req.body;

        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        updateData.updatedAt = new Date();

        const result = await db
            .collection("watercomplaints")
            .findOneAndUpdate(
                { _id: new ObjectId(id) },
                { $set: updateData },
                { returnDocument: "after" }
            );

        if(!result.value)
        {
            return res.status(404).json({
                success: false,
                message: "Complaint not found"
            });
        }

        return res.json({
            success: true,
            message: "Updated successfully",
            complaint: result.value
        });
    }
    catch(error)
    {
        return res.status(500).json({
            success: false,
            message: error.message
        });
    }
}

// =====================
// 🆕 GARBAGE COMPLAINTS
// =====================
async function garbage_complaints_view(req, res)
{
    try
    {
        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        if(!db)
        {
            throw new Error("Database not connected");
        }

        const complaints = await db
            .collection("garbagecomplaints")
            .find({})
            .sort({ createdAt: -1 })
            .toArray();

        if(req.headers.accept && req.headers.accept.includes("application/json"))
        {
            return res.json({ success: true, complaints });
        }

        return res.render("garbage_government", { complaints });
    }
    catch(error)
    {
        console.error(error);

        return res.render("garbage_government", {
            complaints: [],
            error: error.message
        });
    }
}

async function getGarbageComplaintById(req, res)
{
    try
    {
        const { id } = req.params;
        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        const complaint = await db
            .collection("garbagecomplaints")
            .findOne({ _id: new ObjectId(id) });

        if(!complaint)
        {
            return res.status(404).json({
                success: false,
                message: "Garbage complaint not found"
            });
        }

        return res.json({ success: true, complaint });
    }
    catch(error)
    {
        return res.status(500).json({
            success: false,
            message: error.message
        });
    }
}

async function updateGarbageComplaint(req, res)
{
    try
    {
        const { id } = req.params;
        const updateData = req.body;

        const mongoose = require("mongoose");
        const db = mongoose.connection.db;

        updateData.updatedAt = new Date();

        const result = await db
            .collection("garbagecomplaints")
            .findOneAndUpdate(
                { _id: new ObjectId(id) },
                { $set: updateData },
                { returnDocument: "after" }
            );

        if(!result.value)
        {
            return res.status(404).json({
                success: false,
                message: "Garbage complaint not found"
            });
        }

        return res.json({
            success: true,
            message: "Updated successfully",
            complaint: result.value
        });
    }
    catch(error)
    {
        return res.status(500).json({
            success: false,
            message: error.message
        });
    }
}

// =====================
// EXPORTS
// =====================
module.exports = {
    government_home,
    government_register_page,
    government_register,

    water_complaints_view,
    getComplaintById,
    updateComplaint,

    garbage_complaints_view,
    getGarbageComplaintById,
    updateGarbageComplaint
};
