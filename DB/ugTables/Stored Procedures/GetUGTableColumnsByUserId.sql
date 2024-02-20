CREATE PROCEDURE ugTables.GetUGTableColumnsByUserId(@userId INT)
AS SET NOCOUNT ON
BEGIN
	
	SELECT ugTableId, ColumnName, DataType FROM ugTableColumns
	WHERE ugTableId in (SELECT ugTableId FROM ugTables WHERE UserId = @userId)

END