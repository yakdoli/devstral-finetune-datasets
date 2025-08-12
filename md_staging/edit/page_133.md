```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_133.jpeg
document_name: edit
page_number: 133
page_id: edit#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:02:44Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

Syntax Highlighting is accomplished in Essential Edit through the use of XML-based configuration files.

The language-specific configuration is stored in XML files. The below given code snippet illustrates a sample configuration file that can be used for syntax highlighting a LISP-like code.

## XML Configuration Sample

```xml
<ConfigLanguage name="Custom LISP">
    <formats>
        <format name="Text" Font="Courier New, 10pt" FontColor="Black" />
        <format name="Whitespace" Font="Courier New, 10pt" FontColor="Black" />
        <format name="Keyword" Font="Courier New, 10pt" FontColor="Blue" />
        <format name="String" Font="Courier New, 10pt, style=Bold" FontColor="Red" />
        <format name="Number" Font="Courier New, 10pt, style=Bold" FontColor="Navy" />
        <format name="Operator" Font="Courier New, 10pt" FontColor="DarkCyan" />
        <format name="Comment" Font="Courier New, 10pt, style=Bold" FontColor="Green" />
        <format name="SelectedText" Font="Courier New, 10pt" BackColor="Highlight" FontColor="HighlightText" />
        <format name="CollapsedText" Font="Courier New, 10pt" FontColor="Black" BackColor="White" />
    </formats>
    <extensions>
        <extension>lsp</extension>
    </extensions>
    <lexems>
        <lexem BeginBlock="(" Type="Operator" />
        <lexem BeginBlock=")" Type="Operator" />
        <lexem BeginBlock="' " Type="Operator" />
        <lexem BeginBlock="car" Type="KeyWord" />
        <lexem BeginBlock="cdr" Type="KeyWord" />
        <lexem BeginBlock="cons" Type="KeyWord" />
        <lexem BeginBlock="#Region" EndBlock="#End Region" Type="PreprocessorKeyword" IsEndRegex="true" IsComplex="true" IsCollapsable="true" AutoNameExpression="\s*(?&lt;text&gt;).*\n" AutoNameTemplate="${text} " IsCollapseAutoNamed="true" CollapseName="#Region">
            <SubLexems>
                <lexem BeginBlock="\n" IsBeginRegex="true" />
            </SubLexems>
        </lexem>
    </lexems>
</ConfigLanguage>
```

## Summary

- Syntactical elements are defined using XML-based configuration files.
- Various formats such as text, keywords, comments, and regions are specified with distinct font styles and colors.
- Support for highlighting customized LISP-like syntax demonstrates flexibility in language-specific configurations.

## Page-level Navigation/TOC
- Essential Edit for Windows Forms
- Syntax Highlighting Overview
- Language-Specific Configuration

<!-- tags: [Syncfusion Winforms, syntax highlighting, XML configuration, LISP-like syntax, language-specific configuration, Essential Edit, Windows Forms] keywords: [Custom LISP, Font styles, Keywords, Comments, Regions, Selected text, Collapsed text, Operators, Preprocessor keywords, Auto naming] -->
```