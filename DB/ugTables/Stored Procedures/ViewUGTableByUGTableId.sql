CREATE PROCEDURE ugTables.ViewUGTableByUGTableId (@ugTableId INT, @rows INT)
AS SET NOCOUNT ON
BEGIN
	DECLARE @sql NVARCHAR(MAX)


	SET @sql = 'SELECT * FROM ' + dbo.get_ugTable_by_ugTableId(@ugTableId) + 
	
	' ORDER BY ROW_NUMBER() OVER (ORDER BY (SELECT 1))' +
	'OFFSET (' + CAST((@rows - 1) * 50 AS NVARCHAR(100)) + ') ROWS FETCH NEXT 50 ROWS ONLY'

	EXEC sp_executesql @SQL


END