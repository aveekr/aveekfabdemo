CREATE   PROCEDURE dbo.UpdateCustomerTotalAssets
    @CustomerID INT = NULL
AS
BEGIN
   
    BEGIN TRY
        ;WITH Totals AS (
            SELECT
                ca.customerid,
                SUM(ca.current_value) AS TotalAssets
            FROM dbo.holdings AS ca
            GROUP BY ca.customerid
        )
        UPDATE cp
        SET cp.TotalAssets = ISNULL(t.TotalAssets, 0)
        FROM dbo.customerprofile AS cp
        LEFT JOIN Totals AS t
            ON t.customerid = cp.CustomerID
        WHERE (@CustomerID IS NULL OR cp.CustomerID = @CustomerID);
    END TRY
    BEGIN CATCH
        -- Rethrow original error; keeps error number/severity/state intact
        THROW;
    END CATCH
END;