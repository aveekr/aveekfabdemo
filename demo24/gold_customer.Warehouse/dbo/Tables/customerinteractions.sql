CREATE TABLE [dbo].[customerinteractions] (

	[InteractionID] varchar(8000) NULL, 
	[CustomerID] varchar(8000) NULL, 
	[DateTime] datetime2(6) NULL, 
	[Channel] varchar(8000) NULL, 
	[AgentName] varchar(8000) NULL, 
	[InteractionSummary] varchar(8000) NULL, 
	[SentimentScore] float NULL
);


GO
ALTER TABLE [dbo].[customerinteractions] ADD CONSTRAINT UQ_6d34d73d_dfdd_456e_8033_a7170ed63e3d unique NONCLUSTERED ([CustomerID]);