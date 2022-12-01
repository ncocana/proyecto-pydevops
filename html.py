import webbrowser

f = open('conversion.html','w')

tags = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Samuel_Piedra and Noa_Coca�a">
        <meta name="description" content="rent bicycle page">
        <meta name="copyright" content="Samu&Noa">
        <meta name="generator" content="VisualStudioCode">
        <meta name="keywords" content="rent, accesories, shops, bikes, bicycles, type of bicycle">
        <meta http-equiv="content-language" content="text_EN">
        <link rel="stylesheet" href="./css/styles-main.css">
        <link rel="stylesheet" href="./css/styles-shops.css">
        <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
        <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
        <base target="_self">
    </head>
    <body id="background-shops">
        <header>
            <div class="container-header">
                <div class="container-header-logo">
                    <img src="./img/logo-webpage.png" height="65px" width="90px" alt="rental logo">  
                </div>
                <nav class="nav-menu">
                    <a href="./index.html">Inicio</a>
                    <a href="./catalog.html">Catalog</a>
                    <a href="./shops.html">Shops</a>
                    <a href="">Contact</a>
                    <a href="">Products</a>
                </nav>
            </div>
        </header>
        <section>
            <div class="container-box">
                <div class="box-shops">
                    <i class="fa fa-map-marker" id="icon-shop"></i>
                    <h2>Plaça de Cort</h2>
                    <div class="box-shops-information">
                        <div class="box-shops-information-item">
                            <h3>Address</h3>
                            <p>{aaaa}</p>
                        </div>
                        <div class="box-shops-information-item">
                            <h3>Contact information</h3>
                            <p>{aaaa}</p>
                        </div>
                    </div>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1537.776988476192
                        !2d2.6493669!3d39.5696635!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1297924fe7630673%3A0xd
                        114e77cc940e977!2sPla%C3%A7a%20de%20Cort%2C%2007001%20Palma%2C%20Islas%20Baleares!5e
                        0!3m2!1ses!2ses!4v1669774644226!5m2!1ses!2ses" width="400" height="300" style="borde
                        r:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
                    </iframe> 
                </div>
            </div>
            <div class="container-box">
                <div class="box-shops">
                    <i class="fa fa-map-marker" id="icon-shop"></i>
                    <h2>Plaça de Cort</h2>
                    <div class="box-shops-information">
                        <div class="box-shops-information-item">
                            <h3>Address</h3>
                            <p>{aaaa}</p>
                        </div>
                        <div class="box-shops-information-item">
                            <h3>Contact information</h3>
                            <p>{aaaa}</p>
                        </div>
                    </div>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1537.776988476192
                        !2d2.6493669!3d39.5696635!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1297924fe7630673%3A0xd
                        114e77cc940e977!2sPla%C3%A7a%20de%20Cort%2C%2007001%20Palma%2C%20Islas%20Baleares!5e
                        0!3m2!1ses!2ses!4v1669774644226!5m2!1ses!2ses" width="400" height="300" style="borde
                        r:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
                    </iframe> 
                </div>
            </div>
        </section>
    </body>
</html>'''

f.write(tags)
f.close()


webbrowser.open_new_tab('conversion.html')