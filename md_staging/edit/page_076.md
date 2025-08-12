```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: edit
page_number: 076
page_id: edit#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:36Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

| Edit Control Property | Description |
|-----------------------|-------------|
| UseTabs               | Specifies whether tab symbol is allowed or spaces should be used instead.<br/>Setting this property to `True` allows you to insert tabs, whereas setting it to `False` allows you to insert spaces. |
| UseTabStops           | Gets / sets value that indicates whether tab stops should be used. |
| TabStopsArray         | Gets / sets an array of tab stops. |

```csharp
[C#]

this.editControl1.UseTabs = true;
this.editControl1.UseTabStops = true;
this.editControl1.TabStopsArray = new int[] { 8, 16, 24, 32, 40 };
```

```vb
[VB.NET]

Me.editControl1.UseTabs = True
Me.editControl1.UseTabStops = True
Me.EditControl1.TabStopsArray = New Integer() {8, 16, 24, 32, 40}
```

## Specifying Tab Size

The size of the tab can be specified by using the below given property.

| Edit Control Property | Description |
|-----------------------|-------------|
| TabSize               | Specifies tab size in spaces. |

```csharp
[C#]

// Size of the tab in terms of space.
this.editControl1.TabSize = 8;
```

```vb
[VB.NET]

' Size of the tab in terms of space.
Me.editControl1.TabSize = 8
```

<!--[tags: windows-forms, edit-control, tab-stops, tab-size, properties, Syncfusion Winforms, version: 11.4.0.26] keywords: [tab, space, tab stops array, use tabs, use tab stops, tab size, edit control property, C#, VB.NET]-->
```