```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: edit
page_number: 027
page_id: edit#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

To collapse complex lexems, set `IsCollapsible` to 'True'. The `CollapseName` property specifies the text to be set instead of the collapsed construction. To make the C# string collapsible, you should use the following code:

```xml
<lexem BeginBlock="&quot;" EndBlock="&quot;" Type="String" IsComplex="true"
OnlyLocalSublexems="true" IsCollapsible="true" CollapseName="String">
    <SubLexems>
        <lexem BeginBlock="\" EndBlock="&quot;" Type="String" />
    </SubLexems>
</lexem>
```

## Loading a Config File

To load a Config file to the Edit Control, use the following code snippet.

### Code: C#
```csharp
this.editControl1.Configurator.Open(string fileName);
```

### Code: VB
```vb
Me.editControl1.Configurator.Open(String fileName)
```

## See Also

- Creating Configuration Settings Programmatically

### 4.1.2 Creating Configuration Settings Programmatically

Edit Control offers a rich set of APIs to create configuration settings in code. This provides greater flexibility so that users can dynamically modify configuration settings of the currently loaded configuration as per their requirements. The following procedure will guide you through the entire process of creating configuration settings programmatically.

1. A new configuration language can be added to the Edit Control by using the `CreateLanguageConfiguration` method. Once the new configuration language is created, apply it to the contents of the Edit Control by using the `ApplyConfiguration` method.

<!-- tags: [Syncfusion Winforms, Edit Control, Configuration Settings, Customization, APIs] keywords: [Configuration, Programmatically, Edit Control, Flexible Settings, Dynamic Configuration] -->
```