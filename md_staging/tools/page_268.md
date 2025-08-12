```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_268.jpeg
document_name: tools
page_number: 268
page_id: tools#page_268
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:23Z
fidelity: lossless
--> 

## Essential Tools for Windows Forms

```csharp
Me.dockingManager1.GetHiddenOnLoad(Me.listBox1)
Console.Write("Hidden on load " + Me.dockingManager1.GetHiddenOnLoad(Me.listBox1))
```

### setHiddenOnLoad

This method, when called, will decide whether or not to set the docked control as hidden at runtime.

#### C#

```csharp
this.dockingManager1.SetHiddenOnLoad(this.listBox1, true);
```

#### [VB.NET]

```vb
Me.dockingManager1.SetHiddenOnLoad(Me.listBox1, True)
```

### 3.4.4.7.3 How to hide a control when an application loads?

This is done programmatically, by calling `SetHiddenOnLoad` method or through Designer, by setting `HiddenOnLoad` property to `true`.

#### Method Description
| Method           | Description                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------|
| setHiddenOnLoad  | Hides the docked control when the application loads. The parameters are, <br> `Ctrl` - Indicates the docked control. <br> `bhidden` - Value indicating true or false. |

#### C#

```csharp
this.dockingManager1.SetHiddenOnLoad(this.listBox1, true);
```

#### [VB.NET]

```vb
Me.dockingManager1.SetHiddenOnLoad(Me.listBox1, True)
```

### 3.4.4.8 Serialization

This section covers the following topic:

<!-- 
tags: [Syncfusion, Windows Forms, Docking, Serialization, HiddenOnLoad, tools#page_268] 
keywords: [docking, hidden, load, control, SetHiddenOnLoad, GetHiddenOnLoad, serialization, windows forms, docked control, application load, VB.NET, C#] 
--> 
```