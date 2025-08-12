```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_070.jpeg
document_name: grid
page_number: 070
page_id: grid#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:20:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the configuration process for a data connection in Windows Forms.
- Guides users through setting up a connection string for database access.
- Explains security considerations regarding sensitive data in the connection string.

## Content

### Data Connection Setup

#### Step 1: Choose Your Data Connection

- **Window Title**: Data Source Configuration Wizard
- **Prompt**: "Which data connection should your application use to connect to the database?"
- **Connection String**: ACCESS.C:\Documents and Settings\sridvidhar\My Documents\Syncfusion\Essen
- **Security Prompt**: "Do you want to include this sensitive data in the connection string?"
  - Option 1: "No, exclude sensitive data from the connection string. I will set this information in my application code."
  - Option 2: "Yes, include sensitive data in the connection string."
- **Figure**: Figure 34: Database Connection Window

#### Step 2: Pop-up Window

- **Action**: Click **No** to indicate that you do not want to save the MDB in the project.
- **Window Title**: Microsoft Visual Studio
- **Message**: "The connection you selected uses a local data file that is not in the current project. Would you like to copy the file to your project and modify the connection?"
- **Additional Information**: "If you copy the data file to your project, it will be copied to the project’s output directory each time you run the application. Press F1 for information on controlling this behavior."
- **Figure**: Figure 35: Pop-up Window displayed on clicking the Next Button

#### Step 3: Next Screen

- **Expected Outcome**: The following screen appears after selecting the options and confirming the connection.

## Page-level Navigation/TOC (if applicable)
- This section can be navigated within the guide, focusing on database connection configuration.

## Cross References
- Refer to related sections in the guide for additional details regarding database handling and security.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Essential Grid, Data Connection, Security, Version: 11.4.0.26] keywords: [database connection, sensitive data, connection string, visual studio, windows forms, data source, configuration wizard] -->
```