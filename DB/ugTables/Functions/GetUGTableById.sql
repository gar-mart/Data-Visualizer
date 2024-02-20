CREATE FUNCTION ugTables.GetUGTableById (@ugTableId INT)

RETURNS NVARCHAR(100)
AS
BEGIN
    DECLARE @result NVARCHAR(100)
    SELECT @result = 'ugTables.' + GeneratedName FROM ugTables WHERE ugTableId = @ugTableId;
    RETURN @result;
END