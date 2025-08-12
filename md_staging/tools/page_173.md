```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_173.jpeg
document_name: tools
page_number: 173
page_id: tools#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:10:52Z
fidelity: lossless
-->

Essential Tools for Windows Forms

```csharp
this.dockingManager1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Silver;
```

```vb.net
Me.dockingManager1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Silver
```

![Figure 86: Blue, Silver and Black Themes in Office2007 Visual Styles](image.png)

## Custom Color Schemes

Custom colors can also be applied to DockingManager for Office2007 style, using the below code snippet.

```csharp
dockingManager1.Office2007Theme = Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Red);
```

```vb.net
dockingManager1.Office2007Theme = Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(Me, Color.Red);
```

<!-- tags: [custom color schemes, office2007 themes, dockingmanager, windows forms] keywords: [custom colors, office2007 style, managed colors, themes, docking, windows forms] -->
```