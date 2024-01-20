# autosimulacrum / socratic-sync

Utilities for doing work for https://www.instagram.com/simulacro.psi/, such as post automation, data processing, file organization, etc.

## Utilities

-   data generation
    -   read book. mark book. check quality of ocr. remark book with desired quotations.
    -   v1 - extract annotations in obsidian using https://github.com/munach/obsidian-extract-pdf-annotations
        -   TODO BUG this cuts every last letter off
    -   v2 - convert into convenient format (`batch_convert`)
    -   v3 - manually edit
    -   v4 - convert to docx
    -   v5 - translate with google
    -   v6 - end. check translation. upload
    -   ? batch fix extraction errors (with gpt3.5)
        -   (1 cent per 40k chars)
    -   batch translate
        -   check google vs gpt
    -   organize files
-

## how to use

### using `batch_convert`

-   set parameters
-   fitted to deal with output from obsidian
-   run

### using `organize_files.py`

-   files must be named correctly (by page number with duplicates for each additional image per post. maximum 10 images per post because of instagram limitations). see `test` for example.
-   put images in the folder called `data/raw/{BOOK_NAME}`
-   set parameter in `organize_files.py`
-   it will make a folder for each post in `data/ordered/{BOOK_NAME}/{PAGE}`, which can now be iterated on by the main script

## TODO

-   BUG this extracting method cuts off last letter of every line. not good

    -   other ways of extracting annotations
        -   https://github.com/0xabu/pdfannots
        -   try https://github.com/akaalias/obsidian-extract-pdf-highlights
        -   try zotero extension highlight conversion
        -   https://www.systoolsgroup.com/pdf/extractor/
        -   https://pdf.wondershare.com/
        -   https://www.sumnotes.net/
        -   https://www.pdf-online.com/osa/extract.aspx?o=annots

-   add tests
-   automation
    -   image generation in canva
    -   post scheduling through buffer
    -   post scheduling through api
-   request that gets a random post
    -   post it to stories

## current

-   ime (en, pt)
-   cis (en, pt)

## upcoming

-   beer (pt)
-   hacking (en)
-   grunbaum (en)
-   ose (en)
-   fig (pt)
-   figlou (pt)
-   cr (en)
-   musgrave (en)

## possibly

-   dunker
-   wpf
-   never been modern
-   graeber
-   pasternak & pilati
-   gattei

## References

-   instagram api

    -   https://levelup.gitconnected.com/automating-instagram-posts-with-python-and-instagram-graph-api-374f084b9f2b
    -   https://skolo.online/documents/instagram/#pre-requisites-for-instagram-automation
    -   https://developers.facebook.com/docs/instagram-api/
    -   https://developers.facebook.com/docs/instagram-basic-display-api
    -   https://developers.facebook.com/docs/instagram-api/guides/content-publishing/
    -   https://developers.facebook.com/blog/post/2021/01/26/introducing-instagram-content-publishing-api/
    -   https://aphrx.medium.com/automating-social-media-posts-with-python-instagram-graph-api-b9bd81eac5c
    -   https://igsumo.com/

-   image generation
    -   https://www.analyticsvidhya.com/blog/2021/05/automate-your-image-processing-using-python/
    -   https://towardsdatascience.com/automate-graphic-design-using-python-e161bce62cfe
    -   https://neptune.ai/blog/image-processing-python
    -   https://www.youtube.com/watch?v=D6Qo0YAvuQM
    -   https://playwright.dev/python/docs/intro
    -   https://oxylabs.io/blog/playwright-web-scraping
    -   https://www.browserstack.com/guide/playwright-tutorial
