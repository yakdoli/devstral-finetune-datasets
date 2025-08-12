```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: edit
page_number: 160
page_id: edit#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:11Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

### WinForms Context Choice List

The Context Choice displaying characters are specified in the configuration file by using the DropContextChoiceList field in the lexem for the corresponding character. If you wish to display the Context Choice dropdown in response to the period (`.`) or comma (`,`) being typed, use the following XML code.

```xml
[XML]

<lexem BeginBlock="." Type="Operator" DropContextChoiceList="true"/>
<lexem BeginBlock="," Type="Operator" DropContextChoiceList="true"/>
```

The preceding code has to be placed within the `<lexems>` section of the configuration file.

### AutoCompleteSingleLexem

The AutoCompleteSingleLexem property indicates whether the Context Choice list gets autocompleted when a single lexem remains in the list.

```csharp
[C#]

```

## API Reference

### WinForms-specific conventions
- Use C# for examples unless VB is explicitly shown.
- Maintain exact control names, namespaces, and types.
- Differentiate between design-time and runtime features.
- Document properties, methods, events, and enums as seen in the page.

### Design and Runtime Features
- Ensure property grids and designer steps are described accurately.
- Include any relevant method signatures and event handlers.

### Parameters
- List parameters with Name, Type, Description, Default, and Required status.

### Returns
- Specify return type and description.

### Exceptions
- Provide any specific exceptions that may occur.

### Code Examples
- Extract all code examples, including full signatures, imports, and comments.
- Use fenced blocks (````csharp`, ```xml`, etc.) for code snippets.

## Cross References

- See also: [relevant links or text from the page, if any]

## RAG Annotations

<!-- tags: [edit, context-choice, winforms, configuration, auto-complete, lexem] keywords: [context choice, dropdown, configuration file, DropContextChoiceList, AutoCompleteSingleLexem] -->
```