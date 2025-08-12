```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: DocIo
page_number: 254
page_id: DocIo#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:44:21Z
fidelity: lossless
-->

## Essential DocIO

### Sample Code

```vb
[VB]

' Create TextBodySelection and select the items of interest.
Dim textSel As TextBodySelection = New TextBodySelection(sec.Body, 0, lastItemIndex, 0, lastItemIndex)

' Create TextBodyPart and copy the selected items.
Dim replacePart As TextBodyPart = New TextBodyPart(doc)
replacePart.Copy(textSel)

' Paste the copied text at the end of the text body.
replacePart.PasteAt(txtbdy, itemIndex)
```

### Find

Essential DocIO provides various methods to improve the flexibility of the Find feature in the Word document.

#### Find Method

Find method is used to find an entry with a specified text or regular expression in the Word document.

Following are the possible input parameters of the Find method.

- **given string to find.**
- **caseSensitive**: defines if replace is case sensitive. For example, if case sensitive is set to false, and you want to find "AA" string, then in such case strings like "aA" and "Aa" also will be returned (will fit the search conditions).
- **wholeWord**: if set to true, string given must be the whole word (not part of the word).

The following are the variants of the Find method.

- **TextSelection Find(string given, bool caseSensitive, bool wholeWord)**: finds and returns an entry of specified string along with formatting, taking into consideration case-sensitive and whole word options.

---
© 2013 Syncfusion. All rights reserved. 254 | Page
```

<!-- tags: [syncfusion-sdk, essential-docIo, find-feature, word-document, text-selection, c#, vb, document-processing, api-reference, coded-examples] keywords: [DocIO, find method, case-sensitive search, whole word search, text selection, document processing, essential docIo, word document, find feature, search options, text body selection, text body part, replacement] -->