# ucsd-css-001.github.io

This is the website for UCSD CSS (Computational Social Science) 1.  

This website is written as a [jupyter book](https://jupyterbook.org/intro.html).  

## Repo structure

`./` contains book `.yml` configurations, this readme, and the main landing page md.   
`./course/` `.md` files pertaining to course structure.  
`./lectures/` mostly `.ipynb` files with lecture content.   
`./labs/` mostly `.ipynb` files for interactive labs.
`./datasets/` various datasets we might use or refer to.  
`./build` contains the files built by jupyter-book


## Building / updating
- book files, and their order, are listed in `./_toc.yml`  
- Build by running  `jupyter-book .`  
- Use [ghp-import](https://jupyterbook.org/publish/gh-pages.html) to move `build/html` to `docs`  

