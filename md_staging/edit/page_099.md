```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: edit
page_number: 099
page_id: edit#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:59:35Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Auto Indentation Demo

The Auto Indentation characters can be specified by setting the `Indent` field to `True` in the lexem definition of the configuration file, as shown below.

### Figure 31: AutoIndentMode = "Block"

![Auto Indentation Demo](auto_indention_demo.png)

The Auto Indentation characters can be specified by setting the `Indent` field to `True` in the lexem definition of the configuration file, as shown below.

### XML Example

```xml
<lexem BeginBlock="{" EndBlock="}" Type="Operator" IsComplex="true" IsCollapsable="true" Indent="true" CollapseName="{...}" IndentationGuideline="true">
```

A sample which demonstrates Auto Indentation is available in the below sample installation path.

### Sample Path

```
..\\My Documents\\Syncfusion\\EssentialStudio\\VersionNumber\\Windows\\Edit.WIndows\\Samples\\2.0\\Text Formatting\\AutoIndentationDemo
```

### Lexem Support for AutoIndent Block Mode

#### Overview
- **Enables AutoIndent Block mode**
- **Smart block alignment with lexem's config indentation**
- **Preserves previous indentation lines**

In the Edit control, the `EnableSmartInBlockIndent` property ensures the AutoIndent Block mode with respect to the lexem's `config.indent`. With this property, the Block mode will work like Smart mode for conditional statements.

When this property is enabled, the lines will be aligned to the position of the previous indented line. The lines will begin at the original start position if disabled.

### Conclusion
The Auto Indentation features in Syncfusion's WinForms provide developers with powerful tools to maintain code readability and consistency. By configuring the lexem definitions and utilizing properties like `EnableSmartInBlockIndent`, developers can streamline their coding workflows and enhance the maintainability of their codebases.

### Related Links
- [Page 100](edit#page_100) for additional configuration details
- [Chapter 4: Text Formatting](edit#chapter_4)
- [Auto Indentation Samples Repository](https://github.com/Syncfusion/Samples_Windows)

<!-- tags: [product, module, control, api, version?] keywords: [AutoIndentMode, lexem, Indent, EnableSmartInBlockIndent, Block mode, Smart mode, Syncfusion Edit Control, Windows Forms, Auto Indentation, Configuration] -->
```