```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_056.jpeg
document_name: chart
page_number: 056
page_id: chart#page_056
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:16Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes the process of configuring a chart data source using the Syncfusion "Chart & Data Wizard."
- Demonstrates selecting a new `BindingSource` in the Data Source tab.
- Guides through the Data Source Configuration Wizard settings for database integration.

## Content

### Chart Wizard Interface

#### Window Layout
The "Chart Wizard" interface from Syncfusion is displayed, featuring the following elements:

- **Tabs**:
  - Auto Run Wizard
  - Series Data
  - Data Source
  - Series Data Tab
- **Left Panel**:
  - Options for configuring different aspects of the chart:
    - Chart type
    - Series
    - Appearance
    - Axes
    - Points
    - ToolBar
    - Legend
- **Data Source Tab**:
  - Drop-down list for selecting existing or new data sources.
  - Option to create a new `BindingSource`.

#### Process Steps
1. **Selecting a new `BindingSource`**:
   - Open the drop-down list in the Data Source tab.
   - Click on "new BindingSource...." from the list.
   - This action opens the Data Source Configuration Wizard.

2. **Configuring the Data Source**:
   - In the Data Source Configuration Wizard, choose the Data source Type as **Database**.
   - Click **Next** to proceed.

#### Figure 29: Selecting "new BindingSource...."
- The screenshot depicts the step where "new BindingSource...." is selected from the drop-down list in the Data Source tab. This action initiates the Data Source Configuration Wizard.

### Data Source Configuration Wizard

#### Initial Wizard Prompt
- After selecting "new BindingSource...." in the Data Source tab, the Data Source Configuration Wizard will appear.
- **Step 1**: Choose the Data source Type as **Database**.
- **Step 2**: Click **Next** to continue the configuration process.

## API Reference

### Key Actions
- Selection of a new `BindingSource` from the Data Source tab.
- Configuration of the Data Source Type in the Wizard as **Database**.

## Cross References
- Refer to the Data Source Configuration Wizard documentation for additional steps and parameters.

<!-- tags: [syncfusion, winforms, chart wizard, data source binding, database integration] keywords: [chart wizard, new BindingSource, data source, database, configuration wizard] -->
```