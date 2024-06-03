db.createView("clientWithHostname", "clientList", [
    {
        $lookup:
        {
            from: "ip",
            localField: "ip",
            foreignField: "IP",
            as: "hostname"
        }
    },
    {
        $project:
        {
            _id: 0,
            ip: 1,
            ap: 1,
            hostname: "$hostname.hostname"
        }
    }
])

db.clientWithHostname.aggregate([
    {
        $group:
        {
            ip: 1,
            ap: 1,
            hostname: "$hostname.hostname"
        }
    }
])

//inner join de clientes para saber el hostname
db.clientList.aggregate([
    {
        $lookup: {
            from: "inventary",
            localField: "ip",
            foreignField: "inventary_ip",
            as: "fromInventary"
        }
    },
    {
        $replaceRoot: { newRoot: { $mergeObjects: [{ $arrayElemAt: ["$fromInventary", 0] }, "$$ROOT"] } }
    },
    { $project: { fromInventary: 0 } }
])

//inner join para aps
db.apList.aggregate([
    {
        $lookup: {
            from: "inventary",
            localField: "ip",
            foreignField: "inventary_ip",
            as: "fromInventary"
        }
    },
    {
        $replaceRoot: { newRoot: { $mergeObjects: [{ $arrayElemAt: ["$fromInventary", 0] }, "$$ROOT"] } }
    },
    { $project: { fromInventary: 0 } }
])




db.createView("clientsHostname", "clientList", [
    {
        $lookup: {
            from: "ip",
            localField: "ip",
            foreignField: "inventary_ip",
            as: "fromInventary"
        }
    },
    {
        $replaceRoot: { newRoot: { $mergeObjects: [{ $arrayElemAt: ["$fromInventary", 0] }, "$$ROOT"] } }
    },
    { $project: { fromInventary: 0 } }
])

db.clientList.aggregate([
    {
        $lookup: {
            from: "inventary",
            localField: "ip",
            foreignField: "inventary_ip",
            as: "fromInventary"
        }
    },
    {
        $project: {
            // Selecciona los campos deseados de ambas colecciones
            "ip": 1,
            "ap": 1,
            $arrayElemAt: ["$fromInventary.hostname", 1]
            // ...
        }
    }
])