```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_265.jpeg
document_name: tools
page_number: 265
page_id: tools#page_265
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:51Z
fidelity: lossless
-->

## Content

### 3. Set the control as a non-dockable floating window.

- **C#:**
  ```csharp
  this.dockingManager1.SetFloatOnly(this.listView1, true);
  ```

- **VB.NET:**
  ```vb
  Me.dockingManager1.SetFloatOnly(Me.listView1, True)
  ```

### 4. Determine whether the control is floating using the DockingManager.IsFloating() method.

- If true, then the control is being hosted in a subclass of the Form type and this host form can be retrieved through the control's TopLevelControl property.
- Once you have the top-level form, just use the Control.Location property on that form to get its x and y coordinates.

---

#### Example: Getting the Location of a Floating Control

- **C#:**
  ```csharp
  // Get the FloatingForm object to get location of control. FloatingForm is a Form derived class.
  DockHost dhost = this.listView1.Parent as Syncfusion.Windows.Forms.Tools.DockHost;
  FloatingForm floatfrm = dhost.ParentForm as FloatingForm;
  MessageBox.Show(floatfrm.Location.ToString());
  ```

- **VB.NET:**
  ```vb
  ' Get the FloatingForm object to get location of control. FloatingForm is a Form derived class.
  Dim dhost As DockHost = CType(IIf(TypeOf Me.listView1.Parent Is Syncfusion.Windows.Forms.Tools.DockHost, Me.listView1.Parent, Nothing), Syncfusion.Windows.Forms.Tools.DockHost)
  Dim floatfrm As FloatingForm = CType(IIf(TypeOf dhost.ParentForm Is FloatingForm, dhost.ParentForm, Nothing), FloatingForm)
  MessageBox.Show(floatfrm.Location.ToString())
  ```

### 3.4.4.6.4 How to make a docked control Float Only?

The docked control can also be only floating and cannot be docked, by calling the SetFloatOnly method.

| Parameter | Description |
|-----------|-------------|

## API Reference

- **Method:** SetFloatOnly
  - **Parameters:** 
    - `control`: The control to set as float-only.
    - `enabled`: Boolean indicating whether the control should be set to float-only.

## Code Examples

### C# Example

```csharp
this.dockingManager1.SetFloatOnly(this.listView1, true);
```

### VB.NET Example

```vb
Me.dockingManager1.SetFloatOnly(Me.listView1, True)
```

## RAG Annotations

<!-- tags: [DockingManager, FloatOnly, TopLevelControl, ControlLocation, WinForms, Syncfusion] keywords: [docked control, floating window, x-y coordinates, DockHost, FloatingForm] -->
```