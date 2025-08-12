```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_659.jpeg
document_name: tools
page_number: 659
page_id: tools#page_659
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The primitive type to be included should be chosen from the Types of Primitives available in the GradientPanelExt Collection Editor, and added to the control. The properties for the primitive can be set in the property grid available at the right side.

### 3.5.6.3.3.1.1 Expand and Collapse Options

Including the Collapse primitive, provides option to expand and collapse the GradientPanelExt. Performing the following steps will add the Collapse Primitive at design time.

1. Open the GradientPanelExt Collection Editor, and choose the Collapse primitive from the ComboBox available and add it.
2. Set the collapse and expand images in the CollapseImage and ExpandImage property respectively.
3. Specify the alignment and position of the primitive using its respective properties.
4. Close the GradientPanelExt Collection Editor. Build and run the application.
5. Now clicking on the Collapse primitive, collapses the control. The control collapses and expands on alternate clicks.

#### C#
```csharp
Syncfusion.Windows.Forms.Tools.CollapsePrimitive collapsePrimitive1;
gradientPanelExt1.Primitives.Add(collapsePrimitive1);
collapsePrimitive1.Alignment =
Syncfusion.Windows.Forms.Tools.Alignment.Bottom;
collapsePrimitive1.BackColor = System.Drawing.Color.Transparent;
collapsePrimitive1.CollapseImage =
((System.Drawing.Image)(resources.GetObject("collapsePrimitive1.CollapseImage")));
collapsePrimitive1.ExpandImage =
((System.Drawing.Image)(resources.GetObject("collapsePrimitive1.ExpandImage")));
collapsePrimitive1.Position = 130;
collapsePrimitive1.Size = new System.Drawing.Size(40, 40);
```

#### VB.NET
```vb
Private collapsePrimitive1 As
Syncfusion.Windows.Forms.Tools.CollapsePrimitive
gradientPanelExt1.Primitives.Add(collapsePrimitive1)
Private collapsePrimitive1.Alignment =
Syncfusion.Windows.Forms.Tools.Alignment.Bottom
Private collapsePrimitive1.BackColor = System.Drawing.Color.Transparent
Private collapsePrimitive1.CollapseImage =
(CType(resources.GetObject("collapsePrimitive1.CollapseImage"), System.Drawing.Image))
Private collapsePrimitive1.ExpandImage =
```

---

© 2013 Syncfusion. All rights reserved.
```