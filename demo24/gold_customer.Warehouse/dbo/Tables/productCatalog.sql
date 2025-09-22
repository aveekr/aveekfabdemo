CREATE TABLE [dbo].[productCatalog] (

	[ProductID] bigint NULL, 
	[Name] varchar(8000) NULL, 
	[ProductType] varchar(8000) NULL, 
	[TickerSymbol] varchar(8000) NULL, 
	[Exchange] varchar(8000) NULL, 
	[ISIN] varchar(8000) NULL, 
	[Sector] varchar(8000) NULL, 
	[Industry] varchar(8000) NULL, 
	[RiskLevel] varchar(8000) NULL, 
	[Currency] varchar(8000) NULL, 
	[LastUpdated] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[productCatalog] ADD CONSTRAINT UQ_58abb196_bdbb_47b8_81ba_b448cf1ad73c unique NONCLUSTERED ([ProductID]);