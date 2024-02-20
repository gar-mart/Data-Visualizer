

CREATE PROCEDURE ugTables.CreateUGTable ( 

	@userAssignedName VARCHAR(100),
	@cetegoryName VARCHAR(100) NULL,
	@userId INT, 
	@tvpColumns tvpColumns READONLY
)
AS BEGIN 
SET NOCOUNT ON

	DECLARE @generatedName VARCHAR(100)
	
	
	INSERT INTO ugTables (userid, UserAssignedName, CategoryName)
	VALUES (@userId, @userAssignedName, @cetegoryName)
	

	DECLARE @SCOPE_IDENTITY INT = SCOPE_IDENTITY()
	SET @generatedName = 'ugt_' + CAST(@userId AS VARCHAR(10)) + '_' + CAST(@SCOPE_IDENTITY AS VARCHAR(10))
	
	
	INSERT INTO ugTableColumns (ugTableId, ColumnName, DataType, KeyType)
	SELECT @SCOPE_IDENTITY, ColumnName, DataType, NULL FROM @tvpColumns
	
	
	--Create the actual table after genrating

	;EXEC ugTables.GenerateUGTableAttributes @generatedName, @SCOPE_IDENTITY
	
	UPDATE ugTables SET ObjectId = OBJECT_ID('ugTables.' + @generatedName), GeneratedName = @generatedName
	WHERE ugTableId = @SCOPE_IDENTITY


END	
