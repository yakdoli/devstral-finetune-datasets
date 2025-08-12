```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_402.jpeg
document_name: tools
page_number: 402
page_id: tools#page_402
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:31Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Demonstrates how to apply custom colors to a Windows Forms control using the `Syncfusion.Windows.Forms` library.
- Focuses on using the `Office2007Theme` and `Office2007Colors` functionalities to customize the appearance of a Calculator control.
- Describes the usage of the `PopupCalculator` control to embed a Calculator object into a button's context.

### Content

#### Applying Custom Colors to Calculator Control

The `Office2007Theme` and `Office2007Colors` classes from the `Syncfusion.Windows.Forms` library allow you to customize the appearance of controls. In the following example, a custom theme is applied to the `calculatorControl1` control, setting its color to "Navy":

```csharp
Me.calculatorControl1.Office2007Theme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(Me, Color.Navy)
```

![CustomColor = "Navy"](image.png)

**Figure 203: CustomColor = "Navy"**

#### Popup Calculator Control

The `PopupCalculator` class is used to display a popup Calculator control. This class can be created programmatically as shown below:

##### Embedding the PopupCalculator Control

The `PopupCalculator` control can be embedded into a Windows Forms application by following these steps:

1. **Create the Control**: Instantiate a `PopupCalculator` object.
2. **Assign a Parent Control**: Define the control that will act as the parent for the popup.
3. **Set the Alignment**: Specify the alignment of the popup relative to the parent control.

**Example Code:**

```csharp
[C#]

private Syncfusion.Windows.Forms.Tools.PopupCalculator popupCalculator1;

private void buttonAdv1_Click(object sender, EventArgs e)
{
    // Create the Popup Calculator.
    popupCalculator1 = new Syncfusion.Windows.Forms.Tools.PopupCalculator();

    // The control that will act as the Popup's parent.
    this.popupCalculator1.ParentControl = this.button1;

    // Set the alignment.
    this.popupCalculator1.PopupCalculatorAlignment =
}
```

### Conclusion

The provided examples illustrate how to customize the appearance of a Calculator control using the `Office2007Theme` and `Office2007Colors`, as well as how to programmatically embed a `PopupCalculator` control into a Windows Forms application. These features enhance the usability and aesthetics of the application.

### API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `PopupCalculator`
  - **Properties**
    - `ParentControl`: Specifies the parent control for the popup.
    - `PopupCalculatorAlignment`: Determines the alignment of the popup relative to the parent control.

### Code Examples

The above sections include code snippets demonstrating the usage of the `PopupCalculator` class and how to customize the appearance of controls using the `Office2007Theme` API.

### RAG Annotations

<!-- tags: [syncfusion-winforms, control-customization, popup-calculator, office2007-theme] keywords: [calculator control, custom colors, popup calculator, windows forms, theme management, control alignment] -->
```