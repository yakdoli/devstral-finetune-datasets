```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_708.jpeg
document_name: tools
page_number: 708
page_id: tools#page_708
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

This page introduces the **CurrencyEdit Control**, a specialized control for displaying and editing currency values. It includes features such as a calculator button to display a dropdown calculator, as well as detailed information on how to create and configure the control.

### CurrencyEdit Control

**Figure 439: CurrencyEdit Control**

---

### 3.5.8.1.1 Features

The features of CurrencyEdit control are listed below.

- **CurrentUI culture** can be applied to CurrencyEdit control through properties of embedded textbox.
- You can set **Button Styles** for CurrencyEdit control.
- The **Currency value** can be moved from a **PopupCalculator** to a **CurrencyTextbox** and vice versa.
- The **layout of the calculator control** in the CurrencyEdit control can also be changed.
- It is used to display **dropdown Financial Calculator**.

---

### 3.5.8.1.2 Creating CurrencyEdit

To use a CurrencyEdit control in your application, all you need to do is drag and drop the CurrencyEdit control from the controls toolbox onto your form. You can then set any of its properties through the **property grid**.

---

## API Reference

- **Namespace**: Syncfusion.Windows.Forms
- **Class**: CurrencyEdit
- **Properties**:
  - **CurrentUI culture**: Applied via embedded textbox properties.
  - **Button Styles**: Customizable.
  - **Layout**: Configurable for the calculator control.
- **Methods**: See class reference for full details.

---

### Code Examples

#### C#

```csharp
// Drag and drop CurrencyEdit from toolbox to form
CurrencyEdit currencyEdit = new CurrencyEdit();
currencyEdit.Dock = DockStyle.Fill;

// Set properties through property grid
currencyEdit.Culture = CultureInfo.GetCultureInfo("en-US");
currencyEdit.ButtonStyle = ButtonStyle.Calc;
```

#### VB.NET

```vb
' Drag and drop CurrencyEdit from toolbox to form
Dim currencyEdit As New CurrencyEdit()
currencyEdit.Dock = DockStyle.Fill

' Set properties through property grid
currencyEdit.Culture = CultureInfo.GetCultureInfo("en-US")
currencyEdit.ButtonStyle = ButtonStyle.Calc
```

---

## Cross References

See also:
- [CurrencyEdit Control in Documentation]
- [Tools Examples and Samples]

---

<!-- tags: [tools, windows forms, controls, currencyedit, calculator, dropdown] -->
```