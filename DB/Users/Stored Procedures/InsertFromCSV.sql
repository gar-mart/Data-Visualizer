CREATE  PROCEDURE [Users].[InsertFromCSV](@userId INT, @categoryName VARCHAR(50), @tblName varchar(50), @csv varchar(100))

AS BEGIN
SET NOCOUNT ON

DECLARE @sql NVARCHAR(MAX);

	 DECLARE @generatedName VARCHAR(100) 


	 SELECT @generatedName = dbo.get_ugTable_by_category_and_name_id(@userId, @categoryName, @tblName)

	 SET @sql = N'BULK INSERT ' + @generatedName + ' FROM ''' + @csv + ''' 
    WITH (FIRSTROW = 2, FORMAT = ''CSV'',  FIELDTERMINATOR = '','', ROWTERMINATOR = ''0x0a'', TABLOCK);';
    EXEC sp_executesql @sql;

END