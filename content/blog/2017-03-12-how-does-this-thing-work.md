Title:  How does this thing work?
Date:   2017-03-12
Category: python, documentation

# Abstract

How does this website work?

# Start

After 9 months I'm returning to this website. The first question I had was "How does this thing work?" 
Of course I didn't document it and I don't remember. Lesson learned. 

# How does this website work? 

## High level overview

This site is hosted for free by [Github](https://github.com/). Thanks Github! The html "code" is at [roryhr/roryhr.github.io](https://github.com/roryhr/roryhr.github.io).

Great. I used a static site generator called Pelican that generates a website from a series markdown text files in a particular directory structure (more on that in a bit).
These files are in a separate repository at
[roryhr/site-code](https://github.com/roryhr/site-code).

## Recipes

Generate the website

	:::bash
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code$ pelican content
	WARNING: empty slug for /home/rory/Projects/site-code/content/pages/index.md. You can fix this by adding a title or a slug to your content
	Done: Processed 7 articles, 0 drafts, 4 pages and 0 hidden pages in 0.23 seconds.
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code$ 



Shell showing the output folder is a Git repo pointing to `roryhr/roryhr.github.io`

	:::bash
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ git status
	On branch master
	Your branch is up-to-date with 'origin/master'.
	Changes not staged for commit:
	  (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   archives.html
		modified:   author/rory-hartong-redden.html
		modified:   authors.html
		modified:   category/opinion.html

	Untracked files:
	  (use "git add <file>..." to include in what will be committed)

		how-does-this-thing-work.html

	no changes added to commit (use "git add" and/or "git commit -a")
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ git remote -v
	origin	https://github.com/roryhr/roryhr.github.io (fetch)
	origin	https://github.com/roryhr/roryhr.github.io (push)
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ 

Run the development server manually (there's also a `.sh` script but I don't use it)
	:::bash
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code$ cd output/
	((blog)) rory@rory-Satellite-S75-B:~/Projects/site-code/output$ python -m pelican.server

