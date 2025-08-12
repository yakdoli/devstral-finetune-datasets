```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: edit
page_number: 026
page_id: edit#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:55:25Z
fidelity: lossless
-->

## [Essential Edit for Windows Forms](#)

- **If you specify EndBlock, specified formatting will be set only if first token matches ContinueBlock and is followed by EndBlock.**

### Word Wrap Mode Behavior
- All matched text will be treated later as one word and won't be broken into parts in WordWrap mode.

### Using Regular Expressions in Block Definitions
- If you want to use regular expressions in [Begin / Continue / EndBlock], you should set IsBeginRegex/IsContinueRegex/IsEndRegex to 'True'.

### Example

```xml
[XML]
<lexem BeginBlock="$" EndBlock="^[0-9a-fA-F]+$" IsEndRegex="true" Type="Number" />
```

#### Delphi File Parsing Example
- In Delphi file parsing, numbers in hexadecimal format like $54df54af will be treated as one word.

### Handling Complex Lexemes

- If the **IsComplex** attribute is set to 'True', and the token matches the BeginBlock of the lexem, then the lexem found is inserted into the stack. At the start, the stack contains only language, so the parser checks only for children of the `<lexems>` tag. Configuration for the token is always searched among sub-lexems of the last lexem in the stack. If the configuration is not found, a search is done among the sub-lexems of the second lexem in the stack, and so on. This feature can be disabled by setting the **OnlyLocalSublexems** attribute to 'True', and the token will be colored like the last lexem from the stack. If the configuration is still not found, the parser checks if it is the EndBlock of the last lexem in the stack, and if it matches, the token is formatted accordingly and the lexem is removed from the stack. If the token is the **EndBlock**, and the **IsPseudoEnd** attribute is set to 'True', the lexem is removed from the stack, but the search process for that token does not stop. Refer to the sample code below.

### Parsing a C# String Example

```xml
[XML]
<lexem BeginBlock="&quot;" EndBlock="&quot;" Type="String" IsComplex="true" OnlyLocalSublexems="true">
    <SubLexems>
        <lexem BeginBlock="\\" EndBlock="&quot;" Type="String" />
    </SubLexems>
</lexem>
```

## Footer
- **© 2013 Syncfusion. All rights reserved.**
- Page 26

<!-- tags: [Essential Edit, Regular Expressions, WordWrap mode, Lexem, Block Definitions, Delphi file parsing, C# strings, Managed States, Syncfusion Winforms] keywords: [BeginBlock, ContinueBlock, EndBlock, IsComplex, OnlyLocalSublexems, IsPseudoEnd, hexadecimal numbers, parsing, document formatting, example XML] -->
```