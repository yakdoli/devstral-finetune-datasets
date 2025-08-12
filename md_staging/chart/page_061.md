```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: chart
page_number: 061
page_id: chart#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Configurations for selecting database objects and setting up a dataset are shown using the Data Source Configuration Wizard in Syncfusion Winforms.
- Provides steps to integrate database tables and columns into a chart, facilitating dashboard-like functionality.
- Explains the process of selecting required tables and columns, defining dataset names, and integrating the selected database into the Chart Wizard.

## Content

### Data Source Configuration Wizard

#### Step-by-Step Guide
The following steps detail how to configure the Data Source in the Chart Wizard for integrating database objects into a Windows Forms application.

1. **Selecting Database Objects**
   - **Objective**: Choose the necessary database objects to include in the dataset.
   - **Process**: Use the "Choose Your Database Objects" dialog box to select tables, columns, and any other required database items.
   - **Example**:  
     The screenshot shows the selection of a `Demographics` table with columns `ID`, `City`, and `Population`.  
     **DataSet Name**: `ChartDataDataSet1`

2. **Confirming Selection**
   - **Action**: Click the "Finish" button after selecting the required table and columns.
   - **Outcome**: The configuration is completed, and control is returned to the Chart Wizard.

#### Returning to the Chart Wizard
- Upon clicking "Finish," you will be directed back to the Chart Wizard.
- **Next Step**: Select the database from the **Data Source** list as shown in the following images.

**Note**: The provided screenshot reflects the confirmation step of the Data Source Configuration Wizard.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Charts
- **Methods/Properties:**
  - `DataSourceConfigurationWizard`
  - `DataSetName`
  - `Tables`
  - `Columns`

## Code Examples
```csharp
// Example of setting up a dataset in C#
using System;
using System.Data;
using Syncfusion.WinForms.Charts;

public class ChartSetup
{
    public void ConfigureDataSource()
    {
        // Define the dataset name
        string datasetName = "ChartDataDataSet1";

        // Example of selecting tables and columns
        // Here, 'Demographics' table with 'ID', 'City', and 'Population' columns is selected
        // Integration into Chart Wizard
    }
}
```

## Page-level Navigation/TOC (if applicable)
- [1] "Data Source Configuration Wizard"
- [2] "Returning to the Chart Wizard"

## Cross References
See also:
- **Chart Wizard**
- **WinForms Chart Integration**
- **Database Integration in Syncfusion**

## RAG Annotations
<!-- tags: [syncfusion, winforms, chart, dataset, data source, wizard, essential chart, windows forms] keywords: [demographics, population, city, id, dataset name, data source configuration, chart wizard, integration, tutorial] -->
```