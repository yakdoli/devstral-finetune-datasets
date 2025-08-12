```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_945.jpeg
document_name: grid
page_number: 945
page_id: grid#page_945
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:50:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

- Through Code

## Through Verbs

The verbs **"Save Look and Feel"** and **"Choose Look and Feel"** that are found at the bottom of the **property grid** of the Grid Grouping control will allow you to easily accomplish this task. Use the **Save verb** to save the Look and Feel properties of the current Grid Grouping control. Then use the **Choose verb** to apply the saved settings to a different control.

![Look and Feel Customization Options](https://example.com/image_path)
* **Figure 351: Look and Feel Customization Options**

## Through Code

To apply the Look and Feel properties saved as XML at run-time, simply call the **ApplyXmlLookAndFeel** method. For example, the code below shows the code that is necessary to load such a file in the form's constructor.

### [C#]

```csharp
public Form1()
{
    System.Xml.XmlReader xr = new System.Xml.XmlReader("BaseLandF.xml");
    this.gridGroupingControl1.ApplyXmlLookAndFeel(xr);
}
```

### [VB.NET]

```vb
Public Sub New()
    Dim xr As System.Xml.XmlReader = New System.Xml.XmlReader("BaseLandF.xml")
    Me.gridGroupingControl1.ApplyXmlLookAndFeel(xr)
End Sub
```

## API Reference (if applicable)

<!-- No specific API reference is present on this page. -->

## Code Examples

- The example provided shows how to apply saved Look and Feel settings using XML at run-time in both **C#** and **VB.NET**.

## Page-level Navigation/TOC (if applicable)

<!-- No specific local Table of Contents is present on this page. -->

## Cross References

- This page describes how to save and apply Look and Feel properties in the Grid Grouping control.
- See also: [Grid Grouping Customization Options](https://example.com/grid_customization)

<!-- tags: [syncfusion, winforms, grid grouping, look and feel, xml, C#, VB.NET, tutorial] keywords: [GridGroupingControl, ApplyXmlLookAndFeel, Visual Studio, WinForms, Syncfusion.Windows.Forms.Grid, Look and Feel customization, XML serialization, properties, UI customization] -->
```