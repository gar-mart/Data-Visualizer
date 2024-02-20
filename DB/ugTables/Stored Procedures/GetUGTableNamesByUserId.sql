CREATE PROCEDURE ugTables.GetUGTableNamesByUserId(@userId INT)
AS SET NOCOUNT ON
BEGIN
	SELECT ISNULL(CategoryName + '.','') + UserAssignedName ug_tableName, ugTableId
	FROM ugTables WHERE UserId = @userId
	ORDER BY CategoryName, UserAssignedName
END