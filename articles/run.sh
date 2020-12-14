date +"%H:%M"
bzip2 -dc ./plwiki-20201201-pages-articles-multistream.xml.bz2 | python ./rubyslippers/extract_parallel.py rubyslippers/out/extracted_pages/
date +"%H:%M"