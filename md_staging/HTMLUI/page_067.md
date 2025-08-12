```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: HTMLUI
page_number: 067
page_id: HTMLUI#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:30Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Methods

- **GetScriptCode:** Gets the string format of the script code

#### Example in C#
```csharp
MessageBox.Show("ScriptCode:\n" + this.script.GetScriptCode().ToString());
```

#### Example in VB.NET
```vb
MessageBox.Show("ScriptCode:" & Constants.vbLf & Me.script.GetScriptCode().ToString())
```

### 4.5.25 SELECT Element

The SELECT element is used to define a drop-down list. The user can specify the number of items to include in the drop-down list. The SELECTElementImpl class defines the properties and methods for this element.

#### Properties

- **UserControl:** Gets / sets the user control instance to the particular element

#### Example in C#
```csharp
// UserControl property gets or sets the user control instance to the particular element.
Hashtable htmlElements = this.htmluiControl.Document.GetElementsByIdHash();
this.select = htmlElements["select"] as SELECTElementImpl;
this.label1.Text = "\nSelect(UserControl): " + this.UserControl.DefaultSize.ToString();
```

#### Example in VB.NET
```vb
' UserControl property gets or sets the user control instance to the particular element.
```

---

---

<!-- tags: [HTMLUI for Windows Forms, SELECT Element, Script Element, WinForms, Syncfusion] keywords: [HTMLUI, SELECT Element, Script Code, UserControl, WinForms] -->
```