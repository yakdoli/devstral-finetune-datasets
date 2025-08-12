```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: edit
page_number: 199
page_id: edit#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:56Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

Additionally, parsers can detect the situation when no legal end state can be reached, from the sequence of tokens that have been processed.

## Lexical Analysis

Lexical Analysis is the process of scanning text in a document and breaking it up into meaningful tokens. The purpose of lexical analyzers is to take a stream of input characters, and decode them into higher level tokens that a semantic parser can understand. In this stage, the text is split into tokens with the help of some special rules specified by the user. For instance, the user can specify "=+" or "end if" expressions as single tokens using the Split tag in the configuration file. Tokens are plain text, and have no additional information or meaning associated with them.

## Semantic Parsing

In this stage, the syntax highlighting rules are applied. These rules can be as simple as identifying the format name of the token, and applying the appropriate font or color settings. But this simple two-phase procedure was not very flexible in complex scenarios involving embedded scripts. Hence the entire process has been enhanced from the very beginning, by merging the lexical analysis and semantic parsing.

The Parser property indicates the parser used for parsing the currently loaded document in the Edit Control. The parsing process could be performed for any (or all) of the following purposes - syntax highlighting, intellisense, outlining and so on. The rules for the parsing process are specified in the XML based configuration file used.

### C# Code Example

```csharp
// Indicates the parser used for parsing the currently loaded document in the Edit Control.
RenderableLexemParser lexemParser = this.editControl.Parser;
```

### VB.NET Code Example

```vbnet
' Indicates the parser used for parsing the currently loaded document in the Edit Control.
Dim lexemParser As RenderableLexemParser = Me.editControl.Parser
```

## Parsing Modes

Edit Control supports several modes of text parsing which can be specified to the ParsingMode property by using the TextParsingMode enumerator. The default value of the ParsingMode property is set to PartialParsingNoFallback.

| Edit Control Property | Description |
|------------------------|-------------|
| ParsingMode           | Gets / sets text parsing mode. User can select between high parsing |

<!-- tags: [product, module, control, api, version?] keywords: [lexical analysis, semantic parsing, parsing modes, Edit Control, RenderableLexemParser, TextParsingMode, Parser, partial parsing] -->
```