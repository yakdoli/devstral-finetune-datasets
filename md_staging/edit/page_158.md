```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_158.jpeg
document_name: edit
page_number: 158
page_id: edit#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:51Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
container = CodeSnippetsExtractor.Extract(vbsnippetsPath "\Loops")
container.Name = "Loops"
Me.editControl.Language.SnippetsContainer.AddContainer(container)
```

## Overview
- Code snippets can be created using the configuration file.
- The example demonstrates creating a snippet for a `struct` in C#.
- The snippet includes a title, shortcut, description, and code structure.

## Content

### Creating Code Snippets with Configuration File
Code snippets can also be created by using the configuration file. For example, the code snippet for a structure in C# can be created as shown below.

```xml
<CodeSnippetsContainer Name="Container 2">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>struct</Title>
            <Shortcut>struct</Shortcut>
            <Description>Code snippet for struct</Description>
        </Header>
        <Snippet>
            <Declarations>
                <Literal>
                    <ID>name</ID>
                    <ToolTip>Struct name</ToolTip>
                    <Default>MyStruct</Default>
                </Literal>
            </Declarations>
            <Code Language="csharp"><!-- [CDATA[
struct $name$
{
}] -->
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippetsContainer>
```

#### The Literal Element
The `Literal` element is used to identify a replacement for a piece of code that is entirely contained within the snippet, but one that will likely be customized after it is inserted into the code. For example, literal strings, numeric values, and some variable names should be declared as literals. The symbol `$` is placed at the beginning and end of the literal ID element value. For example, if a literal has an ID element that contains the value `MyID`, you must reference that literal in the code element as `$MyID$`. All code snippets must be placed between `<![CDATA[ and ]]>` brackets.

### Showing Code Snippets
You can programmatically show the choice list of code snippets by calling the `ShowCodeSnippets` method.

```csharp
[C#]
```

## API Reference

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [Essential Edit, code snippets, windows forms, configuration file, C# struct] keywords: [CodeSnippetsContainer, CodeSnippet, Literal, ShowCodeSnippets, C# struct snippet] -->
```