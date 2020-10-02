# Mass-Arxiv-downloader
Given a list of titles and authors, attempt to download the pdf if it's on arxiv

This uses Python multiprocess library to download more efficiently. 

File expects a `papers.txt` to read from and a `/pdf/` folder to write to. 

Format of `papers.txt` is having paper title in the first line, then authors in the second line. 

My `papers.txt` has a list of a few papers from the [EMNLP 2019 accepted papers](https://www.emnlp-ijcnlp2019.org/program/accepted/) that I copied and pasted from. 

