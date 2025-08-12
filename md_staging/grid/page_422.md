```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_422.jpeg
document_name: grid
page_number: 422
page_id: grid#page_422
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page details methods and properties related to the appearance and functionality of the Pivot Grid in Windows Forms.

## Content

### Appearance Methods
- **SetAppearance()** - This method sets the appearance of the Pivot Grid.

```csharp
[C#]

pivotGridControl1.SetAppearance(new
PivotGridLibrary.PivotAppearance(pivotGridControl2));
```

### Important Properties

- **AllString** - This property gets the string values that appear in the dropdown filter when all filter values are selected.

```csharp
[C#]

pivotGridControl1.AllString = "All";
```

- **AutoSizeColumns** - This property sizes the column according to the calculated display width.

```csharp
[C#]

pivotGridControl1.AutoSizeColumns = true;
```

- **ColumnCount** - Specifies the number of columns in the main display grid.

```csharp
[C#]

int i = pivotGridControl1.ColumnCount;
```

- **ColumnsCount** - Specifies the number of distinct fields in the pivot grid.

```csharp
[C#]

int i = pivotGridControl1.ColumnsCount;
```

- **DataRowCount** - Specifies the number of rows in the underlying IList datasource.

```csharp
[C#]

int i = pivotGridControl1.DataRowCount;
```

- **DefaultComputationName** - Specifies the name of the default calculation. The default value is `Sum`.

---

## API Reference
- **Namespace**: `PivotGridLibrary`
- **Class**: `PivotGridControl`
- **Properties**
  - `AllString`: string
  - `AutoSizeColumns`: bool
  - `ColumnCount`: int
  - `ColumnsCount`: int
  - `DataRowCount`: int
  - `DefaultComputationName`: string

## Code Examples

### C# Examples
- Set the appearance of the Pivot Grid:

```csharp
pivotGridControl1.SetAppearance(new PivotGridLibrary.PivotAppearance(pivotGridControl2));
```

- Set the string value for the dropdown filter when all values are selected:

```csharp
pivotGridControl1.AllString = "All";
```

- Automatically size the columns:

```csharp
pivotGridControl1.AutoSizeColumns = true;
```

- Retrieve the column count:

```csharp
int i = pivotGridControl1.ColumnCount;
```

- Retrieve the number of distinct fields:

```csharp
int i = pivotGridControl1.ColumnsCount;
```

- Retrieve the number of rows in the datasource:

```csharp
int i = pivotGridControl1.DataRowCount;
```

- Set the default computation name:

```csharp
pivotGridControl1.DefaultComputationName = "Sum";
```

---

<!-- tags: [Pivot Grid, Windows Forms, Appearances, Column Dimensions, Column Count, Field Count, Data Rows, Computation Name] keywords: [SetAppearance, AllString, AutoSizeColumns, ColumnCount, ColumnsCount, DataRowCount, DefaultComputationName, Pivot Grid, Windows Forms] -->
```