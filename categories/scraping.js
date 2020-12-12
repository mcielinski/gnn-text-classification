// HOW TO USE
// 1. Go to dynamic category tree for specific main category
//    example for Chemia
//    https://pl.wikipedia.org/wiki/Specjalna:Drzewo_kategorii?target=Kategoria%3AChemia&mode=categories&namespaces=&title=Specjalna%3ADrzewo_kategorii
// 2. Set variables and put all code below in console
// 3. Run next() in console
// 4. Do it again after finish all requests (after next level categories are unrolled)
//    Repeat this step until unroll tree to max level
// 5. Run saveJSON() to download categories as json
//    In json: key - category name, value - category level


// variables to set
var max_level = 10;
var timeout = 150;

// returns all unrolled tree elements
function getAllTreeTogglers()
{
    var matchingElements = [];
    var allElements = document.getElementsByTagName('*');
    for (var i = 0, n = allElements.length; i < n; i++)
    {
        if ((allElements[i].getAttribute('title') !== null) & (allElements[i].getAttribute('title') == 'rozwiń'))
    {
        // Element exists with attribute. Add to array.
        matchingElements.push(allElements[i]);
    }
    }
    return matchingElements;
}

// unroll tree to specific level
// and save categories names with level info
var categories = {}
var level = 1;

function next() {
    
    if (level <= max_level) {

        elements = getAllTreeTogglers()
        elements.forEach(el => {
            categories[el.attributes['data-ct-title'].value] = level
            setTimeout(function(){el.click()}, timeout)
            // el.click()
        })
        level = level + 1

    } else {
        console.log('Max level')
    }

}

// download categories as json
function saveJSON() {
    let data = JSON.stringify(categories);
    let bl = new Blob([data], {
       type: "text/html"
    });
    let a = document.createElement("a");
    a.href = URL.createObjectURL(bl);
    a.download = "data.json";
    a.hidden = true;
    document.body.appendChild(a);
    a.innerHTML =
       "someinnerhtml";
    a.click();
 }