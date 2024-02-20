
CREATE PROCEDURE ugTables.GenerateUGTableAttributes (
    @TableName NVARCHAR(50),
    @ugTableId INT
)
AS
BEGIN
    DECLARE @SQL NVARCHAR(MAX);

	SELECT * INTO #ugColumns
	FROM ugTableColumns WHERE ugTableId = @ugTableId


    -- start the create table command
    SET @SQL = N'CREATE TABLE ugTables.' + QUOTENAME(@TableName) + ' (';

    -- append each column to the command
    DECLARE @ColumnName NVARCHAR(50), @DataType NVARCHAR(50);
    DECLARE ColumnCursor CURSOR FOR SELECT ColumnName, DataType FROM #ugColumns;
    OPEN ColumnCursor;
    FETCH NEXT FROM ColumnCursor INTO @ColumnName, @DataType;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @SQL = @SQL + QUOTENAME(@ColumnName) + ' ' + @DataType + ', ';
        FETCH NEXT FROM ColumnCursor INTO @ColumnName, @DataType;
    END

    CLOSE ColumnCursor;
    DEALLOCATE ColumnCursor;

    -- remove the last comma and space, and add the closing parenthesis
    SET @SQL = LEFT(@SQL, LEN(@SQL) - 1) + ')';

    -- execute the command
   EXEC sp_executesql @SQL;
END;
