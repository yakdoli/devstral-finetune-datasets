```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_728.jpeg
document_name: tools
page_number: 728
page_id: tools#page_728
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on incorporating the DoubleTextBox control into Windows Forms applications.
- Explains both design-time (drag-and-drop) and runtime (programmatic) approaches.
- Guides through the necessary assembly references and namespaces.

## Content

### 3.5.8.3.2 Creating DoubleTextBox

To use a DoubleTextBox control in your application, all you need to do is drag and drop the DoubleTextBox control from the controls toolbox onto your form.

#### Design-Time Approach

A visual representation of the toolbox with the DoubleTextBox control highlighted is shown below:

![DoubleTextBox in Toolbox](Figure 459: DoubleTextBox in Toolbox "DoubleTextBox in Toolbox")

Figure 459: DoubleTextBox in Toolbox

#### Programmatic Approach

It can be created programmatically as follows:

1. **Add Assembly References and Namespaces**
   - Add Shared.Base, Shared.Windows, Tools.Base, and Tools.Windows assembly references.
   - Include the required namespace.

   **[C#]**
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **[VB.NET]**
   ```vb
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create and Add the DoubleTextBox Instance**
   - Create an instance of the DoubleTextBox.
   - Add that instance to the Form.

   **[C#]**
   ```csharp
   this.doubleTextBox1 = new Syncfusion.Windows.Forms.Tools.DoubleTextBox();
   this.Controls.Add(this.doubleTextBox1);
   ```

   **[VB.NET]**
   ```vb
   this.doubleTextBox1 = New Syncfusion.Windows.Forms.Tools.DoubleTextBox()
   Me.Controls.Add(this.doubleTextBox1)
   ```

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: DoubleTextBox

### Properties
- **Text**: Gets or sets the text displayed in the control.
- **Value**: Gets or sets the double value of the control.

### Methods
- **ParseInput()**: Parses the input text to a double value.
- **IsValidValue(double value)**: Checks if the given value is valid.

### Events
- **ValueChanged**: Occurs when the value in the control changes.

## Code Examples

### Example: Programmatic Creation of DoubleTextBox
**[C#]**
```csharp
using Syncfusion.Windows.Forms.Tools;

// Step 1: Create the DoubleTextBox instance
DoubleTextBox doubleTextBox1 = new DoubleTextBox();

// Step 2: Customize properties if needed
doubleTextBox1.Text = "123.45";
doubleTextBox1.Value = 123.45;

// Step 3: Add to the form
this.Controls.Add(doubleTextBox1);
```

**[VB.NET]**
```vb
Imports Syncfusion.Windows.Forms.Tools

' Step 1: Create the DoubleTextBox instance
Dim doubleTextBox1 As New DoubleTextBox()

' Step 2: Customize properties if needed
doubleTextBox1.Text = "123.45"
doubleTextBox1.Value = 123.45

' Step 3: Add to the form
Me.Controls.Add(doubleTextBox1)
```

## See also
- Syncfusion.Windows.Forms.Tools documentation for further details on Tool controls.

<!-- tags: [Syncfusion, WinForms, DoubleTextBox, Windows Forms, Tool Controls] keywords: [DoubleTextBox, programmatic creation, designer creation, Windows Forms, Syncfusion Controls] -->
```