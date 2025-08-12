```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: PivotGrid
page_number: 016
page_id: PivotGrid#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:53:18Z
fidelity: lossless
-->

# Essential PivotGrid WindowsForms

## Overview
- Provides an overview of the class diagram for the `PivotGrid` control.
- Explains the relationship between `PivotGrid Control`, its base class, and its components.

## Content

### 3.3 Class Diagram

The class diagram for the `PivotGrid WF` control is shown below:

```plaintext
+---------------------------+
| PivotGrid Control        |
+---------------------------+
         ↑
+---------------------------+
| PivotGridControlBase     |
+---------------------------+
         ↑
+------------------------+   +--------------------+
| Pivot Rows           |   | Pivot Columns      |
+------------------------+   +--------------------+
                           ↓                         ↓
+---------------------------+   +--------------------+
| Pivot Calculation Values |   | Filters           |
+---------------------------+   +--------------------+
```

#### Explanation:
- **`PivotGrid Control`**: The main control that implements the `IPivotControl` interface.
- **`IPivotControl`**: The interface that defines the behavior and methods of the pivot grid.
- **`PivotGridControlBase`**: The base class for the pivot grid control, which contains shared functionality.
- **`Pivot Rows`**: Represents the rows in the pivot grid.
- **`Pivot Columns`**: Represents the columns in the pivot grid.
- **`Pivot Calculation Values`**: Defines the calculation values for the pivot grid.
- **`Filters`**: Handles filtering functionality in the pivot grid.

### Figure 7: PivotGrid WF Class Diagram

The diagram illustrates the structure and hierarchy of the `PivotGrid` control, showing how it is composed of various components and interfaces.

## API Reference (if applicable)
- This section details the classes, methods, properties, and events related to the `PivotGrid` control.
- For example:
  - `IPivotControl`: Interface defining the control's behavior.
  - `PivotGridControlBase`: Base class for the pivot grid control.
  - `Pivot Rows`, `Pivot Columns`, `Pivot Calculation Values`, `Filters`: Components of the pivot grid.

## Code Examples
Example code demonstrating how to use the `PivotGrid` control in a Windows Forms application:
```csharp
using Syncfusion.Windows.Forms.PivotGrid;

public class PivotGridExample
{
    private PivotGridControl pivotGrid;

    public void InitializePivotGrid()
    {
        // Create an instance of PivotGridControl
        pivotGrid = new PivotGridControl();

        // Add rows, columns, and calculation values
        pivotGrid.PivotRows.Add(new PivotRowField("Category"));
        pivotGrid.PivotColumns.Add(new PivotColumnField("Product"));
        pivotGrid.PivotCalculationValues.Add(new PivotValueField("Sales", "Total Sales", CalculationMode.Sum));

        // Apply a filter
        pivotGrid.PivotFilters.Add(new PivotFilterField("Region", "North"));
    }
}
```

## Cross References
- See also:
  - [PivotGrid Control Documentation](#pivotgrid-control-documentation)
  - [Working with PivotGrid in Windows Forms](#working-with-pivotgrid-in-windows-forms)

<!-- tags: PivotGrid, WindowsForms, Class Diagram, IPivotControl, PivotGridControlBase keywords: PivotRows, PivotColumns, PivotCalculationValues, Filters, Windows Forms, class diagram, control interface -->
```