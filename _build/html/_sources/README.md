# ucsd-css-001.github.io

This is the website for UCSD CSS (Computational Social Science) 1.  

This website is written as a [jupyter book](https://jupyterbook.org/intro.html).  

## Repo structure

`./` contains book `.yml` configurations, this readme, and the main landing page md.   
`./course/` `.md` files pertaining to course structure.  
`./lectures/` mostly `.ipynb` files with lecture content.   
`./labs/` mostly `.ipynb` files for interactive labs.
`./datasets/` various datasets we might use or refer to.  
`./_build` contains the files built by jupyter-book


## Building / updating
- book files, and their order, are listed in `./_toc.yml`  
- Build by running  `jupyter-book build .`  
- Add changes to main, push.    
- `ghp-import -n -p -f _build/html` to export built book to gh-pages branch.  [more here](https://jupyterbook.org/publish/gh-pages.html)  


## TODO

- [ ] fix myst substitutions [myst](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html?highlight=substitution#substitutions-and-urls)  or [jb]()

- [ ] datahub login as grader? 
  
- [ ] datahub login as student?
