```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_747.jpeg
document_name: grid
page_number: 747
page_id: grid#page_747
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:37:32Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the creation of a summary column for the "Wins" column in a grouping grid using `GridSummaryColumnDescriptor`.
- Explains how to set up a SummaryColumn with properties like SummaryType and format.
- Covers defining a SummaryRow and adding the SummaryColumn to it.

## Content

### Through Code

This example shows a grouping grid bound with a Statistics table whose columns are ID, School, Sport, wins, losses, ties, and year. Follow the steps below to create a summary for the wins column that displays the sum of wins' values.

1. **Setup a SummaryColumn by instantiating GridSummaryColumnDescriptor specifying the SummaryType and format.**

   **[C#]**
   ```csharp
   GridSummaryColumnDescriptor scd = new GridSummaryColumnDescriptor();
   scd.Appearance.AnySummaryCell.Interior = new
       BrushInfo(Color.FromArgb(192, 255, 162));
   scd.DataMember = "wins";
   scd.Format = "{Sum}";
   scd.Name = "TotalWins";
   scd.SummaryType = SummaryType.Int32Aggregate;
   ```

   **[VB.NET]**
   ```vb.net
   Dim scd As GridSummaryColumnDescriptor = New
       GridSummaryColumnDescriptor()
   scd.Appearance.AnySummaryCell.Interior = New
       BrushInfo(Color.FromArgb(192, 255, 162))
   scd.DataMember = "wins"
   scd.Format = "{Sum}"
   scd.Name = "TotalWins"
   scd.SummaryType = SummaryType.Int32Aggregate
   ```

2. **Define a SummaryRow and add the SummaryColumn into it.**

   **[C#]**
   ```csharp
   GridSummaryRowDescriptor srd = new GridSummaryRowDescriptor();
   srd.SummaryColumns.Add(scd);
   srd.Appearance.AnySummaryCell.Interior = new
       BrushInfo(Color.FromArgb(255, 231, 162));
   ```

   **[VB.NET]**
   ```vb.net
   Dim srd As GridSummaryRowDescriptor = New GridSummaryRowDescriptor()
   ```

## Cross References
- See also: related topics on summaries in the Grid control documentation.

<!-- tags: [grid, summary, windows forms, coding example, property settings, syncfusion] keywords: [GridSummaryColumnDescriptor, SummaryType, GridSummaryRowDescriptor, DataMember, Format, Name, Interior, Aggregate, C#, VB.NET] -->
```