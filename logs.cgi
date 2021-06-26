#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html lang='en'>"
# echo "<meta http-equiv="refresh" content="4;url='../index.html'" />"
echo "<head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><script src='./jquery-3.6.0.js'></script><title>Logs</title></head>"
echo "<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        background-color: #89aa9a;
        align-items: center;
        display: flex;
        flex-direction: column;
        font-family: sans-serif;
        justify-content: flex-start;
        min-height: 100vh;
        text-align: center;
    }

    ul {
        list-style: none;
        text-align: left;
    }

    .main {
        align-items: center;
        display: flex;
        flex-direction: column:
        justify-content: center;
    }

    .nav-bar {
        align-items: center;
        background-color: rgb(66, 66, 66);
        box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
        padding: 20px;
        width: 100%;
    }

    .nav-bar a {
        color: white;
        text-decoration: none;
    }

    .nav-bar a:hover {
        color: rgb(173, 173, 173);
    }

    .nav-bar h3 {
        font-size: 1.5rem;
    }
</style>"
echo "</head>"
echo "<body>"
echo "<div class='nav-bar'><a href='/index.html'><h3>PfSense Gateway Monitor</h3></a></div>"
echo "<br>"
echo "<p> </p><a href='../index.html'>Main Menu</a>"
echo "<br>"
echo "<br>"
echo "<ul><li class='log-card'>$(cat /home/www-data/pfsense_gw.log)</li></ul>"
# echo "$(cat /home/www-data/pfsense_gw.log)"
echo "<br>"
echo "<a href='./resetlog.cgi'>Clear the Logs</a>"
echo "<br>"
echo "<a href='./archive.cgi'>Check the archives</a>"
echo "</body>"
echo "<script>$('.nav-bar').click(() => {
            console.log('clicked');
        })</script>"
echo "</html>"
