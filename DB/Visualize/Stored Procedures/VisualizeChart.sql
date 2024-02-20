CREATE PROCEDURE  [Visualize].[VisualizeChart] (
@YAxis VARCHAR(100),
@XAxis VARCHAR(MAX),
@TableName VARCHAR(100),
@userId INT
)
AS SET NOCOUNT ON
BEGIN




DECLARE @sql NVARCHAR(MAX) = 
'SELECT SUM(' + @YAxis +') AS YAxis, ' + @XAxis +' AS XAxis ' +

'FROM ' + dbo.get_ugTable_by_category_name_id(@userId, @TableName)  

+ ' GROUP BY ' + @XAxis


;EXEC SP_EXECUTESQL @sql

END
