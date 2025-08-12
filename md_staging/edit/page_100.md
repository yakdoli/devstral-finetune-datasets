```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_100.jpeg
document_name: edit
page_number: 100
page_id: edit#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:53Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### Properties and Description

| Property                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| EnableSmartInBlockIndent     | Gets or sets a value to make the Block mode work like Smart mode for conditional statements. |

#### C#

```csharp
this.editcontrol1.EnableSmartInBlockIndent = true;
```

#### VB.NET

```vb
Me.editcontrol1.EnableSmartInBlockIndent = True
```

### 4.4.11.3 AutoFormatting

- The Edit Control offers autoformatting and smart indentation support for code as in Visual Studio.
- Currently, only C# has built-in support for this feature.

AutoFormatting can be enabled by using the below given method.

| Edit Control Method | Description                               |
|--------------------|-------------------------------------------|
| AutoFormatText     | AutoFormats given range of text.         |

For example, the closing brace gets automatically aligned with the opening brace. Consider some C# code as shown in the below screenshot.
```

<!-- tags: [Syncfusion, WinForms, Essential Edit, EnableSmartInBlockIndent, AutoFormatting, AutoFormatText] keywords: [Block mode, Smart mode, conditional statements, indentation, code autoformatting, C#, VB.NET] -->
```