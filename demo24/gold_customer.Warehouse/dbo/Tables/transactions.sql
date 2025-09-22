CREATE TABLE [dbo].[transactions] (

	[TransactionID] varchar(8000) NULL, 
	[CustomerID] varchar(8000) NULL, 
	[TransactionDate] datetime2(6) NULL, 
	[ProductID] bigint NULL, 
	[TransactionType] varchar(8000) NULL, 
	[Quantity] bigint NULL, 
	[Price] float NULL, 
	[TotalAmount] float NULL, 
	[BrokerID] varchar(8000) NULL, 
	[Commission] float NULL, 
	[SettlementDate] datetime2(6) NULL, 
	[TransactionStatus] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[transactions] ADD CONSTRAINT FK_b5b86645_c381_45e0_bb6e_3f25b1492158 FOREIGN KEY ([ProductID]) REFERENCES [dbo].[productCatalog]([ProductID]);
GO
ALTER TABLE [dbo].[transactions] ADD CONSTRAINT FK_f6091976_f81f_4276_8aa6_58f4403bea28 FOREIGN KEY ([CustomerID]) REFERENCES [dbo].[customerprofile]([CustomerID]);