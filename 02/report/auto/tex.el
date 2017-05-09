(TeX-add-style-hook
 "tex"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "graphicx")
   (LaTeX-add-labels
    "fig:loss")
   (LaTeX-add-bibliographies
    "main"))
 :latex)

