USE [test]
GO

/****** Object:  Table [dbo].[A]    Script Date: 2021/2/8 15:40:21 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[A](
	[A_uid] [uniqueidentifier] NULL,
	[A_uid2] [uniqueidentifier] NULL,
	[A_field1] [nchar](10) NULL,
	[A_field2] [nchar](10) NULL,
	[A_field3] [nchar](10) NULL,
	[Time] [datetime] NULL
) ON [PRIMARY]
GO


CREATE TABLE [dbo].[B](
	[B_uid] [uniqueidentifier] NULL,
	[B_field1] [varchar](256) NULL,
	[B_field2] [varchar](256) NULL,
	[A_uid] [uniqueidentifier] NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[C](
	[C_field1] [varchar](256) NULL,
	[C_field2] [varchar](256) NULL,
	[A_uid] [uniqueidentifier] NULL,
	[A_uid2] [uniqueidentifier] NULL,
	[C_uid] [uniqueidentifier] NULL
) ON [PRIMARY]
GO