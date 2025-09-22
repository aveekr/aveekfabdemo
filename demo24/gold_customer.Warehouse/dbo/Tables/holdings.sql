CREATE TABLE [dbo].[holdings] (

	[portfolio_id] varchar(8000) NULL, 
	[asset_name] varchar(8000) NULL, 
	[quantity] float NULL, 
	[purchase_date] datetime2(6) NULL, 
	[purchase_price] float NULL, 
	[current_value] float NULL, 
	[profit_loss] float NULL, 
	[sector] varchar(8000) NULL, 
	[industry] varchar(8000) NULL, 
	[market_cap] varchar(8000) NULL, 
	[customerid] varchar(8000) NULL, 
	[productId] varchar(8000) NULL, 
	[Name] varchar(8000) NULL, 
	[ProductType] varchar(8000) NULL, 
	[TickerSymbol] varchar(8000) NULL, 
	[Sector.1] varchar(8000) NULL, 
	[Industry.1] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[holdings] ADD CONSTRAINT FK_b332a691_8392_4100_9adf_ac862704875f FOREIGN KEY ([customerid]) REFERENCES [dbo].[customerprofile]([CustomerID]);