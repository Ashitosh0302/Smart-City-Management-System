const multer = require("multer");
const path = require("path");

const storage = multer.diskStorage({
    destination: (req, file, cb) =>
    {
        cb(null, "uploads/complaints");
    },
    filename: (req, file, cb) =>
    {
        const uniqueName =
            Date.now() + "-" + Math.round(Math.random() * 1E9) +
            path.extname(file.originalname);

        cb(null, uniqueName);
    }
});

const fileFilter = (req, file, cb) =>
{
    const allowedTypes = /jpeg|jpg|png|mp4|mov/;
    const ext = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mime = allowedTypes.test(file.mimetype);

    if(ext && mime)
    {
        cb(null, true);
    }
    else
    {
        cb(new Error("Only images and videos are allowed"));
    }
};

exports.UPLOAD = multer({
    storage: storage,
    fileFilter: fileFilter,
    limits: { fileSize: 10 * 1024 * 1024 }
});
