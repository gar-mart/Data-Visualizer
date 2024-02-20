CREATE PROCEDURE ugTables.GetUGTablesTotalCountById(@ugTableId INT)
AS SET NOCOUNT ON 
BEGIN 
	DECLARE @sql NVARCHAR(MAX) 
	= 'SELECT COUNT(*) FROM ' + ugTables.GetUGTableById(@ugTableId)

	EXEC sp_executesql @SQL;

END