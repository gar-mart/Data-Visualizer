CREATE PROCEDURE [Users].[GetMyAssets](@userId INT)
AS SET NOCOUNT ON
BEGIN
	SELECT CategoryName, UserAssignedName, ugTableId
	FROM ugTables
	WHERE UserId = @userId
END