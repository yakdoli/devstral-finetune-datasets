```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_989.jpeg
document_name: grid
page_number: 989
page_id: grid#page_989
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:53:09Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the integration of a "Print" dialog box in the Grid control.
- Displays how the Grid control can be customized to include printing functionalities.
- Provides an example of setting up the printer properties and selecting print ranges for Grid data.

## Content

### Print Dialog Box on Grid

#### Overview
The screenshot depicts a Grid control with a nested structure that allows for printing. The Grid contains categories and products, and a "Print" dialog box is visible, indicating the configuration options available for printing.

#### Features Highlighted
- **Grid Control:**
  - **Categories**: Each category is expandable/collapsible to show associated product items.
  - **Products**: Each product is listed under its respective category, allowing for detailed data retrieval.
  - **Printing Options**: The Grid allows users to configure printing parameters, such as printer selection, print range, and copies.

#### Print Dialog Details
- **Printer Configuration**:
  - **Name**: "\syncchnst1\SyncChnPrinter"
  - **Status**: Ready
  - **Type**: Samsung SCX-4100 Series
  - **Where**: USB001
  - **Comment**: None
  - **Print to file**: Option is unchecked.

- **Print Range**:
  - **All**: Selected to print all content in the Grid.
  - **Pages**: Range selection is inactive as "All" is chosen.
  - **Selection**: Option is not active as "All" is selected.

- **Copies**:
  - **Number of copies**: Set to 1.
  - **Collate**: Option is unchecked.

- **Print Options**:
  - Two buttons are visible:
    - **OK**: To confirm the print settings.
    - **Cancel**: To discard changes and exit the dialog.

#### Example Grid Structure
- **Categories**:
  - **Beverages - 1**: Includes products like Chai, Chang, Guarana, etc.
  - **Condiments - 1**:
  - **Confections - 1**:

#### Interaction
The Grid demonstrates how data can be hierarchically organized and presented, with the ability to print specific sections or the entire dataset using the print dialog.

### Figure: Grid with Print Dialog Box

#### Caption: Figure 383: Grid with Print Dialog Box
This figure illustrates the integration of the Grid control with a print dialog box. It shows the ability to configure printer settings and select data ranges for printing.

## API Reference
### Namespaces and Classes
While specific API references are not detailed in the image, the functionality demonstrated involves the following areas:
- **Syncfusion.Windows.Forms.Grid**: The main Grid control.
- **Syncfusion.Windows.Forms.Grid.Printing**: Modules responsible for printing functionalities.

## Code Examples
The image does not provide explicit code examples, but a typical implementation of integrating a print dialog in the Grid might involve:
```csharp
// Example:
using Syncfusion.Windows.Forms.Grid;
using Syncfusion.Windows.Forms.Grid.Printing;

GridControl grid = new GridControl();
GridPrintDocument printDoc = new GridPrintDocument(grid.Model);

// Configure print settings
// More code for setting up print properties and ranges
```

## Page-level Navigation/TOC
- **Grid Control Overview**
- **Print Dialog Integration**
- **Printing Configuration**
- **Example Grid Usage**

## Cross References
- Refer to theGrid documentation for full Grid functionalities.
- See the Printing module documentation for advanced options.

<!-- tags: [grid, print dialog, windows forms, syncfusion] keywords: [grid control, print configuration, printer settings, windows forms integration, data printing, categories, products] -->
```