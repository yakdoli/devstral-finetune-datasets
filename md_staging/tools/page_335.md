```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_335.jpeg
document_name: tools
page_number: 335
page_id: tools#page_335
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

We can associate the `AutoAppend` class to a `ComboBox` control by following the below steps.

## Steps to Associate AutoAppend Class to a ComboBox

1. Open a Visual Studio project and include the required namespace.

   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. Drag and drop a `ComboBox` control from the Toolbox onto the form.

3. Create and instance of the `AutoAppend` class as follows.

   ```csharp
   // Creating an instance of the AutoAppend Class.
   private AutoAppend autoAppend1;
   autoAppend1 = new AutoAppend();
   ```

   ```vb
   ' Creating an instance of the AutoAppend Class.
   Private autoAppend1 As AutoAppend
   Private autoAppend1 = New AutoAppend()
   ```

4. After creating the `AutoAppend` instance, we need to associate it with an edit control. To achieve this, use the `AutoAppend.SetAutoAppend` method. This method takes an object of `AutoAppendInfo` class which is used to hold the details of the data associated.

   | Method          | Description                                                                                          |
   |-----------------|------------------------------------------------------------------------------------------------------|
   | `SetAutoAppend` | Sets `AutoAppend` behavior for the control specified. The parameters are:<br>`control` - control to which auto append class has to be associated.<br>`autoAppendInfo` - Initializes an `AutoAppendInfo` class which has three parameters - |

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `AutoAppend`
- **Method**: `SetAutoAppend`

### Parameters

| Name           | Type                             | Description                                                                                          |
|----------------|----------------------------------|------------------------------------------------------------------------------------------------------|
| `control`      | `System.Windows.Forms.Control` | The control to which the auto append class has to be associated.                                  |
| `autoAppendInfo` | `AutoAppendInfo`          | An `AutoAppendInfo` class instance which holds the details of the data associated.                 |

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Tools;

// Creating an instance of the AutoAppend Class.
private AutoAppend autoAppend1;
autoAppend1 = new AutoAppend();

// Assuming 'comboBox1' is the ComboBox control on the form
autoAppend1.SetAutoAppend(comboBox1, new AutoAppendInfo());
```

### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Tools

' Creating an instance of the AutoAppend Class.
Private autoAppend1 As AutoAppend
Private autoAppend1 = New AutoAppend()

' Assuming 'comboBox1' is the ComboBox control on the form
autoAppend1.SetAutoAppend(comboBox1, New AutoAppendInfo())
```

<!-- tags: [product, module, control, api, version?] keywords: [AutoAppend, ComboBox, Windows Forms, AutoAppendInfo] -->
```