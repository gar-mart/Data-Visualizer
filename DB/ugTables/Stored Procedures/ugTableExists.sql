
CREATE PROCEDURE ugTables.ugTableExists(
@userId CHAR(32),
@categoryName VARCHAR(50),
@uAssignedName VARCHAR(50),
@TableExists BIT OUTPUT
)
AS 
SET NOCOUNT ON
BEGIN
	SELECT @TableExists = CASE 
        WHEN EXISTS (
            SELECT * 
            FROM ugTables
            WHERE UserAssignedName = @uAssignedName
			AND UserId = @userId
			AND (CategoryName = @categoryName OR (@categoryName IS NULL AND CategoryName IS NULL))
		)
        THEN 1 
        ELSE 0
	END
END
