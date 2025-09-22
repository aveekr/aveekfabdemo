CREATE TABLE [dbo].[customerprofile] (

	[CustomerID] varchar(8000) NULL, 
	[Name] varchar(8000) NULL, 
	[Age] bigint NULL, 
	[Gender] varchar(8000) NULL, 
	[MaritalStatus] varchar(8000) NULL, 
	[Address] varchar(8000) NULL, 
	[AnnualIncome] float NULL, 
	[Occupation] varchar(8000) NULL, 
	[RiskScore] varchar(8000) NULL, 
	[InvestmentExperience] varchar(8000) NULL, 
	[InvestmentObjective] varchar(8000) NULL, 
	[PreferredInvestmentType] varchar(8000) NULL, 
	[TotalAssets] float NULL, 
	[TotalLiabilities] float NULL, 
	[AccountTenureYears] bigint NULL, 
	[NumberOfDependents] bigint NULL, 
	[EducationLevel] varchar(8000) NULL, 
	[EmploymentStatus] varchar(8000) NULL, 
	[CreditScore] bigint NULL, 
	[Email] varchar(8000) NULL, 
	[PhoneNumber] varchar(8000) NULL, 
	[LastUpdated] datetime2(6) NULL, 
	[City] varchar(8000) NULL, 
	[State] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[customerprofile] ADD CONSTRAINT UQ_24836eaa_0fa2_42b6_a969_f804772b0d33 unique NONCLUSTERED ([CustomerID]);
GO
ALTER TABLE [dbo].[customerprofile] ADD CONSTRAINT FK_dd9d4f38_dbb5_421a_af76_d67b83fe869d FOREIGN KEY ([CustomerID]) REFERENCES [dbo].[customerinteractions]([CustomerID]);