```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_163.jpeg
document_name: edit
page_number: 163
page_id: edit#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:48Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

```csharp
[C#]

// Specify tooltip text for each Context Choice list item.
controller.Items.Add("LoadFile", "Use this method to open a file in EditControl.", this.editControl1.ContextChoiceController.Images["Image3"]);
```

```vb.net
[VB.NET]

' Specify tooltip text for each Context Choice list item.
controller.Items.Add("LoadFile", "Use this method to open a file in EditControl.", Me.editControl1.ContextChoiceController.Images["Image3"])
```

### Customization

#### Border Settings

The border color of the Context Choice form is set by using the `ContextChoiceBorderColor` property.

| Edit Control Property | Description |
|-----------------------|-------------|
| `ContextChoiceBorderColor` | Specifies the color of the Context Choice form border.<br> Used when the `UseXPStyle` property is set to 'False'. Otherwise, a 3D border is drawn. |

```csharp
[C#]

this.editControl1.ContextChoiceBorderColor = System.Drawing.Color.Red;
```

```vb.net
[VB.NET]

Me.editControl1.ContextChoiceBorderColor = System.Drawing.Color.Red
```

#### Size Settings

The size of the Context Choice form can be set by using the `ContextChoiceSize` property.

```csharp
[C#]

this.editControl1.ContextChoiceSize = new System.Drawing.Size(100, 50);
```
```