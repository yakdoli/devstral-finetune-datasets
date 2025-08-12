```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_420.jpeg
document_name: grid
page_number: 420
page_id: grid#page_420
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
' Cover odd rows, columns 1 through 3.
If (((e.RowIndex Mod 2) = 1) AndAlso (e.ColIndex >= 1)) _
    AndAlso (e.ColIndex <= 3)) Then
    e.Range = GridRangeInfo.Cells(e.RowIndex, 1, e.RowIndex, 3)
    e.Handled = True
End If

' Cover column 6 with odd-even row pairs.
If ((e.RowIndex > 0) AndAlso (e.ColIndex = 6)) Then
    Dim row As Integer
    row = ((((e.RowIndex - 1) / 2) * 2) + 1)
    Dim col As Integer
    col = e.ColIndex
    e.Range = GridRangeInfo.Cells(row, col, (row + 1), col)
    e.Handled = True
End If
End Sub
```

## 4.1.4.12 Pivot Grid

### Overview
- Simulates the Pivot Table feature of MS Excel.
- Organizes data via drag-and-drop operations in a cross-tabulated form.
- Major advantage: ability to extract desired information quickly.
- Used to summarize and group data in the financial domain.

### Components
- **Display Grid**: Displays data extracted from the underlying database.
- **Pivot Table Field List**: Lists available fields, allowing addition or removal.
- **Drag-Drop Panel**: View area for rearranging fields via drag-and-drop.
- **Filter Area**: Filters results based on specific criteria.

### Features
- Supports **Office 2003** and **Office 2007** styles.
- Visual aspects are saved in an Appearance object.
- Allows defining rows and columns through drag-and-drop operations.

## Page-level Navigation/TOC (if applicable)
- No local Table of Contents present.

## Cross References
- None explicitly mentioned.

<!-- tags: [grid, pivot-grid, essential-grid, windows-forms, drag-and-drop, data-organization, financial-domain, appearance-object, office-styles] keywords: [pivot table, drag-and-drop operations, cross-tabulation, financial data, filter area, visual aspects, appearance object, office 2003, office 2007] -->
```