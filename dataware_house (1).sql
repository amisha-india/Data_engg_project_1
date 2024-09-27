Create Database EnergyProjectDB
Use EnergyProjectDB
CREATE TABLE DeviceInformation (
    DeviceID INT IDENTITY(1,1) PRIMARY KEY,
    DeviceType VARCHAR(50) NOT NULL,
    InstallationDate DATE NOT NULL,
    Location VARCHAR(100) NOT NULL
);

CREATE TABLE UserProfiles (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(100),
    Address VARCHAR(200),
    AccountCreationDate DATE NOT NULL
);


CREATE TABLE EnergyConsumption (
    ConsumptionID INT IDENTITY(1,1) PRIMARY KEY,
    Timestamp DATETIME NOT NULL,
    DeviceID INT NOT NULL,
    UserID INT NOT NULL,
    EnergyConsumed DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (DeviceID) REFERENCES DeviceInformation(DeviceID),
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID)
);

-- Analyze Energy Consumption Patterns
SELECT 
    EC.UserID, 
    EC.DeviceID, 
    FORMAT(EC.Timestamp, 'yyyy-MM-dd HH:00:00') AS Hour, 
    SUM(EC.EnergyConsumed) AS TotalEnergy
FROM 
    EnergyConsumption EC
GROUP BY 
    EC.UserID, EC.DeviceID, FORMAT(EC.Timestamp, 'yyyy-MM-dd HH:00:00')
ORDER BY 
    TotalEnergy DESC;

-- Identify Peak Usage Periods
SELECT 
    EC.UserID, 
    FORMAT(EC.Timestamp, 'yyyy-MM-dd') AS Day, 
    MAX(EC.EnergyConsumed) AS PeakEnergy
FROM 
    EnergyConsumption EC
GROUP BY 
    EC.UserID, FORMAT(EC.Timestamp, 'yyyy-MM-dd')
ORDER BY 
    PeakEnergy DESC;

-- Calculate Average Energy Usage
SELECT 
    EC.UserID, 
    AVG(EC.EnergyConsumed) AS AverageEnergy
FROM 
    EnergyConsumption EC
GROUP BY 
    EC.UserID
ORDER BY 
    AverageEnergy DESC;

