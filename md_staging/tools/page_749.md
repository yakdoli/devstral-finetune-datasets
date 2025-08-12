```html
<!--  
source: image  
domain: syncfusion-sdk  
task: pdf-ocr-to-markdown  
language: en (keep original; do not translate)  
source_filename: page_749.jpeg  
document_name: tools  
page_number: 749  
page_id: tools#page_749  
product: Syncfusion Winforms  
version: 11.4.0.26  
timestamp: 2025-08-09T10:31:18Z  
fidelity: lossless  
-->  

# Essential Tools for Windows Forms  

## Overview  
- The section explains how to use the IntegerTextBox control in Windows Forms, focusing on banner text support and appearance settings.  
- Demonstrates configuring properties like `AllowNull`, `NullString`, and `Text` for banner text functionality.  
- Covers background color settings using different properties for ReadOnly and normal modes.  

## Content  

### 3.5.8.4.3  
**Banner Text Support**  
The IntegerTextBox control can display banner text in the text field at runtime. A `BannerTextProvider Component` should be available for this purpose. Additionally, the following properties need to be set to make this feature effective:  

#### C#  
```csharp  
this.integerTextBox1.AllowNull = true;  
this.integerTextBox1.NullString = "";  
this.integerTextBox1.Text = "";  
```  

#### VB.NET  
```vbnet  
Me.integerTextBox1.AllowNull = True  
Me.integerTextBox1.NullString = ""  
Me.integerTextBox1.Text = ""  
```  

### 3.5.8.4.5  
**Appearance Settings**  
#### Background Settings  
The background settings of the IntegerTextBox control are discussed below.  

#### Background Color  
The background color of the control can be set using the properties given below.  

| IntegerTextBox Properties                | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| BackColor                                | Specifies the background color of the component.                          |
| ReadOnlyBackColor                       | Specifies the backcolor to be used when the control is in the ReadOnly mode. |

#### Code Example  
```csharp  
this.integerTextBox1.BackColor = System.Drawing.Color.PeachPuff;  
this.integerTextBox1.ReadOnly = true;  
this.integerTextBox1.ReadOnlyBackColor = 
```  

## API Reference  
- **BackColor**  
  - Specifies the background color of the component.  
- **ReadOnlyBackColor**  
  - Specifies the backcolor to be used when the control is in the ReadOnly mode.  

## Code Examples  
#### C#  
```csharp  
this.integerTextBox1.BackColor = System.Drawing.Color.PeachPuff;  
this.integerTextBox1.ReadOnly = true;  
this.integerTextBox1.ReadOnlyBackColor = 
```  

#### VB.NET  
```vbnet  
Me.integerTextBox1.BackColor = System.Drawing.Color.PeachPuff  
Me.integerTextBox1.ReadOnly = True  
Me.integerTextBox1.ReadOnlyBackColor = 
```  

## Cross References  
- **Related Topics:**  
  - `BannerTextProvider Component`  
  - `IntegerTextBox Properties`  

<!-- tags: [Syncfusion Winforms, IntegerTextBox, banner text, background settings, appearance, ReadOnly] keywords: [AllowNull, NullString, Text, BackColor, ReadOnlyBackColor] -->
```