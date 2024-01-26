# autosimulacrum / socratic-sync

https://www.youtube.com/watch?v=NI5IGAim8XU
https://www.youtube.com/watch?v=6tNS--WetLI
https://www.youtube.com/watch?v=mzlH8lp4ISA

Utilities for doing work for https://www.instagram.com/simulacro.psi/, such as post automation, data cleanup, file organization, etc.

## Workflow

1. read book. mark book. check quality of ocr. remark book with desired quotations.
1. extract annotations from pdf
    - try python
1. cleanup quotes (`quote_cleanup`)
1. convert to docx
1. translate (google) (also fixes worst extraction errors)
    - try gpt
1. fix extraction errors (gpt3.5) (1 cent per 40k chars)
1. manually check translation. manually fix things.
1. make images. download images. organize images. (`organize_images`)
1. make buffer post.

## how to use

### using `quote_cleanup`

-   set parameters
-   fitted to deal with output from obsidian
-   run

### using `organize_images`

-   data structure:

        -   {book_name}
            -   text
            -   img
                -   ordered
                -   raw

-   files must be named correctly (by page number with duplicates for each additional image per post. maximum 10 images per post because of instagram limitations). see `test` for example.
-   put images in the folder called `data/raw/{BOOK_NAME}`
-   set parameter in `organize_files.py` and run it
-   it will make a folder for each post in `data/ordered/{BOOK_NAME}/{PAGE}`, which can now be iterated on by the main script

## TODO

-   features and bugs

    -   fix " ' ’ “ … « »
    -   prompt for fixing the weird gender things (see ose p 104)
    -   discover how buffer orders the input files
    -   this [extraction method](https://github.com/munach/obsidian-extract-pdf-annotations) cuts off last letter of every line. not good
        -   other ways of extracting annotations
            -   https://github.com/0xabu/pdfannots
            -   https://github.com/akaalias/obsidian-extract-pdf-highlights
            -   zotero extension highlight conversion
            -   https://www.systoolsgroup.com/pdf/extractor/
            -   https://pdf.wondershare.com/
            -   https://www.sumnotes.net/
            -   https://www.pdf-online.com/osa/extract.aspx?o=annots
    -   automation
        -   image generation in canva
        -   post scheduling through buffer
        -   post scheduling through api
    -   request that gets a random post
        -   post it to stories

-   internal
    -   add type annotations and fix exception bubbling
    -   export to yaml instead of txt
    -   make tests sensitive to file structure

## current

-   ime pt2
-   cis pt2
-   ose
    -   continue from 566

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
