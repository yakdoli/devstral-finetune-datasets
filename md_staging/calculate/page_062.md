```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: calculate
page_number: 062
page_id: calculate#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:02:35Z
fidelity: lossless
-->

# Essential Calculate

## Overview
- Provides a method to specify the row, column, and value for populating a single entry in an ArrayCalcData object.
- Focuses on handling input and updating the data grid programmatically.

## Content

This section explains how to use the provided code to populate a single entry in the ArrayCalcData object by specifying the row, column, and value.

### C#

By tapping the `button2_Click` event, users can input a row, column, and value to populate a corresponding cell in the data grid.

```csharp
/// <summary>
/// Populates a single entry in the ArrayCalcData object.
/// </summary>
/// <param name="sender"></param>
/// <param name="e"></param>
private void button2_Click(object sender, System.EventArgs e)
{
    if (this.nRows == 0)
    {
        MessageBox.Show("Generate data first.");
        return;
    }
    int row = int.Parse(textBox2.Text);
    int col = int.Parse(textBox3.Text);
    string val = this.textBox4.Text;
    this.data[row, col] = val;

    ShowObject();
}
```

### VB

The equivalent in VB handles the same functionality, allowing users to enter a row, column, and value to update the data grid dynamically.

```vb
' <summary>
' Populates a single entry in the ArrayCalcData object.
' </summary>
' <param name="sender"></param>
' <param name="e"></param>
Private Sub button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) _
        Handles Button2.Click
    If Me.nRows = 0 Then
        MessageBox.Show("Generate data first.")
        Return
    End If

    Dim row As Integer = Integer.Parse(Me.textBox2.Text)
    Dim col As Integer = Integer.Parse(Me.textBox3.Text)
    Dim val As String = Me.textBox4.Text

    Me.data(row, col) = val
```

## API Reference

| **Namespace** | `Syncfusion.WinForms` |
|---------------|--------------------------|
| **Class**     | `ArrayCalcData`        |

### Methods

- **Name:** `button2_Click`
  - **Description:** Populates a single entry in the ArrayCalcData object based on user input.
  - **Parameters:**
    - `sender`: The control that raised the event (typically `object`).
    - `e`: EventData containing additional information about the event (typically `System.EventArgs`).
  - **Returns:** `void`
  - **Exceptions:** None explicitly stated in the provided code.

- **Name:** `ShowObject`
  - **Description:** Displays or refreshes the updated data grid to reflect changes.

### Properties

- **data**: A two-dimensional array that stores the grid data.

## Code Examples

The provided code examples demonstrate how to integrate the `button2_Click` method into your application to enable users to update specific cells in the data grid programmatically.

### Important Notes
- Ensure the `nRows` is greater than zero before updating the grid to avoid null reference exceptions.
- Input validation should be implemented to handle invalid inputs such as non-numeric values in row and column fields.

## Page-level Navigation/TOC (if applicable)

- [Overview]
- [Content]
- [API Reference]
- [Code Examples]

## Cross References

For more details on working with grid data and handling user inputs, refer to the Syncfusion documentation for Syncfusion WinForms.

<!-- tags: [syncfusion, winforms, arraycalcdata, grid, data, programming] keywords: [syncfusion, winforms, calculate, cell, update, data grid, programmatic update, grid data, arraycalcdata] -->
```