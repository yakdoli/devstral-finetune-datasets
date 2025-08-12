```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: grid
page_number: 005
page_id: grid#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:15:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Covers various cell types and features in Essential Grid for Windows Forms, including OLE objects, specialized controls, and MS Excel-like functionalities.
- Focuses on advanced features such as embedding different objects, handling dates and times, and supporting formulas and calculations.

## Content

### Section 4.1.4.4.2 Embedding OLE Objects in the Grid Cell
- Page: 208

### Section 4.1.4.4.3 Calculator Text Box
- Page: 209

### Section 4.1.4.4.4 Calendar
- Page: 211

### Section 4.1.4.4.5 Date Time Picker
- Page: 212

### Section 4.1.4.4.6 Enhanced Numeric Up Down
- Page: 213

### Section 4.1.4.4.7 GridInCell
- Page: 215

### Section 4.1.4.4.8 Link Label Cell
- Page: 216

### Section 4.1.4.4.9 Picture Box
- Page: 217

### Section 4.1.4.4.10 Slider
- Page: 218

### Section 4.1.4.4.11 XHTML Cell
- Page: 220

### Section 4.1.4.4.12 Chart Cell
- Page: 222

### Section 4.1.4.4.13 Drop-Down Grid Cell
- Page: 223

### Section 4.1.4.4.14 Drop-Down Form and User Control Cell
- Page: 225

### Section 4.1.4.4.15 Integer Text Box
- Page: 226

### Section 4.1.4.4.16 Double Text Box
- Page: 227

### Section 4.1.4.4.17 Percent Text Box
- Page: 228

### Section 4.1.4.5 MS Excel-like Features
- Page: 230

#### Section 4.1.4.5.1 Selection Frame
- Page: 230

#### Section 4.1.4.5.2 Current Cell
- Page: 231

#### Section 4.1.4.5.3 Workbook
- Page: 232

#### Section 4.1.4.5.4 Splitter
- Page: 233

#### Section 4.1.4.5.5 Freeze Pane
- Page: 235

#### Section 4.1.4.5.6 MultiLevel Undo and Redo
- Page: 236

#### Section 4.1.4.5.7 Find Replace
- Page: 238

#### Section 4.1.4.5.8 Unhide Column by Double-Clicking Disabled
- Page: 240

#### Section 4.1.4.5.9 Highlighting Row and Column Headers
- Page: 241

### Section 4.1.4.6 Formula Support
- Page: 243

#### Section 4.1.4.6.1 Defining a FormulaCell
- Page: 243

#### Section 4.1.4.6.2 Using the Formula Library
- Page: 244

#### Section 4.1.4.6.3 Supported Arithmetic Operators and Calculation Precedence
- Page: 244

#### Section 4.1.4.6.4 Inside Essential Grid's Formula Support
- Page: 245

#### Section 4.1.4.6.5 Adding Formulas to the Formula Library
- Page: 245

#### Section 4.1.4.6.6 Function Reference Section
- Page: 249

#### Section 4.1.4.6.7 Cross Sheet Reference
- Page: 378

## Code Examples (multi-language supported)

### Sample Code: Embedding OLE Objects in the Grid Cell
```csharp
// Example usage in C#
Syncfusion.Windows.Forms.Grid.GridControl grid = new Syncfusion.Windows.Forms.Grid.GridControl();
// Configure the grid to allow embedding OLE objects
grid.EmbeddedControlCellFactory = new MyOLECellFactory();
// Add logic to handle OLE objects in grid cells
```

## Page-level Navigation/TOC (if applicable)
- **Section 4.1.4.4.2** Embedding OLE Objects in the Grid Cell
- **Section 4.1.4.4.3** Calculator Text Box
- **Section 4.1.4.4.4** Calendar
- **Section 4.1.4.4.5** Date Time Picker
- **Section 4.1.4.4.6** Enhanced Numeric Up Down
- **Section 4.1.4.4.7** GridInCell
- **Section 4.1.4.4.8** Link Label Cell
- **Section 4.1.4.4.9** Picture Box
- **Section 4.1.4.4.10** Slider
- **Section 4.1.4.4.11** XHTML Cell
- **Section 4.1.4.4.12** Chart Cell
- **Section 4.1.4.4.13** Drop-Down Grid Cell
- **Section 4.1.4.4.14** Drop-Down Form and User Control Cell
- **Section 4.1.4.4.15** Integer Text Box
- **Section 4.1.4.4.16** Double Text Box
- **Section 4.1.4.4.17** Percent Text Box
- **Section 4.1.4.5** MS Excel-like Features
  - **Section 4.1.4.5.1** Selection Frame
  - **Section 4.1.4.5.2** Current Cell
  - **Section 4.1.4.5.3** Workbook
  - **Section 4.1.4.5.4** Splitter
  - **Section 4.1.4.5.5** Freeze Pane
  - **Section 4.1.4.5.6** MultiLevel Undo and Redo
  - **Section 4.1.4.5.7** Find Replace
  - **Section 4.1.4.5.8** Unhide Column by Double-Clicking Disabled
  - **Section 4.1.4.5.9** Highlighting Row and Column Headers
- **Section 4.1.4.6** Formula Support
  - **Section 4.1.4.6.1** Defining a FormulaCell
  - **Section 4.1.4.6.2** Using the Formula Library
  - **Section 4.1.4.6.3** Supported Arithmetic Operators and Calculation Precedence
  - **Section 4.1.4.6.4** Inside Essential Grid's Formula Support
  - **Section 4.1.4.6.5** Adding Formulas to the Formula Library
  - **Section 4.1.4.6.6** Function Reference Section
  - **Section 4.1.4.6.7** Cross Sheet Reference

## RAG Annotations
<!-- tags: [syncfusion, winforms, grid, essentialgrid, celltypes, formulas, excel, oleobjects, datetimes, numericUpdown, splitpanes] keywords: [OLEObjects, CalculatorTextBox, DateTimePicker, FormulaSupport, FrozenPanes, NumberFormatting, Grid, UserGuide, Syncfusion, Version11.4.0.26] -->
```
