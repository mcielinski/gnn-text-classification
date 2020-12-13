
import urllib.parse

XML_CHAR_ENTITIES =  {
    '&nbsp;'   :u'\u00A0', '&iexcl;' :u'\u00A1', '&cent;'    :u'\u00A2',
    '&pound;'  :u'\u00A3', '&curren;':u'\u00A4', '&yen;'     :u'\u00A5',
    '&brvbar;' :u'\u00A6', '&sect;'  :u'\u00A7', '&uml;'     :u'\u00A8',
    '&copy;'   :u'\u00A9', '&ordf;'  :u'\u00AA', '&laquo;'   :u'\u00AB',
    '&not;'    :u'\u00AC', '&shy;'   :u'\u00AD', '&reg;'     :u'\u00AE',
    '&macr;'   :u'\u00AF', '&deg;'   :u'\u00B0', '&plusmn;'  :u'\u00B1',
    '&sup2;'   :u'\u00B2', '&sup3;'  :u'\u00B3', '&acute;'   :u'\u00B4',
    '&micro;'  :u'\u00B5', '&para;'  :u'\u00B6', '&middot;'  :u'\u00B7',
    '&cedil;'  :u'\u00B8', '&sup1;'  :u'\u00B9', '&ordm;'    :u'\u00BA',
    '&raquo;'  :u'\u00BB', '&frac14;':u'\u00BC', '&frac12;'  :u'\u00BD',
    '&frac34;' :u'\u00BE', '&iquest;':u'\u00BF', '&Agrave;'  :u'\u00C0',
    '&Aacute;' :u'\u00C1', '&Acirc;' :u'\u00C2', '&Atilde;'  :u'\u00C3',
    '&Auml;'   :u'\u00C4', '&Aring;' :u'\u00C5', '&AElig;'   :u'\u00C6',
    '&Ccedil;' :u'\u00C7', '&Egrave;':u'\u00C8', '&Eacute;'  :u'\u00C9',
    '&Ecirc;'  :u'\u00CA', '&Euml;'  :u'\u00CB', '&Igrave;'  :u'\u00CC',
    '&Iacute;' :u'\u00CD', '&Icirc;' :u'\u00CE', '&Iuml;'    :u'\u00CF',
    '&ETH;'    :u'\u00D0', '&Ntilde;':u'\u00D1', '&Ograve;'  :u'\u00D2',
    '&Oacute;' :u'\u00D3', '&Ocirc;' :u'\u00D4', '&Otilde;'  :u'\u00D5',
    '&Ouml;'   :u'\u00D6', '&times;' :u'\u00D7', '&Oslash;'  :u'\u00D8',
    '&Ugrave;' :u'\u00D9', '&Uacute;':u'\u00DA', '&Ucirc;'   :u'\u00DB',
    '&Uuml;'   :u'\u00DC', '&Yacute;':u'\u00DD', '&THORN;'   :u'\u00DE',
    '&szlig;'  :u'\u00DF', '&agrave;':u'\u00E0', '&aacute;'  :u'\u00E1',
    '&acirc;'  :u'\u00E2', '&atilde;':u'\u00E3', '&auml;'    :u'\u00E4',
    '&aring;'  :u'\u00E5', '&aelig;' :u'\u00E6', '&ccedil;'  :u'\u00E7',
    '&egrave;' :u'\u00E8', '&eacute;':u'\u00E9', '&ecirc;'   :u'\u00EA',
    '&euml;'   :u'\u00EB', '&igrave;':u'\u00EC', '&iacute;'  :u'\u00ED',
    '&icirc;'  :u'\u00EE', '&iuml;'  :u'\u00EF', '&eth;'     :u'\u00F0',
    '&ntilde;' :u'\u00F1', '&ograve;':u'\u00F2', '&oacute;'  :u'\u00F3',
    '&ocirc;'  :u'\u00F4', '&otilde;':u'\u00F5', '&ouml;'    :u'\u00F6',
    '&divide;' :u'\u00F7', '&oslash;':u'\u00F8', '&ugrave;'  :u'\u00F9',
    '&uacute;' :u'\u00FA', '&ucirc;' :u'\u00FB', '&uuml;'    :u'\u00FC',
    '&yacute;' :u'\u00FD', '&thorn;' :u'\u00FE', '&yuml;'    :u'\u00FF',
    '&fnof;'   :u'\u0192', '&Alpha;' :u'\u0391', '&Beta;'    :u'\u0392',
    '&Gamma;'  :u'\u0393', '&Delta;' :u'\u0394', '&Epsilon;' :u'\u0395',
    '&Zeta;'   :u'\u0396', '&Eta;'   :u'\u0397', '&Theta;'   :u'\u0398',
    '&Iota;'   :u'\u0399', '&Kappa;' :u'\u039A', '&Lambda;'  :u'\u039B',
    '&Mu;'     :u'\u039C', '&Nu;'    :u'\u039D', '&Xi;'      :u'\u039E',
    '&Omicron;':u'\u039F', '&Pi;'    :u'\u03A0', '&Rho;'     :u'\u03A1',
    '&Sigma;'  :u'\u03A3', '&Tau;'   :u'\u03A4', '&Upsilon;' :u'\u03A5',
    '&Phi;'    :u'\u03A6', '&Chi;'   :u'\u03A7', '&Psi;'     :u'\u03A8',
    '&Omega;'  :u'\u03A9', '&alpha;' :u'\u03B1', '&beta;'    :u'\u03B2',
    '&gamma;'  :u'\u03B3', '&delta;' :u'\u03B4', '&epsilon;' :u'\u03B5',
    '&zeta;'   :u'\u03B6', '&eta;'   :u'\u03B7', '&theta;'   :u'\u03B8',
    '&iota;'   :u'\u03B9', '&kappa;' :u'\u03BA', '&lambda;'  :u'\u03BB',
    '&mu;'     :u'\u03BC', '&nu;'    :u'\u03BD', '&xi;'      :u'\u03BE',
    '&omicron;':u'\u03BF', '&pi;'    :u'\u03C0', '&rho;'     :u'\u03C1',
    '&sigmaf;' :u'\u03C2', '&sigma;' :u'\u03C3', '&tau;'     :u'\u03C4',
    '&upsilon;':u'\u03C5', '&phi;'   :u'\u03C6', '&chi;'     :u'\u03C7',
    '&psi;'    :u'\u03C8', '&omega;' :u'\u03C9', '&thetasym;':u'\u03D1',
    '&upsih;'  :u'\u03D2', '&piv;'   :u'\u03D6', '&bull;'    :u'\u2022',
    '&hellip;' :u'\u2026', '&prime;' :u'\u2032', '&Prime;'   :u'\u2033',
    '&oline;'  :u'\u203E', '&frasl;' :u'\u2044', '&weierp;'  :u'\u2118',
    '&image;'  :u'\u2111', '&real;'  :u'\u211C', '&trade;'   :u'\u2122',
    '&alefsym;':u'\u2135', '&larr;'  :u'\u2190', '&uarr;'    :u'\u2191',
    '&rarr;'   :u'\u2192', '&darr;'  :u'\u2193', '&harr;'    :u'\u2194',
    '&crarr;'  :u'\u21B5', '&lArr;'  :u'\u21D0', '&uArr;'    :u'\u21D1',
    '&rArr;'   :u'\u21D2', '&dArr;'  :u'\u21D3', '&hArr;'    :u'\u21D4',
    '&forall;' :u'\u2200', '&part;'  :u'\u2202', '&exist;'   :u'\u2203',
    '&empty;'  :u'\u2205', '&nabla;' :u'\u2207', '&isin;'    :u'\u2208',
    '&notin;'  :u'\u2209', '&ni;'    :u'\u220B', '&prod;'    :u'\u220F',
    '&sum;'    :u'\u2211', '&minus;' :u'\u2212', '&lowast;'  :u'\u2217',
    '&radic;'  :u'\u221A', '&prop;'  :u'\u221D', '&infin;'   :u'\u221E',
    '&ang;'    :u'\u2220', '&and;'   :u'\u2227', '&or;'      :u'\u2228',
    '&cap;'    :u'\u2229', '&cup;'   :u'\u222A', '&int;'     :u'\u222B',
    '&there4;' :u'\u2234', '&sim;'   :u'\u223C', '&cong;'    :u'\u2245',
    '&asymp;'  :u'\u2248', '&ne;'    :u'\u2260', '&equiv;'   :u'\u2261',
    '&le;'     :u'\u2264', '&ge;'    :u'\u2265', '&sub;'     :u'\u2282',
    '&sup;'    :u'\u2283', '&nsub;'  :u'\u2284', '&sube;'    :u'\u2286',
    '&supe;'   :u'\u2287', '&oplus;' :u'\u2295', '&otimes;'  :u'\u2297',
    '&perp;'   :u'\u22A5', '&sdot;'  :u'\u22C5', '&lceil;'   :u'\u2308',
    '&rceil;'  :u'\u2309', '&lfloor;':u'\u230A', '&rfloor;'  :u'\u230B',
    '&lang;'   :u'\u2329', '&rang;'  :u'\u232A', '&loz;'     :u'\u25CA',
    '&spades;' :u'\u2660', '&clubs;' :u'\u2663', '&hearts;'  :u'\u2665',
    '&diams;'  :u'\u2666', '&quot;'  :u'\u0022', '&lt;'      :u'\u003C',
    '&gt;'     :u'\u003E', '&OElig;' :u'\u0152', '&oelig;'   :u'\u0153',
    '&Scaron;' :u'\u0160', '&scaron;':u'\u0161', '&Yuml;'    :u'\u0178',
    '&circ;'   :u'\u02C6', '&tilde;' :u'\u02DC', '&ensp;'    :u'\u2002',
    '&emsp;'   :u'\u2003', '&thinsp;':u'\u2009', '&zwnj;'    :u'\u200C',
    '&zwj;'    :u'\u200D', '&lrm;'   :u'\u200E', '&rlm;'     :u'\u200F',
    '&ndash;'  :u'\u2013', '&mdash;' :u'\u2014', '&lsquo;'   :u'\u2018',
    '&rsquo;'  :u'\u2019', '&sbquo;' :u'\u201A', '&ldquo;'   :u'\u201C',
    '&rdquo;'  :u'\u201D', '&bdquo;' :u'\u201E', '&dagger;'  :u'\u2020',
    '&Dagger;' :u'\u2021', '&permil;':u'\u2030', '&lsaquo;'  :u'\u2039',
    '&rsaquo;' :u'\u203A', '&euro;'  :u'\u20AC'
}

def unescape_xml(text):
    for ch in XML_CHAR_ENTITIES:
        if ch in text:
            text = text.replace(ch, XML_CHAR_ENTITIES[ch])
    return text

def get_wiki_document_url(wiki_document_title, prefix):
    quoted_title = urllib.parse.quote(wiki_document_title.replace(' ', '_').encode('utf-8'))
    quoted_title = quoted_title.replace('%28', '(').replace('%29', ')')
    return prefix + quoted_title[0].upper() + quoted_title[1:]

def extract_pages_from_dump(filestream):
    page = []
    for line in filestream:
        line = line.strip()
        if line == '<page>':
            page = []
        elif line == '</page>':
            yield page
            page = []
        else:
            page.append(line)
