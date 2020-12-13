date +"%H:%M"
bzip2 -dc ./plwiki-20201120-pages-articles-multistream.xml.bz2 | python ./rubyslippers/extract_parallel.py extracted-new/
date +"%H:%M"