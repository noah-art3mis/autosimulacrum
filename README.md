# auto-simulacrum / socratic-sync

Instagram post automation for https://www.instagram.com/simulacro.psi/. Organize files then upload them automatically to Buffer using Playwright.

## using organize_files.py

-   files must be named correctly (by page number with duplicates for each additional image per post. maximum 10 images per post because of instagram limitations). see `test` for example.
-   put images in the folder called `data/raw/{BOOK_NAME}`
-   set parameter in `organize_files.py` and run it
-   it will make a folder for each post in `data/ordered/{BOOK_NAME}/{PAGE}`, which can now be iterated on by the main script

## TODO

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
