import webbrowser
from queries_db.get_all_data_from_bikes import get_all_data_from_bikes

f = open('catalog.html','w')



inicial = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Samuel_Piedra and Noa_Cocaña">
    <meta name="description" content="rent bicycle page">
    <meta name="copyright" content="Samu&Noa">
    <meta name="generator" content="VisualStudioCode">
    <meta name="keywords" content="rent, accesories, shops, bikes, bicycles, type of bicycle">
    <meta http-equiv="content-language" content="text_EN">
    <link rel="stylesheet" href="./proyecto-pydevops/src/html/main.css">
    <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
    <link rel="shortcut icon" href="icon.png">

</head>
<body class="background">
<header>
    <div class="head">  
        <div class="logo">
            <a href="first.html" target="_self"><img src="rb.png" height="65px" width="90px" alt="rental logo"></a>   
        </div>
        <nav class="navbar">
            <a href="index.html" target="_self">Inicio</a>
            <a href="catalog.html" target="_self">Catalog</a>
            <a href="shops.html" target="_self">Shops</a>
            <a href="" target="_self">Contact</a>
            <a href="" target="_self">Products</a>
        </nav>
</header>
<section>
    </div>
    <div class="box-container">"""


menu = ''
for document in get_all_data_from_bikes()['documents']:
    
    name_bike = document['type']
    
    
    menu += f'''<div class="box">
                <i class="fa fa-bicycle"></i>
                <h3>MTB</h3>
                <ul class="c">
                    <li class="c_list">Type: {name_bike.upper()}</li>
                    <li class="c_list">2 characteristics</li>
                    <li class="c_list">3 Price</li>
                    <li class="c_list">4 Add</li>
                    <li class="c_list">1 type</li>
                    <li class="c_list">2 characteristics</li>
                    <li class="c_list">3 Price</li>
                    <li class="c_list">4 Add</li>
                    <li class="c_list">1 type</li>
                    <li class="c_list">2 characteristics</li>
                    <li class="c_list">3 Price</li>
                    <li class="c_list">4 Add</li>
                </ul>

                <div><a href="#" class="btn">Book Now!</a></div>'''
        
final="""</div>
    <div class="box">
    <i class="fa fa-bicycle"></i>
        <h3>Road bike</h3>
            <ul class="c">
                <li class="c_list">1 type</li>
                <li class="c_list">2 characteristics</li>
                <li class="c_list">3 Price</li>
                <li class="c_list">4 Add</li>
                <li class="c_list">1 type</li>
                <li class="c_list">2 characteristics</li>
                <li class="c_list">3 Price</li>
                <li class="c_list">4 Add</li>
                <li class="c_list">1 type</li>
                <li class="c_list">2 characteristics</li>
                <li class="c_list">3 Price</li>
                <li class="c_list">4 Add</li>
            </ul>
            <div><a href="#" class="btn">Book Now!</a></div>
        </div>
    </div>
</section>
</body>
</html>"""

f.write(inicial)
f.write(menu)
f.write(final)
f.close()


webbrowser.open_new_tab('catalog.html')