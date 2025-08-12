```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_710.jpeg
document_name: tools
page_number: 710
page_id: tools#page_710
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the creation and use of the `CurrencyEdit` control in Windows Forms.
- Explains the features and functionalities of the `CurrencyEdit` control.

## Content

### Creating a CurrencyEdit Control Programmatically

```csharp
Private currencyEdit1 As Syncfusion.Windows.Forms.Tools.CurrencyEdit
Me.currencyEdit1 = New Syncfusion.Windows.Forms.Tools.CurrencyEdit()
Me.Controls.Add(Me.currencyEdit1)
```

![Figure 441: CurrencyEdit Control Created Programmatically](https://i.imgur.com/example.png)

#### **Figure 441: CurrencyEdit Control Created Programmatically**

### 3.5.8.1.3 Concepts and Features

The following topics will help you become more familiar in using the `CurrencyEdit` control.

#### 3.5.8.1.3.1 Calculator Settings

A `CurrencyEdit` control has a text field and a Calculator button, pressing which will open a Calculator control. The below image illustrates the same.

![Calculator Button and Popup](https://i.imgur.com/example.png)

- **CurrencyEdit**: The text field where the currency value is displayed and edited.
- **Calculator Button**: The button that opens the Calculator control when clicked.
- **Calculator Popup**: The Calculator interface that appears when the Calculator button is pressed.

## API Reference

### Namespace: `Syncfusion.Windows.Forms.Tools`

#### Class: `CurrencyEdit`

- **Properties**
  - `CustomFormat`: Format string for the currency display.
  - `DecimalPlaces`: Number of decimal places to display.
  - `NegativeNumberStyle`: Style for displaying negative numbers.

- **Methods**
  - `ShowCalculator()`: Opens the calculator for input.
  - `UpdateTotal()`: Updates the total value based on the calculation.

### Usage
The `CurrencyEdit` control integrates seamlessly with Windows Forms, providing a user-friendly interface for monetary calculations.

## Code Examples

- **C# Example**
  ```csharp
  currencyEdit1.CustomFormat = "$###,##0.00";
  currencyEdit1.DecimalPlaces = 2;
  ```

- **VB.NET Example**
  ```vb
  currencyEdit1.CustomFormat = "$###,##0.00"
  currencyEdit1.DecimalPlaces = 2
  ```

## Cross References
See also:
- `NumericUpDown` control
- `CurrencyTextBox` control

<!-- tags: [windows-forms, currencyedit, calculator, control] keywords: [currency, edit, calculator, control, windows, forms] -->
```