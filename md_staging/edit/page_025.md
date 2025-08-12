```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_025.jpeg
document_name: edit
page_number: 025
page_id: edit#page_025
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:22Z
fidelity: lossless
-->

## Splits Syntax

- **Splits**: Contains a list of expressions that must be treated as one word. By default, "=" and "+" are splitters; So each of them will be returned by the tokenizer as a single char. But if you want to specify some configuration for "+=", you should specify "+=" in the Splits section. To do this, just add the below string to the Splits section:

```xml
<split>+=</split>
```

## Formats Definition

- **Formats**: Contains a list of definitions of the formats that can be used later in lexem configuration. Every format is specified by a tag ` <format>` . Every format contains the attributes such as name, font, fore color, font color, back color, style, weight, underline, and line color.

  - **Name**: Specifies the name of the format. **SelectedText** is always used for selection (if fontcolor is not specified, selected text is drawn with its own color; only the background is changed).
  - **Font**: String with XML representation of the font. Refer to the default configuration file for examples.
  - **Forecolor**: Specifies the color of the rectangle that is drawn around the text. It is not drawn if fore color is not specified.
  - **FontColor**: Specifies the color of the text.
  - **BackColor**: Specifies the background color of the text.
  - **Style**: Specifies the fill style of the background. Look at the HatchStyle enumeration members for the list of possible values.
  - **Weight**: Weight of the underlining. Possible values: Thick, Bold, Double, and Double Bold.
  - **Underline**: Underline style. Possible values: None, Solid, DashDot, and Wave.
  - **LineColor**: Color of the underlining.

## Lexems Configuration

- **Lexems**: Contains rules for parsing text. In other words, rules for setting lexem format. There are two attributes to specify the format of the lexem: **Type** and **FormatName**. FormatName is used only if Type is 'Custom'. Type is used for standard predefined types of lexems, some of them have special meaning for controls (such as SelectedText). For a list of possible values. Refer to the definition of the FormatType enumeration.

The simplest case of lexem definition looks like the following:

```xml
[XML]

<lexem BeginBlock="public" Type="KeyWord" />
```

It means that the word **public** will be drawn using the **KeyWord** format setting. For non-complex lexems, you can specify **ContinueBlock** and **EndBlock** attributes.

- If you specify **ContinueBlock**, the parser will read words (tokens) and set the specified formatting for them until it encounters a **ContinueBlock**.

## Summary

This section discusses the configuration of `Splits`, `Formats`, and `Lexems` in setting up text formatting and parsing rules in a Syncfusion WinForms application. It includes details on specifying custom word groupings, defining highlighting formats, and configuring lexem-based text parsing with examples and attribute descriptions.

### Page-level Navigation/TOC

- **Splits Configuration**
- **Formats Definition**
- **Lexems Parsing Rules**

### Cross References

See also:
- `Splits` section for custom word grouping configurations.
- `Formats` section for defining text highlighting styles.
- `Lexems` section for token-based text parsing rules.

### RAG Annotations

<!-- tags: [Syncfusion, WinForms, Splits, Formats, Lexems, Tokenization, SyntaxHighlight, Settings] keywords: [Splits, Formats, Lexems, BeginBlock, ContinueBlock, EndBlock, Tokenizer, Word Grouping, Text Parsing, Format Settings, Syntax Highlighting] -->
```