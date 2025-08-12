```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_041.jpeg
document_name: edit
page_number: 041
page_id: edit#page_041
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:40Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```xml
IsCollapseAutoNamed="true" CollapseName="#region"
  <SubLexems>
    <lexem BeginBlock="\n" IsBeginRegex="true" />
  </SubLexems>
</lexem>
```

Ampersands (&) can be escaped using `&amp`, less-than symbols (<) can be escaped using `&lt`, and greater-than symbols (>) can be escaped using `&gt`.

## Invalid Regular Expressions

If you enter an invalid regular expression pattern in a language definition that the Edit Control cannot parse, an exception is raised with a diagnostic message describing the problem.

### 4.2.5.1 Language Elements

The Edit Control regular expression engine accepts an extensive set of regular expression elements that enable you to efficiently search for text patterns. This section details the set of characters, operators, and constructs that you can use to define regular expressions.

#### Character Escapes

Most of the important regular expression language operators are unescaped single characters. The escape character `\` (a single backslash) signals to the regular expression parser that the character following the backslash is not an operator. For example, the parser treats an asterisk (*) as a repeating quantifier, and a backslash followed by an asterisk (`\*`) as the Unicode character `\u002A`.

| Escaped Character | Description                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------|
| (Ordinary characters) | Characters other than `. $ ^ { [ ( | ) * + ? \` match themselves.                        |
| `\a`                | Matches a bell (alarm) `\u0007`.                                                              |
| `\t`                | Matches a tab `\u0009`.                                                                       |
| `\r`                | Matches a carriage return `\u000D`.                                                           |
| `\v`                | Matches a vertical tab `\u000B`.                                                              |
| `\f`                | Matches a form feed `\u000C`.                                                                 |

<!-- tags: [winforms, regular expressions, language elements, character escapes, edit control] keywords: [regular expressions, escape characters, operators, constructs, Edit Control] -->
```